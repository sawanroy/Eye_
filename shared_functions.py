# shared_functions.py
import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd

# SQLite database initialization
conn = sqlite3.connect('patients.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        gender TEXT,
        dob TEXT,
        mobile TEXT
    )
''')
conn.commit()

def search_patients(query):
    cursor.execute('''
        SELECT id, name, gender, dob, mobile
        FROM patients
        WHERE name LIKE ? OR dob LIKE ? OR mobile LIKE ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%'))

    return cursor.fetchall()

def open_patient_detail_window(patient_id):
    messagebox.showinfo("Patient Detail", f"Opening Patient Detail Window for Patient ID: {patient_id}")

def save_patient_to_database(name, gender, dob, mobile):
    cursor.execute('''
        INSERT INTO patients (name, gender, dob, mobile)
        VALUES (?, ?, ?, ?)
    ''', (name, gender, dob, mobile))
    conn.commit()

def export_to_excel():
    cursor.execute('''
        SELECT id, name, gender, dob, mobile
        FROM patients
    ''')
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=["ID", "Name", "Gender", "Date of Birth", "Mobile Number"])

    excel_file_path = 'patients_data.xlsx'
    df.to_excel(excel_file_path, index=False)

    messagebox.showinfo("Export Successful", f"Data exported to {excel_file_path}")
