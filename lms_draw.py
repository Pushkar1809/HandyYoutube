import mediapipe as mp
import cv2
import numpy as np
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
feed = cv2.VideoCapture(1)

p_time = 0
c_time = 0

while True:
    _, frame = feed.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                print(id, lm)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # print(results.multi_hand_landmarks)
    c_time = time.time()
    fps = 1/(c_time - p_time)

    p_time = c_time

    # cv2.putText(frame, str(int(fps)), (10, 70),
    #             cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)

    cv2.imshow("Gestutre Recognizer", frame)
    k = cv2.waitKey(30)
    if k == 27:
        break