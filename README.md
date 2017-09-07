##### OpenCV installed using Homebrew
  * `brew install opencv3 --with-python3 --without-python`
  * note: change the name of the file in /usr/local/opt/opencv3/lib/python3.6/site-packages to cv2.so

##### TensorFlow installed using pip
  * `pip install tensorflow`

Run server.py with:  
`export FLASK_APP=server.py`    
`python -m flask run`.  
Visit localhost:5000/bd

Initial picture sent to the service  
<img src="Images/after.png" width="500" />

The result of canny edge detection on the previous image having already undergone
a 3x3 gaussian filter  
<img src="Images/canny.png" width="500" />

Hough circle transform applied to the previous canny edge detection
results. The circles found are drawn on the first image for reference.  
<img src="Images/orig.png" width="500" />

Then by applying a mask above the coordinates of the circles
and imposing original image on top of the mask, the individual balls
can be extracted for classification.  
<img src="Images/ball1.png" width="260" />
<img src="Images/ball2.png" width="260" />
<img src="Images/ball3.png" width="260" />
<img src="Images/ball4.png" width="260" />
<img src="Images/ball5.png" width="260" />
<img src="Images/ball6.png" width="260" />



