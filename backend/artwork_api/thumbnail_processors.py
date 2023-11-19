from easy_thumbnails.processors import scale_and_crop
from PIL import Image, ImageDraw
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

def entropy1d(array):
    if array.size <= 1:
        return 0
    _,counts = np.unique(array, return_counts=True)
    probs = counts/array.size
    ent = 0.0
    for x in probs:
        ent -= x * math.log(x, 2)
    return ent

def image_entropy(image, neighbor_size):
    greyIm = np.array(image.convert('L'))
    S = greyIm.shape
    E = np.empty(S)
    for row in range(S[0]):
        for col in range(S[1]):
            Lx = max(0, col-neighbor_size)
            Ux = min(S[1], col+neighbor_size)
            Ly = max(0, row-neighbor_size)
            Uy = min(S[0], row+neighbor_size)
            region=greyIm[Ly:Uy,Lx:Ux]
            region=region.reshape(region.size)
            E[row,col]=entropy1d(region)
    return E

def detect_face(image):
    greyIm = np.array(image.convert('L'))
    face_cascade = cv2.CascadeClassifier("backend/artwork_api/haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(greyIm, 1.3, 7)
    return faces

def face_scale_and_crop(image, size, **kwargs):
    sw,sh = image.size[0],image.size[1]
    tw,th = size[0],size[1]

    if sw*th//sh < tw:
        nw,nh = tw,sh*tw//sw
        direction = 'v'
    else:
        nw,nh = sw*th//sh,th
        direction = 'h'
    
    faces = detect_face(image)
    rx, ry = nw/sw, nh/sh
    faces = [(int(x*rx),int(y*ry),int(w*rx),int(h*ry)) for (x,y,w,h) in faces]
    #faces = []

    image = image.resize((nw,nh))

    entropyMap = image_entropy(image, 5)
    maxEntropyValue = np.max(entropyMap)
    Image.fromarray((entropyMap/maxEntropyValue*255).astype(np.uint8)).save("entropy.png")

    for (x,y,w,h) in faces:
        entropyMap[y:y+h,x:x+w] = maxEntropyValue*2
        for ix in range(1,w+1):
            if x-ix >= 0:
                entropyMap[y:y+h,x-ix] = maxEntropyValue*(2-ix/w)
            if x+w-1+ix < nw:
                entropyMap[y:y+h,x+w-1+ix] = maxEntropyValue*(2-ix/w)
        for iy in range(1,h+1):
            if y-iy >= 0:
                entropyMap[y-iy,x:x+w] = maxEntropyValue*(2-iy/h)
            if y+h-1+iy < nh:
                entropyMap[y+h-1+iy,x:x+w] = maxEntropyValue*(2-iy/h)

    maxEntropyValue = np.max(entropyMap)
    Image.fromarray((entropyMap/maxEntropyValue*255).astype(np.uint8)).save("entropy_with_face.png")

    #for (x,y,w,h) in faces:
    #    draw = ImageDraw.Draw(image)
    #    draw.rectangle(((x,y),(x+w,y+h)), outline="red", width=1)

    if direction == 'h':
        best_offset = 0
        max_crop_entropy = float('-inf')
        sum_array = np.sum(entropyMap, axis=0)
        for offset in range(nw-tw+1):
            if offset==0:
                crop_entropy = np.sum(sum_array[:tw])
            else:
                crop_entropy = crop_entropy - sum_array[offset-1] + sum_array[offset+tw-1]

            penalty = 0
            for (x,y,w,h) in faces:
                if ((x<offset and x+w>offset) or 
                    (x<offset+tw and x+w>offset+tw)):
                    penalty += (4*maxEntropyValue*w*h)

            if crop_entropy-penalty > max_crop_entropy:
                max_crop_entropy = crop_entropy-penalty
                best_offset = offset
        return image.crop((best_offset, 0, best_offset+tw, th))
    else:
        best_offset = 0
        max_crop_entropy = float('-inf')
        sum_array = np.sum(entropyMap, axis=1)
        for offset in range(nh-th+1):
            if offset==0:
                crop_entropy = np.sum(sum_array[:th])
            else:
                crop_entropy = crop_entropy - sum_array[offset-1] + sum_array[offset+th-1]

            penalty = 0
            for (x,y,w,h) in faces:
                if ((y<offset and y+h>offset) or 
                    (y<offset+th and y+h>offset+th)):
                    penalty += (4*maxEntropyValue*w*h)

            if crop_entropy-penalty > max_crop_entropy:
                max_crop_entropy = crop_entropy-penalty
                best_offset = offset
        return image.crop((0, best_offset, tw, best_offset+th))
        

if __name__ == "__main__":
    image = Image.open('backend/artwork_api/media/a-student-poses-for-a-photo-during-a-visit-with-exercise-71f593-1024.jpg')

    faces = detect_face(image)
    face_image = image.copy()
    for (x,y,w,h) in faces:
        draw = ImageDraw.Draw(face_image)
        draw.rectangle(((x,y),(x+w,y+h)), outline="red", width=5)

    cropped_image = face_scale_and_crop(image, (200,200))

    entropy_image = Image.open('entropy.png')
    entropy_with_face_image = Image.open('entropy_with_face.png')

    image.thumbnail((300,200))
    face_image.thumbnail((300,200))
    entropy_image.thumbnail((300,200))
    entropy_with_face_image.thumbnail((300,200))

    plt.subplot(3,2,1)
    plt.imshow(image)
    plt.subplot(3,2,2)
    plt.imshow(face_image)
    plt.subplot(3,2,3)
    plt.imshow(entropy_image, cmap='gray')
    plt.subplot(3,2,4)
    plt.imshow(entropy_with_face_image, cmap='gray')
    plt.subplot(3,2,5)
    plt.imshow(cropped_image)
    plt.show()


