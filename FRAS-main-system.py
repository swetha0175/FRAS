# this is the main FRAS System File
#---------------------------------------- Libraries Downloaded for FRAS ---------------------------------------
import pickle
import cvzone
import cv2
import os
import face_recognition
import numpy as np
import mysql.connector
import datetime

#--------------------------------------- Database - MySQL Credentials ---------------------------------------
# connecting the mysql server for the attendance db
mydb_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Passwd',
    database='fras_attendance'
)

# connecting the second mysql db called fras_student_db
fras_studentdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Passwd',
    database='fras-db'
)

print(mydb_connection.is_connected(),fras_studentdb.is_connected())# to check whether the mysql database are successfully connected

cursor = mydb_connection.cursor()  # defining attendance db
cursor2 = fras_studentdb.cursor()  # defining fras student db
timestamp = datetime.date.today().strftime("%d_%m_%Y")

cursor.execute(f"SHOW TABLES LIKE '{timestamp}'")
result = cursor.fetchone()
print("done")

if result is None:
    # create the table in MYSQL scheme fras_attendance to add table daily to record facial data
    cursor.execute(f""" CREATE TABLE {timestamp} (id INT AUTO_INCREMENT PRIMARY KEY,studentID VARCHAR(30) NOT NULL,time VARCHAR(30) NOT NULL)""")
    mydb_connection.commit()
    print(f"Table '{timestamp}' created successfully.")

cursor.close()

#----------------------------------- Code to open WebCam for face scanning ----------------------------------
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgbackground = cv2.imread('Resources/background.png')  # importing background of the FRAS

# importing the resources mode images used for user attendance verification
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModelLists = []
for path in modePathList:
    imgModelLists.append(cv2.imread(os.path.join(folderModePath, path)))

# -------------------------------------------- Encoding Images -----------------------------------------------
# load the pickle encoder file
print("Loading Encoded Files")
file = open('FinalEncodedFile.p', 'rb')
encodeListKnownWithIDs = pickle.load(file)
file.close()
encodeListKnown, studentIDs = encodeListKnownWithIDs
print("Encode File Loaded")

mode_counter = 0
modeType = 0 
cooldown_time = {}
cooldown_period = 30  # Cooldown period in seconds

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from webcam.")
        break

    # --------------------------------------- Reducing & Recognizing Images Given -------------------------------
    # scale the image down smaller
    imgsmall = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    imgsmall = cv2.cvtColor(imgsmall, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgsmall, model="cnn")  # feed in the value to the face reg system
    encodeCurFrame = face_recognition.face_encodings(imgsmall, faceCurFrame)

    # --------------------------------------- Background Co-ordination ------------------------------------------
    imgbackground[162:162 + 480, 55:55 + 640] = frame
    imgbackground[44:44 + 633, 808:808 + 414] = imgModelLists[modeType]  # --> display "Active" Page

    # ------------------------------------ Comparing Faces & Detection from Webcam ------------------------------
    if faceCurFrame:
        for encodeface, faceloc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeface, tolerance=0.5)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeface)
            #print("matches", matches)  # --> to test if the program can detect the correct face
            #print("distance", faceDis)  # --> to test if the program can detect the correct face

            matchindex = np.argmin(faceDis)

            if matches[matchindex]:
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                cvzone.cornerRect(imgbackground, bbox, rt=0)
                name = studentIDs[matchindex]
                position = (62 + x1, 162 + y1 - 15)
                cvzone.putTextRect(imgbackground, name, position, scale=1, thickness=2, colorR=(0, 255, 0),
                                   colorB=(255, 0, 0), offset=10)

                if mode_counter == 0:
                    # Check if the user is in cooldown
                    try:
                        cursor = mydb_connection.cursor()
                        cursor.execute(f"SELECT time FROM {timestamp} WHERE studentID = %s ORDER BY time DESC LIMIT 1", (name,))
                        result3 = cursor.fetchone()
                        if result3:
                            last_attendance_time_str = result3[0]
                            last_attendance_time = datetime.datetime.strptime(last_attendance_time_str, "%H:%M:%S")
                            current_time = datetime.datetime.now().strftime("%H:%M:%S")
                            current_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
                            secondsElapsed = (current_time - last_attendance_time).total_seconds()

                            if secondsElapsed < cooldown_period:
                                modeType = 3  # Already Marked
                                mode_counter = 3
                                continue
                    except mysql.connector.Error as e:
                        print("Error connection with MySQL", e)
                    finally:
                        if cursor:
                            cursor.close()

                    # If not in cooldown, proceed to Mode 1
                    modeType = 1 # user information interface
                    mode_counter = 1

                    # Fetch student information
                    sql2 = "SELECT StudentName, StudentCourse, StudentImage_Path, StudentImage FROM fras_studentdb WHERE StudentID = %s"
                    val2 = (name,)
                    cursor2.execute(sql2, val2)
                    result2 = cursor2.fetchone()

                    #this section of the code from line 150-176, does have an error, as the information are not properly displayed in mode 1 - user information
                    #however correct user information are still being retrieved, therefore I still left it in this code
                    #fras-main(result for interface mode 1).py file is also included in the artefact submission, to show how the mode 1
                    #actually should look like, as it successfully work in that .py file

                    if result2:
                        StudentName, StudentCourse, StudentImage_Path, StudentImage = result2
                        print(f"Fetched Student Info: {StudentName}, {StudentCourse}, {StudentImage_Path}")  # Debug statement

                        # Display student information only if modeType is 1
                        if mode_counter == 1:
                            # Display student name
                            (w, h), _ = cv2.getTextSize(StudentName, cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                            offset = (414 - w) // 2
                            cv2.putText(imgbackground, StudentName, (808 + offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1,
                                        (50, 50, 50), 1)

                            # Display student course
                            cv2.putText(imgbackground, StudentCourse, (985, 548), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                        (255, 255, 255), 1)

                            # Display student ID
                            cv2.putText(imgbackground, name, (1006, 490), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

                            # Display student image
                            if os.path.exists(StudentImage_Path):
                                StudentImage = cv2.imread(StudentImage_Path)
                                if StudentImage is not None:
                                    StudentImage_resize = cv2.resize(StudentImage, (216, 216))
                                    imgbackground[175:175 + 216, 909:909 + 216] = StudentImage_resize
                            else:
                                print(f"Image not found at path: {StudentImage_Path}")  # Debug statement

                    # Add data to MySQL DB
                    try:
                        cursor = mydb_connection.cursor()
                        current_time = datetime.datetime.now().strftime("%H:%M:%S")
                        cursor.execute(f"SELECT * FROM {timestamp} WHERE studentID = %s AND time >= %s",
                                       (name, current_time))
                        result = cursor.fetchone()
                        if not result:
                            sql = f"INSERT INTO {timestamp} (studentID, time) VALUES (%s, %s)"
                            val = (name, current_time)
                            cursor.execute(sql, val)
                            mydb_connection.commit()
                            print(f"Attendance Successfully Added for {name} at {current_time}")
                            cooldown_time[name] = datetime.datetime.now()
                    except mysql.connector.Error as e:
                        print("Error while importing data into MySQL:", e)
                    finally:
                        if cursor:
                            cursor.close()

                mode_counter += 1

                if mode_counter >= 10:
                    modeType = 2  # Marked
                    mode_counter = 0

    else:
        modeType = 0
        mode_counter = 0

    cv2.imshow("Face Attendance", imgbackground)
    key = cv2.waitKey(1)

    # to close the attendance webcam window when prompted
    if cv2.getWindowProperty("Face Attendance", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()