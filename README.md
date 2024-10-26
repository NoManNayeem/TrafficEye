
# TrafficEye

TrafficEye is a real-time vehicle detection and classification application built with Flask and YOLOv5. It detects, classifies, and counts vehicles from a live video feed, providing valuable data for traffic analysis, road safety planning, and congestion management.

## Features

- **Real-Time Detection and Classification**: Detects and classifies vehicles such as cars, buses, trucks, and motorcycles.
- **Unique Counting**: Ensures each vehicle is counted only once as it crosses a designated counting line.
- **Modern Video Player Interface**: Includes play/pause controls, a progress bar, and volume adjustment for a better user experience.
- **Responsive Design**: Styled with Bootstrap for responsiveness and modern aesthetics.
- **Statistics Dashboard**: Displays vehicle counts and average speed in a dynamic and interactive dashboard.

## Technologies Used

- **Flask** - For backend server and routing.
- **YOLOv5** - For vehicle detection and classification.
- **OpenCV** - For video feed processing and frame management.
- **Bootstrap & Font Awesome** - For responsive, modern UI design.
- **Python** - The core language for backend processing.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/NoManNayeem/TrafficEye.git
   ```

2. Navigate to the project directory:
   ```bash
   cd TrafficEye
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to view the real-time vehicle detection dashboard.

## Project Structure

```plaintext
TrafficEye/
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies
├── static/                 # Static assets (CSS, icons)
├── templates/              # HTML templates
├── utils/                  # Utility functions (YOLOv5 model and detection logic)
│   └── detector.py         # Vehicle detection and counting logic
├── videos/                 # Sample video files
└── README.md               # Project documentation
```

## Future Enhancements

- **Enhanced Tracking**: Improve vehicle tracking for more accurate counting over time.
- **Data Storage**: Store historical vehicle counts in a database for long-term analysis.
- **Enhanced Speed Calculation**: Use frame rate and distance calibration for accurate speed metrics.

## License

This project is licensed under the MIT License.

---

TrafficEye provides an easy-to-use, effective system for real-time traffic monitoring, combining state-of-the-art detection with an intuitive interface.
