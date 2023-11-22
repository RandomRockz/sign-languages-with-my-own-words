import cv2
import mediapipe as mp

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe Drawing module for visualizing landmarks
mp_drawing = mp.solutions.drawing_utils

# Initialize a video capture object
cap = cv2.VideoCapture(0)  # Use the default camera (you can change this to a video file)

# Define the "I love you" sign recognizer
def recognize_ily_sign(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    little_tip = landmarks[20]

    # Check if fingers are in the extended position
    is_ily_sign = (
        thumb_tip.y > index_tip.y and
        thumb_tip.y > little_tip.y 
    )

    return is_ily_sign
def recognize_please(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    # Check if fingers are in the extended position
    is_please = (
        thumb_tip.y < index_tip.y and
        index_tip.y < middle_tip.y and
        middle_tip.y < ring_tip.y and
        ring_tip.y < little_tip.y 

    )
    return is_please
def recognize_yellow(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    # Check if fingers are in the extended position
    is_yellow = (
        thumb_tip.y < index_tip.y and
        little_tip.y < middle_tip.y and
        little_tip.y < ring_tip.y and
        little_tip.y < thumb_tip.y 

    )
    return is_yellow

def recognize_luck(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    # Check if fingers are in the extended position
    is_luck = (
        thumb_tip.y > index_tip.y and
        index_tip.y < middle_tip.y and
        middle_tip.y < ring_tip.y and
        ring_tip.y < little_tip.y 



    )
    return is_luck

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)  # Mirror the frame for a more natural feel

    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Convert hand landmarks to a list for gesture recognition
            landmarks = []
            for point in hand_landmarks.landmark:
                landmarks.append(point)

            # Recognize "I love you" sign gesture
            is_ily_sign = recognize_ily_sign(landmarks)
            please=recognize_please(landmarks)
            luck=recognize_luck(landmarks)
            yellow=recognize_yellow(landmarks)
            if is_ily_sign:
                cv2.putText(frame, "I Love You", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            if please:
                cv2.putText(frame, "Please", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            if luck:
                cv2.putText(frame, "Luck", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            if yellow:
                cv2.putText(frame, "Yellow", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            # Visualize the hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
