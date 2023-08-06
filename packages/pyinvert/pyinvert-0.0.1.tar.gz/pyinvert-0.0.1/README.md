# invert
Image inversion in python (OpenCV & numpy)

## Usage
### example
```
import cv2
from pyinvert import invert

image = cv2.imread('house.tiff')

new = invert(image)
cv2.imwrite('invertedhouse.tiff', new)
```
**Original Image**
![A Blue car in front of a house](https://github.com/garbage1010/invert/blob/main/tests/house.tiff)

**Inverted**
![Inversion of the previous image](https://github.com/garbage1010/invert/blob/main/tests/invertedhouse.tiff)
