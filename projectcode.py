import cv2
import time

# Load the Haar Cascade classifier for detecting eyes
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Load the video feed from the webcam
cap = cv2.VideoCapture(0)

# Initialize the alert counter, previous number of detected eyes and delay counter
alert_no = 1
prev_eyes = 0
delay_counter = 0
delay_time = 10  # Set delay time in seconds
#alert_limit = 5
while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the grayscale image
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Check if eyes are detected
    if len(eyes) == 0 and prev_eyes > 0:
        delay_counter += 1
        if delay_counter == delay_time:
            # Display an alert message in a pop-up window
            cv2.putText(frame, f"Alert No : {alert_no}, Be in the screen", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 0, 255), 2)
            cv2.imshow('frame', frame)
            alert_no += 1
            delay_counter = 0
            if cv2.waitKey(1) == ord('q'):
                break
    else:
        prev_eyes = len(eyes)
        delay_counter = 0
        # Draw rectangles around the detected eyes
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
'''
    if alert_no > alert_limit:
        break
'''
# Release the video feed and close the window
cap.release()
cv2.destroyAllWindows()
