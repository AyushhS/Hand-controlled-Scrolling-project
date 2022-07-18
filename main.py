import cv2
import numpy
import mouse
import keyboard
import sys
from handprocessing import *
from mouseprocessing import *
from scrollprocessing import *

cap = cv2.VideoCapture(0)
width = cap.get(3)
height = cap.get(4)
dimensions = (width, height)
is_hand_active = None
hand_state_change = None
is_scrollwheel_active = None
scrollwheel_state_change = None
previous_scrollwheel = None
previous_hand_coordinates = []
previous_mouse_position = []

n = 0 # REMOVE THIS LATER
while cap.isOpened():
    n += 1 # REMOVE THIS LATER
    success, image = cap.read()
    if not success:
        print("Frame not captured, continuing...")
        continue

    image, hand_coordinates = process_coordinates(image, width, height)
    is_hand_active, hand_state_change = hands_change(hand_coordinates, previous_hand_coordinates)
    # print(is_hand_active, hand_state_change)
    if is_hand_active:
        is_scrollwheel_active, scrollwheel_state_change = scroll_change(hand_coordinates, previous_scrollwheel)
        if not is_scrollwheel_active and not scrollwheel_state_change:
            previous_mouse_position = mouse.get_position()
            previous_hand_coordinates = hand_coordinates
        else:
            scrolling(hand_coordinates, previous_hand_coordinates, is_scrollwheel_active, scrollwheel_state_change, previous_mouse_position)

    previous_scrollwheel = is_scrollwheel_active
    if len(sys.argv) > 1:
        if is_hand_active:
            image = draw_hands_on_image(image, hand_coordinates, width, height)
        cv2.imshow('Test', cv2.flip(image, 1))

    if cv2.waitKey(50) & 0xFF == 27:
        break

    if keyboard.is_pressed('Esc'):
        break
cap.release()
cv2.destroyAllWindows()