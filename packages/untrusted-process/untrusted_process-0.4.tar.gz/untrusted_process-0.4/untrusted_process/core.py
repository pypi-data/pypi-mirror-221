import subprocess
import json
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class UntrustedProcess:
    def __init__(self):
        self.osquery_path = None

    def setPath(self, osquery_path):
        self.osquery_path = osquery_path

    def run_osquery_command(self, commands):
        if not self.osquery_path:
            raise ValueError("osquery path not set. Use setPath() method to set the osquery path.")

        command_to_run = [self.osquery_path, '--json', commands]

        try:
            result = subprocess.run(command_to_run, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print("Command executed successfully.")
                data = json.loads(result.stdout)
                df = pd.DataFrame(data)
                df['trust_status'] = df['result'].apply(lambda x: 'trusted' if x == 'trusted' else 'untrusted')
                return df
            else:
                print("Error executing the command.")
                print("Error message:")
                print(result.stderr)
                return None
        except Exception as e:
            print("An error occurred:", e)
            return None

    def display_pie_chart_and_table(self, df):
        if df is not None:
            root = tk.Tk()
            root.title("Process Data Visualization")

            main_frame = tk.Frame(root)
            main_frame.pack()

            pie_frame = tk.Frame(main_frame)
            pie_frame.pack(side=tk.LEFT, padx=10)

            plt.figure(figsize=(8, 8))
            labels = df['trust_status'].value_counts().index.tolist()
            counts = df['trust_status'].value_counts().tolist()
            colors = ['salmon', 'lightgreen']
            plt.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.title('Distribution of Trusted and Untrusted Processes')

            canvas = FigureCanvasTkAgg(plt.gcf(), master=pie_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

            table_frame = tk.Frame(main_frame)
            table_frame.pack(side=tk.LEFT, padx=10)

            trusted_paths = df[df['trust_status'] == 'trusted']['path'].tolist()
            untrusted_paths = df[df['trust_status'] == 'untrusted']['path'].tolist()

            table = ttk.Treeview(table_frame, columns=('Trusted Path', 'Untrusted Path'), show='headings')
            table.heading('Trusted Path', text='Trusted Path')
            table.heading('Untrusted Path', text='Untrusted Path')

            for trusted, untrusted in zip(trusted_paths, untrusted_paths):
                table.insert('', 'end', values=(trusted, untrusted))

            table.pack()

            root.mainloop()
    def ShowResults(self):
        
        untrust = UntrustedProcess()
        untrust.setPath(self.osquery_path)
        df = untrust.run_osquery_command('SELECT process.pid, process.path, signature.issuer_name, signature.subject_name, signature.result FROM processes as process LEFT JOIN authenticode AS signature ON process.path = signature.path;')
        untrust.display_pie_chart_and_table(df)