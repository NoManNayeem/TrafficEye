# Project Structure

```
vehicle_counter/          # Root project directory
├── app.py                # Main Flask application
├── requirements.txt      # Dependencies file
├── static/               # Static files (CSS, JavaScript, images, etc.)
│   └── style.css         # Styles for the web app (optional for now)
├── templates/            # HTML templates for rendering pages
│   └── index.html        # Main page for video display and results
├── utils/                # Utility functions for video handling and YOLO detection
│   └── detector.py       # Script for loading YOLO model and processing video frames
├── videos/               # Folder for storing local video files
│   └── sample_video.mp4  # Placeholder video (can add more here)
└── README.md             # Project documentation (optional)

```