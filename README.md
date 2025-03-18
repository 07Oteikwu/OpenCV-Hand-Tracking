# **Hand Tracking & Object Detection with YOLOv5 and MediaPipe** 🖐️🎯🔊

This project combines **real-time hand tracking** using **MediaPipe** and **object detection** using **YOLOv5** to create an interactive experience. It also integrates sound effects with `pygame` for a fun and engaging user experience.

---

## **✨ Features**

- **🖐️ Hand Tracking:**
  - Detects and tracks hands in real-time using **MediaPipe**.
  - Visualizes hand landmarks and connections.

- **🎯 Object Detection:**
  - Uses **YOLOv5** to detect objects in real-time from your webcam feed.
  - Click on objects to lock and track them dynamically.

- **🔊 Sound Integration:**
  - Plays a machine gun sound when all five fingers are raised.
  - Stops the sound when fingers are lowered.

- **🖱️ Interactive Interface:**
  - Click on objects to select and track them.
  - Press `F` to play the sound, `S` to stop it, and `Q` to quit.

---

## **💻 Controls**

| Key  | Action                             |
|------|-----------------------------------|
| Click| Select object for tracking.       |
| ESC  | Remove object selection.          |
| F    | Play machine gun sound.           |
| S    | Stop sound playback.              |
| Q    | Quit the program.                 |

---

## **📂 Requirements**

- Python 3.x
- `opencv-python`
- `mediapipe`
- `pygame`
- `torch` (for YOLOv5)
- `numpy`

---

## **🚀 How It Works**

1. **Hand Tracking:**
   - MediaPipe detects and tracks hands in real-time.
   - Raises all five fingers to trigger the machine gun sound.

2. **Object Detection:**
   - YOLOv5 detects objects in the webcam feed.
   - Click on an object to lock and track it.

3. **Sound Integration:**
   - Plays a looping machine gun sound when all fingers are raised.
   - Stops the sound when fingers are lowered.

---

## **📌 Installation & Usage**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/07Oteikwu/OpenCV-Hand-Tracking.git
