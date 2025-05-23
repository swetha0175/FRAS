# FRAS: Facial Recognition Attendance System

FRAS is an AI-powered Facial Recognition Attendance System that automates attendance tracking using internal or external webcams. It leverages facial recognition technology to identify and log user attendance seamlessly into a MySQL database.

---

## Table of Contents
- [Project Scope](#project-scope)  
- [Project Objectives](#project-objectives)  
- [Project Requirements](#project-requirements)  
  - [Hardware Requirements](#hardware-requirements)  
  - [Software Requirements](#software-requirements)  
  - [Python Library Requirements](#python-library-requirements)  
- [Installation & Usage](#installation--usage)  
- [Important Notes](#important-notes)

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
- Python 3.9
- PyCharm IDE
- MySQL Server & MySQL Workbench

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
   - Open the `FRAS_main.py` file in PyCharm.  
   - Install all required Python libraries listed in the requirements section.

4. **Set Up MySQL**  
   - Install MySQL Server and MySQL Workbench on your system.  
   - Remember the password you use for the database—it will be required later.

5. **Database Configuration**  
   - In `FRAS_main.py`, connect your Python script to MySQL using your credentials.

6. **Run the Attendance System**  
   - Execute `FRAS_main.py` to begin facial recognition attendance logging.

### Registration Script
To use the user registration feature:

1. Open the `FRAS_Registration.py` file.
2. Connect it to the MySQL database as done in `FRAS_main.py`.
3. Execute the script to register new users.

---

## Important Notes

- **Update MySQL Password**: Replace the placeholder password in the scripts with your actual MySQL database password.
- **Library Versions**: Ensure you're using the exact library versions specified to avoid compatibility issues.
- **Environment Setup**: All installations and script executions should be done within the PyCharm IDE.

---
