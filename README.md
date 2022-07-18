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


---
**UPCOMING FEATURES** - A Fully Hand controlled mouse with left and right clicks, complete with the scroll function.