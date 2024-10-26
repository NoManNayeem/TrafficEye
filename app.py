from flask import Flask, render_template, Response
import cv2
from utils.detector import VehicleDetector

app = Flask(__name__)
video_source = './videos/sample_video.mp4'  # Path to video file
detector = VehicleDetector()  # Initialize the vehicle detector

@app.route('/')
def index():
    # Render the main HTML page
    return render_template('index.html')

def generate_frames():
    # Capture video feed
    cap = cv2.VideoCapture(video_source)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect vehicles and get annotated frame with updated counts
        annotated_frame, counts = detector.detect_and_count(frame)

        # Encode the frame in JPEG format for streaming
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        # Yield frame as byte stream for live video feed
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    # Release video capture when done
    cap.release()

@app.route('/video_feed')
def video_feed():
    # Route for the video feed
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
