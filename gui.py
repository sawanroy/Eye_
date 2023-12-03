# gui.py
import tkinter as tk
from tkinter import messagebox
from register_window import RegisterPatient
from database_window import DatabaseWindow
from shared_functions import save_patient_to_database

class MainApplication:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.title("XYZ Optics")

        label = tk.Label(master, text="XYZ Optics", font=('Helvetica', 24, 'bold'))
        label.pack(pady=50)

        new_patient_button = tk.Button(master, text="New Patient", command=self.open_register_window, font=('Helvetica', 16))
        new_patient_button.pack(pady=20)

        database_button = tk.Button(master, text="Existing patient", command=self.open_database_window, font=('Helvetica', 16))
        database_button.pack(pady=20)

    def open_register_window(self):
        register_window = tk.Toplevel(self.master)
        RegisterPatient(register_window, self.submit_data, self.save_to_database)

    def open_database_window(self):
        DatabaseWindow(self.master)

    def submit_data(self, name, gender, dob, mobile):
        messagebox.showinfo("Submission Successful", "Patient data submitted successfully!")

    def save_to_database(self, name, gender, dob, mobile):
        save_patient_to_database(name, gender, dob, mobile)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
