import skimage as si
from skimage.color import rgb2gray
from skimage.transform import rescale
import av
import pandas as pd
import numpy as np

thresh = 0.4
totalFrames = 6573
includedFrames = totalFrames

i = 0
holymoly = np.zeros((96*128*includedFrames, 2))
container = av.open("C:/Users/joonatan/Documents/BadApple/Bad Apple!!.mp4")
for frame in container.decode(video=0):
    img = np.where(rescale(rgb2gray(np.array(frame.to_image())), 0.25, anti_aliasing=False) > thresh, 0, 1)
    for j, row in enumerate(img):
        for k, pixel in enumerate(row):
            if pixel == 1:
                holymoly[(j*128)+(i*128*96)+k][0] = k
                holymoly[(j*128)+(i*128*96)+k][1] = 96 - j + 10
            else:
                holymoly[(j*128)+(i*128*96)+k][0] = k
                holymoly[(j*128)+(i*128*96)+k][1] = 0
    
    i += 1
    if (i == includedFrames):
        break

df = pd.DataFrame(holymoly)
df.to_csv('data.csv', header=False, index=False)
