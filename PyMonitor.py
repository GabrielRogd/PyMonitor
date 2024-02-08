import psutil
import tkinter as tk

def fetch_sys_info():
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq().current / 1000
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().total
    memory_remaining = psutil.virtual_memory().available
    memory_usage = psutil.virtual_memory().percent
    return f"CPU Count: {cpu_count}\nCPU Frequency: {cpu_freq:.2f} GHz\nCPU Usage: {cpu_usage}%\n\nMemory: {memory / 1024 / 1024 / 1024:.2f} GB\nMemory Usage: {memory_usage}%\nMemory Available: {memory_remaining / 1024 / 1024 / 1024:.2f} GB"

def info_label_update():
    info_label.config(text=fetch_sys_info())
    info_label.after(1000, info_label_update) # You can change the update interval here. (in milliseconds)

# GUI ipmlementation
root = tk.Tk()
root.title("PyMonitor")

info_label = tk.Label(root, text=fetch_sys_info(), font=("Arial", 12))
info_label.pack(padx=20, pady=20)

info_label_update()

root.mainloop()