import time
import random
import pickle
import os
import tkinter as tk
from tkinter import messagebox

class TypingSpeedTest:
    def __init__(self):
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Programming is fun and challenging.",
            "Python is a versatile programming language.",
            "Practice makes perfect.",
            "Coding improves problem-solving skills."
        ]
        self.user_data_file = "user_data.pkl"
        self.users = self.load_users()
        self.user = self.register_user()
        self.session_start_time = 0
        self.session_end_time = 0
        self.session_score = 0

        self.window = tk.Tk()
        self.window.title("Typing Speed Test")
        self.window.geometry("400x300")

        self.start_button = tk.Button(self.window, text="Start Test", command=self.start_session)
        self.start_button.pack(pady=20)

        self.score_label = tk.Label(self.window, text="Your current score: 0")
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(self.window, text="")
        self.timer_label.pack(pady=10)

    def load_users(self):
        if os.path.exists(self.user_data_file):
            with open(self.user_data_file, "rb") as file:
                users = pickle.load(file)
            return users
        return {}

    def save_users(self):
        with open(self.user_data_file, "wb") as file:
            pickle.dump(self.users, file)

    def register_user(self):
        username = input("Welcome! Please enter your username: ")
        if username not in self.users:
            self.users[username] = {"total_score": 0, "sessions": 0}
            print(f"Welcome, {username}! You are now registered.")
        else:
            print(f"Welcome back, {username}!")

        return username

    def generate_random_sentence(self):
        return random.choice(self.sentences)

    def display_score(self):
        self.score_label.config(text=f"Your current score: {self.session_score}")

    def display_timer(self, remaining_time):
        self.timer_label.config(text=f"Time remaining: {remaining_time:.2f} seconds")

    def start_session(self):
        self.start_button.config(state=tk.DISABLED)
        self.session_score = 0
        self.display_score()

        self.session_start_time = time.time()
        self.display_timer(30)

        self.typing_entry = tk.Entry(self.window)
        self.typing_entry.pack(pady=20)
        self.typing_entry.focus_set()

        self.window.bind("<Return>", self.check_input)

        self.window.after(1000, self.update_timer)

    def end_session(self):
        self.session_end_time = time.time()
        session_duration = self.session_end_time - self.session_start_time

        messagebox.showinfo("Session Ended", f"Session ended!\nSession duration: {session_duration:.2f} seconds\nTotal score: {self.session_score} points")

        self.users[self.user]["total_score"] += self.session_score
        self.users[self.user]["sessions"] += 1
        self.save_users()

        self.start_button.config(state=tk.NORMAL)
        self.typing_entry.destroy()

    def update_timer(self):
        remaining_time = max(0, 30 - (time.time() - self.session_start_time))
        if remaining_time == 0:
            self.end_session()
        else:
            self.display_timer(remaining_time)
            self.window.after(1000, self.update_timer)

    def check_input(self, event):
        user_input = self.typing_entry.get()
        self.typing_entry.delete(0, tk.END)

        sentence = self.generate_random_sentence()

        if user_input.lower() == sentence.lower():
            time_taken = time.time() - self.session_start_time
            words_per_minute = (len(sentence.split()) / time_taken) * 60
            self.session_score += int(words_per_minute)
            self.display_score()
        else:
            messagebox.showwarning("Incorrect Typing", "Oops! Your typing didn't match the given sentence. Try again.")

if __name__ == "__main__":
    typing_test = TypingSpeedTest()
    typing_test.window.mainloop()