import tkinter as tk
from tkinter import messagebox, filedialog
import mysql.connector
from mysql.connector import Error
import os
import shutil

# Database connection function
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Passwd',
            database='fras-db'
        )
        return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL Database: {e}")
        return None

# Function to register a student
def register_student():
    student_id = entry_student_id.get()
    student_name = entry_student_name.get()
    student_email = entry_student_email.get()
    student_number = entry_student_number.get()
    student_course = entry_student_course.get()
    student_image_path = entry_student_image_path.get()

    if not all([student_id, student_name, student_email, student_number, student_course, student_image_path]):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        # Read the image file as binary data
        with open(student_image_path, 'rb') as file:
            student_image_data = file.read()

        # Save the image to the FRAS_image folder
        fras_image_folder = "FRAS_image"
        if not os.path.exists(fras_image_folder):
            os.makedirs(fras_image_folder)
        image_filename = f"{student_id}.jpg"  # Use StudentID as the filename
        image_destination_path = os.path.join(fras_image_folder, image_filename)
        shutil.copy(student_image_path, image_destination_path)

        # Insert data into MySQL database
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            sql = """
            INSERT INTO fras_studentdb (StudentID, StudentName, StudentEmail, StudentNumber, StudentCourse, StudentImage_Path, StudentImage)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            val = (student_id, student_name, student_email, student_number, student_course, image_destination_path, student_image_data)
            cursor.execute(sql, val)
            connection.commit()
            messagebox.showinfo("Success", "Student registered successfully!")
    except Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to upload an image
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg;")])
    if file_path:
        entry_student_image_path.delete(0, tk.END)
        entry_student_image_path.insert(0, file_path)

# Function to change button color on hover
def on_enter(event):
    event.widget.config(bg="#6f50f8")  # Change to a darker green

def on_leave(event):
    event.widget.config(bg="#471ff6")  # Change back to the original green

# Create the main GUI window
root = tk.Tk()
root.title("FRAS Registration")
root.geometry("650x350")  # Set window size
root.configure(bg="#f0f0f0")  # Light gray background

# Custom Fonts
label_font = ("Times New Roman", 12)
entry_font = ("Times New Roman", 11)
button_font = ("Times New Roman", 12, "bold")

# Header Frame
header_frame = tk.Frame(root, pady=10)
header_frame.pack(fill="x")

tk.Label( text="Student Registration Form", font=("Times New Roman", 18, "bold"), fg="#471ff6",justify="left", pady=10).pack()

# Main Form Frame
form_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
form_frame.pack(fill="both", expand=True)

# Student ID and Student Name in one row
tk.Label(form_frame, text="Student ID", font=label_font, bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
entry_student_id = tk.Entry(form_frame, font=entry_font)
entry_student_id.grid(row=0, column=1, padx=10, pady=5, ipadx=10, ipady=5)

tk.Label(form_frame, text="Student Name", font=label_font, bg="#f0f0f0").grid(row=0, column=2, sticky="w", pady=5)
entry_student_name = tk.Entry(form_frame, font=entry_font)
entry_student_name.grid(row=0, column=3, padx=10, pady=5, ipadx=10, ipady=5)

# Student Email and Student Number in one row
tk.Label(form_frame, text="Student Email", font=label_font, bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
entry_student_email = tk.Entry(form_frame, font=entry_font)
entry_student_email.grid(row=1, column=1, padx=10, pady=5, ipadx=10, ipady=5)

tk.Label(form_frame, text="Student Number", font=label_font, bg="#f0f0f0").grid(row=1, column=2, sticky="w", pady=5)
entry_student_number = tk.Entry(form_frame, font=entry_font)
entry_student_number.grid(row=1, column=3, padx=10, pady=5, ipadx=10, ipady=5)

# Student Course in a separate row
tk.Label(form_frame, text="Student Course", font=label_font, bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
entry_student_course = tk.Entry(form_frame, font=entry_font)
entry_student_course.grid(row=2, column=1, columnspan=3, padx=10, pady=5, ipadx=10, ipady=5, sticky="ew")

# Student Image in a separate row
tk.Label(form_frame, text="Student Path & Image", font=label_font, bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
entry_student_image_path = tk.Entry(form_frame, font=entry_font)
entry_student_image_path.grid(row=3, column=1, columnspan=2, padx=10, pady=5, ipadx=10, ipady=5, sticky="ew")

upload_button = (tk.Button(form_frame, text="Upload Image", command=upload_image, font=button_font, bg="#471ff6", fg="white"))
upload_button.grid(row=3, column=3, padx=10, pady=5)

# Register Button
register_button = tk.Button(root, text="Register", command=register_student, font=button_font, bg="#471ff6", fg="white", padx=10, pady=5)
register_button.pack(pady=10)

# Bind hover events to the Register button
upload_button.bind("<Enter>", on_enter)
upload_button.bind("<Leave>", on_leave)

register_button.bind("<Enter>", on_enter)
register_button.bind("<Leave>", on_leave)
# Start the Tkinter event loop

root.mainloop()