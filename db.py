import sqlite3
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Function to display the menu
def display_menu():
    print("MENU:")
    print("1. Show database content")
    print("2. Export data to Excel")
    print("3. Export data to PDF")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

# Function to export data to Excel file in table format
def export_to_excel(data):
    df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
    df.to_excel('patients_data.xlsx', index=False)
    print("Data exported to patients_data.xlsx")

# Function to export data to PDF file in table format
def export_to_pdf(data):
    pdf_file = 'patients_data.pdf'
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    elements = []

    # Create a table from the data
    table_data = [tuple([desc[0] for desc in cursor.description])] + data
    table = Table(table_data)

    # Define table style
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    elements.append(table)

    # Build PDF document
    doc.build(elements)
    print("Data exported to patients_data.pdf")

# Connect to the database
conn = sqlite3.connect('patients.db')

# Create a cursor object to execute queries
cursor = conn.cursor()

try:
    while True:
        choice = display_menu()

        if choice == '1':
            # Execute a query to fetch data from the patients table
            cursor.execute('SELECT * FROM patients')
            # Fetch all rows from the table
            rows = cursor.fetchall()
            # Display the fetched data
            for row in rows:
                print(row)
        elif choice == '2':
            cursor.execute('SELECT * FROM patients')
            rows = cursor.fetchall()
            export_to_excel(rows)
        elif choice == '3':
            cursor.execute('SELECT * FROM patients')
            rows = cursor.fetchall()
            export_to_pdf(rows)
        elif choice == '4':
            break  # Exit the loop
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
    # Close the connection
    conn.close()
