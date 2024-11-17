import cv2
import os
import mediapipe as mp
import numpy as np  # Ensure numpy is imported

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Paths for saving data
data_path = r"C:\Users\harryy\Desktop\harshadisl\Data"
os.makedirs(data_path, exist_ok=True)

# Variables for toggling save mode and letter class
save_mode = False
current_letter = "B"

# Function to create folder for a specific letter
def create_folder(letter):
    folder_path = os.path.join(data_path, letter)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

# Start webcam feed
cap = cv2.VideoCapture(0)
counter = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting.")
        break

    # Flip frame and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with MediaPipe Hands
    results = hands.process(rgb_frame)
    annotated_frame = frame.copy()

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = hand_info.classification[0].label  # "Left" or "Right"
            # Set contrasting dark colors for hands
            if hand_label == "Left":
                color = (0, 128, 0)  # Dark green for left hand
            else:
                color = (0, 0, 128)  # Dark red for right hand

            # Draw landmarks
            mp_drawing.draw_landmarks(
                annotated_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=color, thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=color, thickness=2)
            )

    # White background for landmarks only
    landmark_frame = 255 * np.ones_like(frame)
    if results.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = hand_info.classification[0].label  # "Left" or "Right"
            # Set contrasting dark colors for hands
            if hand_label == "Left":
                color = (0, 128, 0)  # Dark green for left hand
            else:
                color = (0, 0, 128)  # Dark red for right hand

            mp_drawing.draw_landmarks(
                landmark_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=color, thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=color, thickness=2)
            )

    # Show frames
    cv2.imshow("Hand Tracking", annotated_frame)
    cv2.imshow("Landmarks Only", landmark_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Quit
        break
    elif key == ord('n'):  # Switch to next letter on pressing 'n'
        current_letter = chr((ord(current_letter) - ord('A') + 1) % 26 + ord('A'))
        print(f"Current letter: {current_letter}")
    elif key == ord('a'):  # Toggle save mode on pressing 'a'
        save_mode = not save_mode
        print(f"Save mode: {'ON' if save_mode else 'OFF'}")

    # Save images when 'z' is held down and save mode is ON
    if save_mode and key == ord('z'):  # Only save when 'z' is held down
        folder_path = create_folder(current_letter)
        img_name = f"{current_letter}_{counter}.jpg"
        img_path = os.path.join(folder_path, img_name)
        cv2.imwrite(img_path, landmark_frame)
        print(f"Saved: {img_path}")
        counter += 1

# Cleanup
cap.release()
cv2.destroyAllWindows()
