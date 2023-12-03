# database_window.py
import tkinter as tk
from tkinter import ttk
from shared_functions import open_patient_detail_window, export_to_excel, search_patients

class DatabaseWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("800x600")
        self.title("Database")

        self.search_label = tk.Label(self, text="Search:")
        self.search_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.search_button = tk.Button(self, text="Search", command=self.perform_search)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

        columns = ("ID", "Name", "Gender", "Date of Birth", "Mobile Number")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.tree.bind("<Double-1>", self.open_selected_patient_detail)

        self.excel_button = tk.Button(self, text="Export to Excel", command=self.export_to_excel)
        self.excel_button.grid(row=2, column=0, columnspan=3, pady=20)

    def perform_search(self):
        query = self.search_entry.get()
        results = search_patients(query)
        self.display_patients(results)

    def display_patients(self, results):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for result in results:
            self.tree.insert("", "end", values=result)

    def open_selected_patient_detail(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            patient_id = self.tree.item(selected_item, "values")[0]
            open_patient_detail_window(patient_id)

    def export_to_excel(self):
        export_to_excel()

if __name__ == "__main__":
    app = DatabaseWindow()
    app.mainloop()
