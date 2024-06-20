import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from data_loader import DataLoader
from visualizer import Visualizer

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Analysis Application")
        self.root.geometry("600x400")
        self.data = None

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        self.load_button.pack()

        self.display_columns_button = tk.Button(self.root, text="Display Columns", command=self.display_columns)
        self.display_columns_button.pack()

        self.display_button = tk.Button(self.root, text="Display Data", command=self.display_data)
        self.display_button.pack()

        self.plot_label = tk.Label(self.root, text="Plot Type (count/scatter/histogram/box):")
        self.plot_label.pack()
        self.plot_type = ttk.Combobox(self.root, values=['count', 'scatter', 'histogram', 'box'])
        self.plot_type.pack()
        self.plot_column_label = tk.Label(self.root, text="Plot Column:")
        self.plot_column_label.pack()
        self.plot_column = ttk.Combobox(self.root)
        self.plot_column.pack()
        self.plot_x_column_label = tk.Label(self.root, text="X-Axis Column (for scatter):")
        self.plot_x_column_label.pack()
        self.plot_x_column = ttk.Combobox(self.root)
        self.plot_x_column.pack()
        self.plot_y_column_label = tk.Label(self.root, text="Y-Axis Column (for scatter):")
        self.plot_y_column_label.pack()
        self.plot_y_column = ttk.Combobox(self.root)
        self.plot_y_column.pack()
        self.plot_button = tk.Button(self.root, text="Plot Data", command=self.plot_data)
        self.plot_button.pack()

    def run(self):
        self.root.mainloop()

    def load_data(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.data = DataLoader.load_data(file_path)
            if self.data is not None:
                self.update_comboboxes()
                messagebox.showinfo("Info", "Data loaded successfully.")
            else:
                messagebox.showerror("Error", "Failed to load data.")
        else:
            messagebox.showerror("Error", "No file selected.")

    def display_columns(self):
        if self.data is not None:
            columns = self.data.columns.tolist()
            messagebox.showinfo("Columns", f"Available columns: {', '.join(columns)}")
        else:
            messagebox.showerror("Error", "No data loaded.")

    def display_data(self):
        if self.data is not None:
            top = tk.Toplevel(self.root)
            top.title("Data Display")
            frame = tk.Frame(top)
            frame.pack(fill=tk.BOTH, expand=1)
            canvas = tk.Canvas(frame)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            data_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=data_frame, anchor="nw")

            for i, col in enumerate(self.data.columns):
                label = tk.Label(data_frame, text=col, borderwidth=1, relief="solid")
                label.grid(row=0, column=i, sticky="nsew")

            for i, row in self.data.iterrows():
                for j, value in enumerate(row):
                    label = tk.Label(data_frame, text=value, borderwidth=1, relief="solid")
                    label.grid(row=i + 1, column=j, sticky="nsew")

            for i in range(len(self.data.columns)):
                data_frame.grid_columnconfigure(i, weight=1)

        else:
            messagebox.showerror("Error", "No data loaded.")

    def plot_data(self):
        if self.data is not None:
            plot_type = self.plot_type.get()
            if plot_type:
                try:
                    if plot_type == 'count':
                        column = self.plot_column.get()
                        if column:
                            Visualizer.plot_count(self.data, column)
                        else:
                            messagebox.showerror("Error", "Plot column must be selected for count plot.")
                    elif plot_type == 'scatter':
                        x_column = self.plot_x_column.get()
                        y_column = self.plot_y_column.get()
                        if x_column and y_column:
                            Visualizer.plot_scatter(self.data, x_column, y_column)
                        else:
                            messagebox.showerror("Error", "Both X and Y columns must be selected for scatter plot.")
                    elif plot_type == 'histogram':
                        column = self.plot_column.get()
                        if column:
                            Visualizer.plot_histogram(self.data, column)
                        else:
                            messagebox.showerror("Error", "Plot column must be selected for histogram.")
                    elif plot_type == 'box':
                        column = self.plot_column.get()
                        if column:
                            Visualizer.plot_box(self.data, column)
                        else:
                            messagebox.showerror("Error", "Plot column must be selected for box plot.")
                    else:
                        messagebox.showerror("Error", "Invalid plot type.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to generate plot: {str(e)}")
            else:
                messagebox.showerror("Error", "Plot type must be selected.")
        else:
            messagebox.showerror("Error", "No data loaded.")

    def update_comboboxes(self):
        columns = self.data.columns.tolist()
        self.plot_column['values'] = columns
        self.plot_x_column['values'] = columns
        self.plot_y_column['values'] = columns
