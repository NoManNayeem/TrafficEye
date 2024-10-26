from ultralytics import YOLO
import cv2

class VehicleDetector:
    def __init__(self):
        # Load YOLOv5 model with pretrained weights
        self.model = YOLO('https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt')
        
        # Dictionary to store vehicle counts
        self.vehicle_count = {
            "cars": 0,
            "buses": 0,
            "trucks": 0,
            "motorcycles": 0,
            "others": 0,
            "total": 0
        }
        
        # Set to store unique vehicle IDs that have been counted
        self.tracked_vehicles = set()
        
        # Define a counting line (y-coordinate) for vehicles to cross
        self.counting_line_y = 300  # Adjust based on video frame

    def detect_and_count(self, frame):
        # Run YOLOv5 detection on the frame
        results = self.model(frame)
        annotated_frame = results[0].plot()  # Get frame with annotations
        
        # Temporary set to store new vehicle IDs in the current frame
        new_vehicles = set()

        for box in results[0].boxes:
            label = int(box.cls.item())  # Get the class label as integer
            x1, y1, x2, y2 = box.xyxy[0].tolist()  # Get bounding box coordinates
            
            x_center = int((x1 + x2) / 2)
            y_center = int((y1 + y2) / 2)

            # Generate a unique ID for each detected vehicle based on class and coordinates
            vehicle_id = f"{label}_{x_center}_{y_center}"
            
            # Check if the vehicle has crossed the counting line and hasn't been counted yet
            if vehicle_id not in self.tracked_vehicles and y_center > self.counting_line_y:
                new_vehicles.add(vehicle_id)

                # Increment count based on vehicle type
                if label == 2:  # Car
                    self.vehicle_count["cars"] += 1
                elif label == 5:  # Bus
                    self.vehicle_count["buses"] += 1
                elif label == 7:  # Truck
                    self.vehicle_count["trucks"] += 1
                elif label == 3:  # Motorcycle
                    self.vehicle_count["motorcycles"] += 1
                else:
                    self.vehicle_count["others"] += 1

        # Update total count and tracked vehicles
        self.vehicle_count["total"] = sum(self.vehicle_count.values())
        self.tracked_vehicles.update(new_vehicles)  # Add new vehicles to tracked set

        return annotated_frame, self.vehicle_count
