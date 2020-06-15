# About
This repo contains a binary wheel of custom version of OpenCV

# List of custom features
## OpenCV 3.4.2
### Presentation timestamp support (PTS) in VideoCapture
```
import cv2
cap = cv2.VideoCapture('video.mp4')
_, frame =  cap.read()
pts = cap.get(cv2.CAP_PROP_POS_AVI_RATIO) * cap.get(cv2.CAP_PROP_POS_MSEC)
print(pts)
assert 0 < pts < 10
```

# How to install with PIP
```
pip install https://github.com/cyberj0g/OpenCV-Custom/raw/master/opencv_python-3.4.2.17-cp36-cp36m-manylinux1_x86_64.whl
```

# How to create a binary wheel with customized OpenCV source
STEPS:
1. Build OpenCV Python extension module (.so)
2. Change lib rpath of generated .so with `chrpath -r $ORIGIN/.libs name.so`
3. Find dependencies with `readelf -d` and copy all dependecies except system to opencv_python-3.4.2.17-cp36-cp36m-manylinux1_x86_64/cv2/.libs
4. Generate RECORDS file with record_generator (paste manually)
5. Zip folder and change extension to .whl
6. Check if pip can install it
