# duoguard
segregation of duties
Gaurav DuoGuard
Overview
Gaurav DuoGuard is a Python-based tool that implements the concept of Segregation of Duties in data forwarding processes. It requires two users to authenticate and approve actions, ensuring enhanced security and accountability.

Features
User Authentication: Requires both Junior and Senior users to log in to initiate data forwarding.
Data Forwarding: Only allows data to be forwarded when both users are authenticated.
Error Handling: Displays error messages if either user tries to forward data without being logged in.
Real-time Logging: Logs all actions, including login attempts, successful data forwarding, and errors, in a scrollable text area.
File Logging: Saves logs to a text file for future reference.
Sign-Out Option: Allows users to log out, affecting the ability to forward data.
Technologies Used
Python: Programming language used to build the application.
Tkinter: Library used for creating the graphical user interface (GUI).
Datetime: Library used to manage timestamps for logging actions.
Installation
Ensure you have Python installed on your system. You can download it from python.org.

The GUI will open, allowing both users to log in with their respective credentials:
Junior: Username - junior, Password - senior
Senior: Username - senior, Password - admin
Once both users are logged in, they can forward data.
All actions will be logged in the GUI and saved to a text file called forward_log.txt.
Contribution
Feel free to contribute to this project by forking the repository and submitting a pull request.

License
This project is licensed under the MIT License.

Contact
For any inquiries or feedback, please reach out to me on LinkedIn: Your LinkedIn Profile.
