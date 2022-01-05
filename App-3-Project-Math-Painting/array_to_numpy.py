import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255,255,0]
print(data)

#make a red patch
#accessing rows
#data[1:3] = [255,0 ,0]

#accessing columns
#data[:, 1:3] = [255,0,0]

#accessing rows + colums
data[0:3, 0:3] = [255,0,0]
data[3:5,2:3] = [45,67,43]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
print("="*50)
print(data)
