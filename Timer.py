import tkinter as tk
from tkinter import messagebox
import time
import threading

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")

        self.time_left_var = tk.StringVar()
        self.time_left_var.set("00:00:00")

        self.label = tk.Label(root, text="Enter time in seconds:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=10, font=("Helvetica", 12))
        self.entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Helvetica", 12))
        self.start_button.pack(pady=5)

        self.time_display = tk.Label(root, textvariable=self.time_left_var, font=("Helvetica", 24))
        self.time_display.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, font=("Helvetica", 12))
        self.stop_button.pack(pady=5)

        self.running = False

    def start_timer(self):
        try:
            self.total_time = int(self.entry.get())
            self.running = True
            self.thread = threading.Thread(target=self.countdown)
            self.thread.start()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter an integer value.")

    def countdown(self):
        while self.total_time > 0 and self.running:
            mins, secs = divmod(self.total_time, 60)
            hours, mins = divmod(mins, 60)
            time_format = f"{hours:02d}:{mins:02d}:{secs:02d}"
            self.time_left_var.set(time_format)
            self.root.update()
            time.sleep(1)
            self.total_time -= 1

        if self.total_time == 0:
            messagebox.showinfo("Time's up", "Countdown has finished!")
            self.time_left_var.set("00:00:00")

    def stop_timer(self):
        self.running = False
        self.time_left_var.set("00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
