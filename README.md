# Indian Sign Language (ISL) Hand Tracking and Recognition

This repository contains Python scripts for collecting hand gesture data and processing it for Indian Sign Language (ISL) recognition using **MediaPipe** and **OpenCV**.

---

## Contents

1. [Project Overview](#project-overview)
2. [File Descriptions](#file-descriptions)
3. [Requirements](#requirements)
4. [Usage Instructions](#usage-instructions)
5. [Examples](#examples)

---

## Project Overview

The goal of this project is to build a robust system for hand gesture tracking and recognition using **MediaPipe Hands** and **MediaPipe Holistic**. The system comprises:
- **Data Collection:** Capturing hand gesture images labeled with specific ISL alphabets for training.
- **Model Building:** Detecting and visualizing hand, face, and pose landmarks in real-time.

---

## File Descriptions

### 1. `datacollection.py`

- **Purpose:** 
  Collect labeled hand gesture images for building the dataset.
  
- **Key Features:**
  - Real-time hand detection and visualization using MediaPipe Hands.
  - Capture landmarks in a white background for better feature extraction.
  - Save images organized by class labels (e.g., `A`, `B`, `C`, etc.).
  - Keyboard controls:
    - `q`: Quit the application.
    - `n`: Switch to the next letter class.
    - `a`: Toggle save mode (ON/OFF).
    - `z`: Save current frame when save mode is ON.

---

### 2. `model.py`

- **Purpose:** 
  Process video frames and draw landmarks for holistic body tracking.

- **Key Features:**
  - Real-time tracking of face, pose, and hand landmarks using MediaPipe Holistic.
  - Styled visualizations of landmarks with distinct colors for better clarity.
  - Tracks left-hand landmarks specifically and outputs their count.
  - Access results after capturing is complete.

---

## Requirements

Install the following Python libraries before running the scripts:

```bash
pip install mediapipe opencv-python matplotlib numpy
