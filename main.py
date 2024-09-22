import tkinter as tk
import customtkinter as ctk
from screens.login.login_gui import LoginFrame
from screens.dashboard.dashboard_gui import DashboardFrame
from screens.report.report_gui import ReportFrame
from screens.settings.settings_gui import SettingsFrame
from screens.add_user.add_user_gui import AddUserFrame

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Data Logger")

        # Maximize the window
        self.state('zoomed')

        # Display login screen
        self.login_frame = LoginFrame(self, self.show_main_content)
        self.login_frame.pack(fill=tk.BOTH, expand=True)

    def show_main_content(self):
        self.login_frame.pack_forget()

        # Use customtkinter notebook instead of ttk.Notebook
        self.notebook = ctk.CTkNotebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create and add tabs to the notebook
        self.dashboard_frame = DashboardFrame(self.notebook)
        self.report_frame = ReportFrame(self.notebook)
        self.settings_frame = SettingsFrame(self.notebook)
        self.add_user_frame = AddUserFrame(self.notebook)

        self.notebook.add(self.dashboard_frame, text="Dashboard")
        self.notebook.add(self.report_frame, text="Report")
        self.notebook.add(self.settings_frame, text="Settings")
        self.notebook.add(self.add_user_frame, text="Add User")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
