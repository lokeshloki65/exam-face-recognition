import cv2
import matplotlib.pyplot as plt
import time
import random
import threading

# Face detection setup
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize data for plotting
xdata, ydata = [], []

def update_graph():
    """Function to update the Matplotlib graph in a separate thread."""
    plt.ion()  # Interactive mode ON
    fig, ax = plt.subplots()
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Time")
    ax.set_ylabel("Cheat Probability")
    ax.set_title("SUSpicious Behaviour Detection")
    ax.grid(True)

    line, = ax.plot(xdata, ydata, 'r-', markersize=2, label="Cheat Probability")
    ax.legend()

    while True:
        if len(xdata) > 200:  # Keep only last 200 points
            xdata.pop(0)
            ydata.pop(0)

        xdata.append(len(xdata))
        ydata.append(random.uniform(0, 0.3))  # Fake cheat probability

        line.set_xdata(xdata)
        line.set_ydata(ydata)
        ax.relim()
        ax.autoscale_view()

        plt.draw()
        plt.pause(0.1)  # Prevent freezing

def run_graph():
    """Function to handle face detection and plotting in parallel."""
    threading.Thread(target=update_graph, daemon=True).start()  # Run graph in separate thread

    cap = cv2.VideoCapture(0)  # Open webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error accessing webcam")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        if len(faces) == 0:
            print("⚠ Warning: No face detected!")

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

