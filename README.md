## YOLOv5 Real-Time Object Detection & Dynamic Tracking 🔍🎯

This project implements **real-time object detection and tracking** using a pre-trained **YOLOv5 model** via PyTorch. It also integrates sound effects with `pygame` for a fun and interactive experience.

### ✨ Features
- **📸 Real-Time Detection:** Utilizes YOLOv5 to detect objects from webcam input with high accuracy.
- **📍 Dynamic Tracking:** Automatically tracks the selected object even when it moves, using **Intersection over Union (IoU)** calculation.
- **🖱️ Interactive Interface:**
  - Click on objects to lock and track them.
  - Adjust bounding boxes to maintain original size during tracking.
- **🔊 Audio Integration:**
  - Plays machine gun sound with `pygame` when triggered.
  - Continuous looping and easy stopping of sound playback.
- **⚙️ Configurable Thresholds:** Adjustable confidence threshold for improved detection accuracy.

### 💻 Controls
| Key  | Action                             |
|------|-----------------------------------|
| Click| Select object for tracking.       |
| ESC  | Remove object selection.          |
| F    | Play machine gun sound.           |
| S    | Stop sound playback.              |
| Q    | Quit the program.                 |

### 📂 Requirements
- `torch`
- `opencv-python`
- `pygame`
- `numpy`

### 🚀 How It Works
1. **Object Detection:** YOLOv5 detects objects in real-time from your webcam feed.
2. **Object Selection:** Click on any detected object to lock onto it.
3. **Object Tracking:** The program tracks the object even if it moves, maintaining the original bounding box size.
4. **Sound Effects:** Trigger machine gun sounds with keyboard interaction.

### 📌 Installation & Usage
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required packages:
   ```bash
   pip install torch opencv-python pygame numpy
   ```
3. Run the program:
   ```bash
   python <your_script_name>.py
   ```



