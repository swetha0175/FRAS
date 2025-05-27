# FRAS: Facial Recognition Attendance System

FRAS is an AI-powered Facial Recognition Attendance System that automates attendance tracking using internal or external webcams. It leverages facial recognition technology to identify and log user attendance seamlessly into a MySQL database.

---

## Table of Contents
- [🚀 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🧠 How It Works](#-how-it-works)
- [Project Scope](#project-scope)  
- [Project Objectives](#project-objectives)  
- [Project Requirements](#project-requirements)  
  - [Hardware Requirements](#hardware-requirements)  
  - [Software Requirements](#software-requirements)  
  - [Python Library Requirements](#python-library-requirements)  
- [Installation & Usage](#installation--usage)  
- [Images](#images)  
- [Recommended Image Guidelines for Facial Recognition](#recommended-image-guidelines-for-facial-recognition)  
- [🛠️ Troubleshooting](#-troubleshooting)
- [🙋‍♂️ Author & Acknowledgements](#-author--acknowledgements)
- [Important Notes](#important-notes)

---

## 🚀 Features

- Real-time facial recognition for attendance logging  
- Secure MySQL integration for data persistence  
- User registration via webcam  
- Error handling and performance optimized  
- Compatible with external and internal webcams

---

## 📂 Project Structure

```plaintext
FRAS/
│
├── FRAS_Main.py             # Main script for attendance taking
├── FRAS_Registration.py     # Registration system for new users
├── images/                  # Sample and saved images for facial recognition
├── README.md                # Project documentation

```
---

## 🧠 How It Works

1. User registers their face using `FRAS_Registration.py`.  
2. `FRAS-main-system.py` captures multiple facial encodings using `face_recognition`.  
3. During attendance (`FRAS_main-system.py`), the webcam captures live frames and compares with known encodings.  
4. On match, the user's attendance is marked and logged in MySQL with a timestamp.

---

## Project Scope

The primary scope of FRAS is to simplify and digitize the attendance process by reducing manual errors and minimizing the time required for traditional attendance-taking methods.

---

## Project Objectives

The main objective of FRAS is to accurately capture attendance using facial recognition via a webcam and log the data into a MySQL database. This system enhances efficiency and improves the integrity of attendance records.

---

## Project Requirements

### Hardware Requirements
- Laptop with webcam (internal or external)  
- CPU: 11th Gen Intel or more (recommended)  
- RAM: 16 GB or higher

### Software Requirements
- Python 3.9  (3.10 - 3.12 not recommended since some version are not compatible with face_recognition library)
- PyCharm IDE (Any version)
- MySQL Server & MySQL Workbench (Any version)

### Python Library Requirements
Make sure the following libraries are installed within PyCharm:

- `face_recognition==1.3.0`  
- `face_recognition_model==0.3.0`  
- `opencv-python==4.11.0.86`  
- `cmake==3.31.4`  
- `dlib==19.24.6`  
- `numpy==2.0.2`  
- `cvzone==1.6.1`  
- `pickle`  
- `mysql-connector-python==2.2.9`  
- `os`  
- `datetime`

---

## Installation & Usage

Follow the steps below to set up and run FRAS on your local machine:

1. **Create a Folder in PyCharm**  
   Create a new project/folder where FRAS will reside.

2. **Add Project Files**  
   Download all FRAS Python files and add them to the created folder.

3. **Open and Configure PyCharm**  
   - Open the `FRAS-main-system.py` `FRAS-registeration.py` `fRAS-encoder`file in PyCharm.  
   - Install all required Python libraries listed in the requirements section.

4. **Set Up MySQL**  
   - Install MySQL Server and MySQL Workbench on your system.  
   - Remember the password you use for the database—it will be required later.

5. **Database Configuration**  
   - In `FRAS-main-system.py`, connect your Python script to MySQL using your MySQL Server credentials.

6. **Run the Attendance System**  
   - Execute `FRAS-main-system.py` to begin facial recognition attendance logging.

### Registration Script
To use the user registration feature:

1. Open the `FRAS_Registration.py` file.  
2. Connect it to the MySQL database as done in `FRAS-main-system.py`.  
3. Execute the script to register new users.

---

## Images

Below are some screenshots and visuals of FRAS in action:

![FRAS Main System](FRAS-Main-System.png)  
![FRAS Registration Page](Registration-Page.png)

---

## Recommended Image Guidelines for Facial Recognition

To ensure optimal performance and accuracy in facial recognition, follow these image guidelines when registering faces:

- ✅ Face should be centered and looking straight at the camera.  
- ✅ Capture images in well-lit environments.  
- ✅ Use high-resolution images with neutral or plain backgrounds.  
- ❌ Avoid:  
  - Masks or sunglasses  
  - Strong shadows or side lighting  
  - Side profiles or tilted faces  
  - Multiple people in the frame

**Recommended Image Formats**: `.jpg`, `.png`  
**Recommended Resolution**: At least 640x480 pixels

---

## 🛠️ Troubleshooting

- **Camera Not Found**: Ensure your webcam is properly connected and permissions are granted.  
- **Face Not Recognized**: Make sure face images meet the recommended guidelines.  
- **Database Error**: Check if MySQL service is running and credentials are correctly entered.  
- **Missing Libraries**: Run `pip install -r requirements.txt` to install all dependencies.

---

## 🙋‍♂️ Author & Acknowledgements

**Developed by:** Swetha Ganesh  
**University:** Teesside University  
**Special Thanks:**  
- Lecturers and mentors who provided project guidance  
- Open-source contributors of the `face_recognition`, `opencv-python`, and `dlib` libraries

---

## Important Notes

- **Update MySQL Password**: Replace the placeholder password in the scripts with your actual MySQL database password.  
- **Library Versions**: Ensure you're using the exact library versions specified to avoid compatibility issues.  
- **Environment Setup**: All installations and script executions should be done within the PyCharm IDE.

---
