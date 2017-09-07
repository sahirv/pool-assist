##### OpenCV installed using Homebrew
  * `brew install opencv3 --with-python3 --without-python`
  * note: change the name of the file in /usr/local/opt/opencv3/lib/python3.6/site-packages to cv2.so

##### TensorFlow installed using pip
  * `pip install tensorflow`

Run server.py with:  
`export FLASK_APP=server.py`    
`python -m flask run`.  
Visit localhost:5000/bd

<img src="Images/after.png" width="800" />
<img src="Images/canny.png" width="800" />
<img src="Images/orig.png" width="800" />



