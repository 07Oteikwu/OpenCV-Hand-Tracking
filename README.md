Hand Tracking & Object Detection with YOLOv5 and MediaPipe 🖐️🎯🔊
This project combines real-time hand tracking using MediaPipe and object detection using YOLOv5 to create an interactive experience. It also integrates sound effects with pygame for a fun and engaging user experience.

✨ Features
🖐️ Hand Tracking:

Detects and tracks hands in real-time using MediaPipe.

Visualizes hand landmarks and connections.

🎯 Object Detection:

Uses YOLOv5 to detect objects in real-time from your webcam feed.

Click on objects to lock and track them dynamically.

🔊 Sound Integration:

Plays a machine gun sound when all five fingers are raised.

Stops the sound when fingers are lowered.

🖱️ Interactive Interface:

Click on objects to select and track them.

Press F to play the sound, S to stop it, and Q to quit.

💻 Controls
Key	Action
Click	Select object for tracking.
ESC	Remove object selection.
F	Play machine gun sound.
S	Stop sound playback.
Q	Quit the program.
📂 Requirements
Python 3.x

opencv-python

mediapipe

pygame

torch (for YOLOv5)

numpy

🚀 How It Works
Hand Tracking:

MediaPipe detects and tracks hands in real-time.

Raises all five fingers to trigger the machine gun sound.

Object Detection:

YOLOv5 detects objects in the webcam feed.

Click on an object to lock and track it.

Sound Integration:

Plays a looping machine gun sound when all fingers are raised.

Stops the sound when fingers are lowered.

📌 Installation & Usage
Clone the Repository:

bash
Copy
git clone https://github.com/07Oteikwu/OpenCV-Hand-Tracking.git
Install Dependencies:

bash
Copy
pip install opencv-python mediapipe pygame torch torchvision numpy
Run the Program:

bash
Copy
python openCV_project.py
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📸 Demo
[Insert a link to a demo video or GIF here]

🛠️ Troubleshooting
Sound Not Playing:

Ensure the sound file (Machine Gun - QuickSounds.com.mp3) is in the same directory as the script.

Hand Tracking Issues:

Ensure your hand is clearly visible to the camera.

Adjust lighting conditions for better detection.

Object Detection Issues:

Ensure the YOLOv5 model is loaded correctly.

Adjust the confidence threshold in the script if needed.

📝 Notes
The project is designed for educational and entertainment purposes.

Feel free to modify and extend the code to suit your needs
