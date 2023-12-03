# register_window.py
import tkinter as tk
from tkinter import messagebox
from shared_functions import save_patient_to_database

class RegisterPatient:
    def __init__(self, master, submit_callback, save_to_database):
        self.master = master
        self.submit_callback = submit_callback  # Save the callback
        self.save_to_database = save_to_database  # Save the database-saving callback

        master.geometry("400x300")
        master.title("Register Patient")

        name_label = tk.Label(master, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        gender_label = tk.Label(master, text="Gender:")
        gender_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.gender_entry = tk.Entry(master, width=30)
        self.gender_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        dob_label = tk.Label(master, text="Date of Birth:")
        dob_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.dob_entry = tk.Entry(master, width=30)
        self.dob_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        mobile_label = tk.Label(master, text="Mobile Number:")
        mobile_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.mobile_entry = tk.Entry(master, width=30)
        self.mobile_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        submit_button = tk.Button(master, text="Submit", command=self.submit_data)
        submit_button.grid(row=4, column=0, columnspan=2, pady=20)

    def submit_data(self):
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        dob = self.dob_entry.get()
        mobile = self.mobile_entry.get()

        # Call the callback function from the main application
        self.submit_callback(name, gender, dob, mobile)

        # Save the data to the database
        self.save_to_database(name, gender, dob, mobile)

        # Close the register window after submission
        self.master.destroy()
