import cv2
import numpy as np
import mediapipe as mp
import pygame
import torch

# Initialize Pygame for sound
pygame.init()
pygame.mixer.init()
gun_sound = pygame.mixer.Sound("Machine Gun - QuickSounds.com.mp3")  # Ensure this file is in the same directory

# Initialize MediaPipe for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Load YOLOv5 model
print("Loading YOLOv5 model...")
try:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, trust_repo=True)
    print("YOLOv5 model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Initialize webcam
print("Accessing webcam...")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam. Please check if the webcam is connected and accessible.")
    exit()

# Set video resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Variables for hand tracking
is_playing = False  # Track if the gun sound is playing

# Variables for object detection
clicked_position = None
selected_bbox = None
fixed_bbox_size = None  # Keep the original size of the selected bounding box

# Mouse callback function to handle clicks
def click_event(event, x, y, flags, param):
    global clicked_position
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button clicked
        clicked_position = (x, y)
        print(f"Mouse clicked at: {clicked_position}")

# Function to calculate IoU (Intersection over Union)
def calculate_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1p, y1p, x2p, y2p = box2

    # Intersection
    xi1 = max(x1, x1p)
    yi1 = max(y1, y1p)
    xi2 = min(x2, x2p)
    yi2 = min(y2, y2p)
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)

    # Union
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2p - x1p) * (y2p - y1p)
    union_area = box1_area + box2_area - inter_area

    return inter_area / union_area if union_area > 0 else 0

# Create a window and set mouse callback
cv2.namedWindow("OpenCV Project", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("OpenCV Project", click_event)

print("Starting real-time detection... Press 'ESC' to remove highlight, 'F' to play gunshot sound, 'S' to stop sound, or 'Q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture frame.")
        break

    # Flip the frame horizontally for natural interaction
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand tracking
    hand_results = hands.process(rgb_frame)

    # Hand Tracking Logic
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Check if all five fingers are up
            finger_tips = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]]

            finger_bases = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
                            hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
                            hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
                            hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP],
                            hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]]

            fingers_up = [tip.y < base.y for tip, base in zip(finger_tips, finger_bases)]

            if all(fingers_up):
                if not is_playing:
                    gun_sound.play(-1)  # Loop the sound
                    is_playing = True
                cv2.putText(frame, 'Target Engaged', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                if is_playing:
                    gun_sound.stop()
                    is_playing = False

    # Object Detection Logic
    detection_results = model(frame)
    detected_objects = []

    # Parse detection results
    for *bbox, conf, label in detection_results.xyxy[0].cpu().numpy():
        if conf < 0.6:  # Confidence threshold
            continue
        x_min, y_min, x_max, y_max = map(int, bbox)
        detected_objects.append((x_min, y_min, x_max, y_max))

    # Check if a click occurred and update selected item
    if clicked_position:
        for (x_min, y_min, x_max, y_max) in detected_objects:
            if x_min <= clicked_position[0] <= x_max and y_min <= clicked_position[1] <= y_max:
                selected_bbox = (x_min, y_min, x_max, y_max)
                fixed_bbox_size = (x_max - x_min, y_max - y_min)  # Save initial size
                print(f"Locked onto object at: {selected_bbox}")
                clicked_position = None  # Reset clicked position
                break

    # Dynamically track the selected item
    if selected_bbox:
        max_iou = 0
        best_bbox = None

        for (x_min, y_min, x_max, y_max) in detected_objects:
            current_bbox = (x_min, y_min, x_max, y_max)
            iou = calculate_iou(selected_bbox, current_bbox)

            if iou > max_iou:  # Update if IoU is better
                max_iou = iou
                best_bbox = current_bbox

        # Update the selected bounding box position while keeping size constant
        if best_bbox and fixed_bbox_size:
            selected_center = (
                (best_bbox[0] + best_bbox[2]) // 2,
                (best_bbox[1] + best_bbox[3]) // 2,
            )
            box_width, box_height = fixed_bbox_size

            # Calculate new top-left and bottom-right corners
            x_min = selected_center[0] - box_width // 2
            y_min = selected_center[1] - box_height // 2
            x_max = selected_center[0] + box_width // 2
            y_max = selected_center[1] + box_height // 2

            # Update selected_bbox and draw the fixed bounding box
            selected_bbox = (x_min, y_min, x_max, y_max)
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)  # Green box for tracking

    # Display the frame
    cv2.imshow("OpenCV Project", frame)

    # Handle keyboard input
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key to clear selection
        selected_bbox = None
        print("Highlight removed.")
    elif key == ord('f'):  # Play gunshot sound on 'F' key
        print("Gunshot sound triggered.")
        pygame.mixer.music.play(-1)  # Loop the sound indefinitely
    elif key == ord('s'):  # Stop gunshot sound on 'S' key
        print("Gunshot sound stopped.")
        pygame.mixer.music.stop()
    elif key == ord('q'):  # Quit on 'Q' key
        print("Exiting real-time detection...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
pygame.quit()
print("Program terminated.")