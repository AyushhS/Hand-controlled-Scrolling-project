# Hand controlled Scrolling Project

This is a project which uses hand gestures to activate the scroll wheel, and uses the index finger to scroll. It can be used in many applications, such as reading various documents/books handsfree, scrolling through presentations, etc.

It uses the google <a href='https://google.github.io/mediapipe/'>medipipe</a> library to provide pretrained hand tracking models, and opencv for cam access and image processing.
## How to Use -

Step 1 - Clone the repo to the desired folder.

Step 2 - Install the required packages -

```
pip install -r requirements.txt
```

Step 3 - Run the main.py file -

```
python main.py
```

Step 4 - Minimize the command window and use hand gestures to control the Scroll-Wheel.

To Stop the Program, go to the terminal window and press the Escape key.

Note - _To see the Hand detection model in action, give any extra argument before running the script._

```
python main.py 1
```
<!--
## Hand Gestures -
 -->

## Hand gestures available for scrolling -

There are 2 gestures by which you can control scrolling, Fist open and Fist close.

![](https://res-1.cloudinary.com/sharecare/image/upload/c_fill,f_auto,g_faces:center,h_515,w_916/v1647284932/slideshows/hand-exercises-02)

The fist open gesture deactivates the scroll function, and fist close activates it. when the fist is closed, the camera tracks the index finger's tip and scrolls the page relative to its position.



---
**UPCOMING FEATURES** - A Fully Hand controlled mouse with left and right clicks, complete with the scroll function.