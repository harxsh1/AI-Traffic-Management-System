 AI-Based Traffic Management System

* Introduction
Traffic congestion is a common problem in cities and it leads to delays, fuel wastage, and pollution. Traditional traffic signals work on fixed timings and do not consider real-time traffic conditions.

In this project, we are trying to solve this problem using Artificial Intelligence. The system analyzes traffic using camera input, detects vehicles, predicts congestion, and adjusts signal timings accordingly.

* Objective
The main objective of this project is to build a smart traffic system that can:
- Detect vehicles in real-time using YOLO
- Predict traffic congestion using Machine Learning
- Adjust signal timings based on traffic conditions
- Display all the information on a simple dashboard


* Technologies Used
- Python  
- OpenCV  
- YOLO (Ultralytics)  
- Scikit-learn  
- Flask  
- HTML, CSS, JavaScript  
- SUMO Simulator  

* Project Structure
AI-Traffic-Management-System/
│
├── backend/
│ ├── yolo_test.py
│ ├── ml_test.py
│ ├── signal.py
│
├── frontend/
│ ├── index.html
│
├── requirements.txt
├── README.md

* How the System Works
- First, the system takes video input from a camera or dataset  
- YOLO model detects vehicles and counts them  
- Based on this data, the ML model predicts congestion level (Low, Medium, High)  
- Then, signal timing is adjusted according to the traffic  
- Finally, all the data is shown on the dashboard  

* How to Run
1. Install required libraries:
* How the System Works
- First, the system takes video input from a camera or dataset  
- YOLO model detects vehicles and counts them  
- Based on this data, the ML model predicts congestion level (Low, Medium, High)  
- Then, signal timing is adjusted according to the traffic  
- Finally, all the data is shown on the dashboard  

* How to Run
1. Install required libraries:
pip install -r requirements.txt

2. Run the detection:
python backend/yolo_test.py

* Expected Output
- Vehicles detected in real-time with bounding boxes  
- Congestion level prediction  
- Signal timing based on traffic  
- Simple dashboard to view results  

* Team Members
- Harsh Mohan Mishra 
- Harsh Pandey 
- Abhay Ranjan Mishra 
- Krishna Singh Chauhan 

* Future Scope
- Integration with real-time CCTV cameras  
- Use of Google Maps data  
- Deployment on edge devices like Raspberry Pi  
- Handling multiple traffic intersections  

* Conclusion
This project shows how AI can be used in real-life problems like traffic management. It can help in reducing congestion and improving traffic flow. With further improvements, this system can be used in smart city applications.