import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

class DataForwarderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gaurav DuoGuard")

        # Login status for users
        self.junior_logged_in = False
        self.senior_logged_in = False
        self.data_count = 0

        # Create login frames for both users
        self.create_login_frame("Junior", "junior", "senior")
        self.create_login_frame("Senior", "senior", "admin")

        # Create data forwarding frame
        self.data_frame = tk.Frame(self.root)
        self.data_frame.pack(pady=20)

        self.forward_button = tk.Button(self.data_frame, text="Forward Data", command=self.forward_data)
        self.forward_button.pack(pady=10)

        # Scrollable text area for output logs
        self.log_text = scrolledtext.ScrolledText(self.root, height=10, width=60)
        self.log_text.pack(pady=10)

        # Save button to write log to file
        self.save_button = tk.Button(self.root, text="Save Log to File", command=self.save_log_to_file)
        self.save_button.pack(pady=10)
    
    def create_login_frame(self, user_role, username, password):
        """Creates login frames for users."""
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(pady=5)

        tk.Label(frame, text=f"{user_role} Login").grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="Username: ").grid(row=1, column=0)
        username_entry = tk.Entry(frame)
        username_entry.grid(row=1, column=1)

        tk.Label(frame, text="Password: ").grid(row=2, column=0)
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1)

        login_button = tk.Button(frame, text="Login", command=lambda: self.login(user_role, username, password, username_entry.get(), password_entry.get()))
        login_button.grid(row=3, column=0, pady=5)

        logout_button = tk.Button(frame, text="Logout", command=lambda: self.logout(user_role))
        logout_button.grid(row=3, column=1, pady=5)

    def login(self, user_role, valid_username, valid_password, entered_username, entered_password):
        """Handles login logic."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if entered_username == valid_username and entered_password == valid_password:
            if user_role == "Junior":
                self.junior_logged_in = True
            elif user_role == "Senior":
                self.senior_logged_in = True

            log_entry = f"{user_role} logged in successfully at {current_time}.\n"
            self.log_text.insert(tk.END, log_entry)
            messagebox.showinfo("Login Success", log_entry.strip())
            self.write_to_log_file(log_entry)
        else:
            messagebox.showerror("Login Failed", f"Incorrect credentials for {user_role}.")

    def logout(self, user_role):
        """Handles logout logic."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if user_role == "Junior" and self.junior_logged_in:
            self.junior_logged_in = False
            log_entry = f"{user_role} logged out at {current_time}.\n"
        elif user_role == "Senior" and self.senior_logged_in:
            self.senior_logged_in = False
            log_entry = f"{user_role} logged out at {current_time}.\n"
        else:
            log_entry = f"{user_role} attempted to log out but was not logged in at {current_time}.\n"

        self.log_text.insert(tk.END, log_entry)
        self.write_to_log_file(log_entry)
        messagebox.showinfo("Logout", log_entry.strip())

    def forward_data(self):
        """Handles data forwarding logic."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not self.junior_logged_in and not self.senior_logged_in:
            log_entry = f"Both users not logged in. Attempted to forward data at {current_time}.\n"
            self.log_text.insert(tk.END, log_entry)
            messagebox.showerror("Error", "Both users must be logged in to forward data.")
        elif not self.junior_logged_in:
            log_entry = f"senior tried to forward data at {current_time} without junior logged in.\n"
            self.log_text.insert(tk.END, log_entry)
            messagebox.showerror("Error", "Junior must be logged in to forward data.")
        elif not self.senior_logged_in:
            log_entry = f"junior tried to forward data at {current_time} without senior logged in.\n"
            self.log_text.insert(tk.END, log_entry)
            messagebox.showerror("Error", "Senior must be logged in to forward data.")
        else:
            self.data_count += 1
            log_entry = f"Data {self.data_count} forwarded successfully by both users at {current_time}.\n"
            self.log_text.insert(tk.END, log_entry)
            messagebox.showinfo("Success", f"Data {self.data_count} forwarded successfully.")
        
        self.write_to_log_file(log_entry)

    def write_to_log_file(self, log_entry):
        """Writes log entry to a text file."""
        with open("forward_log.txt", "a") as log_file:
            log_file.write(log_entry)

    def save_log_to_file(self):
        """Saves the log displayed on the GUI to a file."""
        with open("saved_output_log.txt", "w") as file:
            file.write(self.log_text.get("1.0", tk.END))
        messagebox.showinfo("Save Log", "The log has been saved to 'saved_output_log.txt'.")

# Create the main window
root = tk.Tk()
app = DataForwarderApp(root)
root.mainloop()
