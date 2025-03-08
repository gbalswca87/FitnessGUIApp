import tkinter as tk
from tkinter import Toplevel, messagebox

# Stores user info like name, goal, and weekly activities
user_profile = {
    "name": "",
    "goal": "",
    "running_per_week": 0,
    "walking_per_week": 0,
    "swimming_per_week": 0,
}

# Converts miles to kilometers and updates the label
def miles_to_km():
    miles = miles_entry.get()
    if not miles.replace(".", "", 1).isdigit():  # make sure it's a number
        messagebox.showerror("Oops!", "Enter a valid number for miles.")
        return
    miles = float(miles)
    km = miles * 1.60934  # Simple conversion
    result_label.config(text=f"{miles} miles is {round(km, 2)} km")

# Converts kilometers to miles
def km_to_miles():
    km = km_entry.get()
    if not km.replace(".", "", 1).isdigit():  # again, make sure it's a number
        messagebox.showerror("Oops!", "Enter a valid number for kilometers.")
        return
    km = float(km)
    miles = km / 1.60934  # Simple conversion
    result_label.config(text=f"{km} km is {round(miles, 2)} miles")

# Opens the profile window where users enter their info
def open_profile_window():
    profile_window = Toplevel(window)
    profile_window.title("User Profile")
    profile_window.geometry("300x300")
    profile_window.config(bg="lightblue")
    
    # Labels and fields for user info
    name_label = tk.Label(profile_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(profile_window)
    name_entry.pack()
    
    goal_label = tk.Label(profile_window, text="Goal:")
    goal_label.pack()
    goal_entry = tk.Entry(profile_window)
    goal_entry.pack()
    
    running_label = tk.Label(profile_window, text="Running per week:")
    running_label.pack()
    running_entry = tk.Entry(profile_window)
    running_entry.pack()
    
    walking_label = tk.Label(profile_window, text="Walking per week:")
    walking_label.pack()
    walking_entry = tk.Entry(profile_window)
    walking_entry.pack()
    
    swimming_label = tk.Label(profile_window, text="Swimming per week:")
    swimming_label.pack()
    swimming_entry = tk.Entry(profile_window)
    swimming_entry.pack()
    
    # Saves user input, making sure it's valid
    def save_profile():
        if not running_entry.get().isdigit() or not walking_entry.get().isdigit() or not swimming_entry.get().isdigit():
            messagebox.showerror("Oops!", "Enter numbers only for activities.")
            return
        
        user_profile["name"] = name_entry.get()
        user_profile["goal"] = goal_entry.get()
        user_profile["running_per_week"] = int(running_entry.get())
        user_profile["walking_per_week"] = int(walking_entry.get())
        user_profile["swimming_per_week"] = int(swimming_entry.get())
        profile_window.destroy()
    
    save_button = tk.Button(profile_window, text="Save", command=save_profile)
    save_button.pack()

# Opens the progress window to show user stats
def open_progress_window():
    progress_window = Toplevel(window)
    progress_window.title("Fitness Progress")
    progress_window.geometry("300x200")
    progress_window.config(bg="lightyellow")
    
    progress_label = tk.Label(progress_window, text="Your Progress:")
    progress_label.pack()
    
    # Show how often the user does each activity
    running_label = tk.Label(progress_window, text=f"Running: {user_profile['running_per_week']} times/week")
    running_label.pack()
    
    walking_label = tk.Label(progress_window, text=f"Walking: {user_profile['walking_per_week']} times/week")
    walking_label.pack()
    
    swimming_label = tk.Label(progress_window, text=f"Swimming: {user_profile['swimming_per_week']} times/week")
    swimming_label.pack()
    
    back_button = tk.Button(progress_window, text="Back", command=progress_window.destroy)
    back_button.pack()

# Main window setup
window = tk.Tk()
window.title("Fitness App")
window.geometry("300x400")
window.config(bg="lightgreen")

# Input fields and buttons for conversions
miles_label = tk.Label(window, text="Miles:")
miles_label.pack()
miles_entry = tk.Entry(window)
miles_entry.pack()
miles_button = tk.Button(window, text="Convert to KM", command=miles_to_km)
miles_button.pack()

km_label = tk.Label(window, text="Kilometers:")
km_label.pack()
km_entry = tk.Entry(window)
km_entry.pack()
km_button = tk.Button(window, text="Convert to Miles", command=km_to_miles)
km_button.pack()

# Label to display results
result_label = tk.Label(window, text="")
result_label.pack()

# Buttons to open profile and progress windows
profile_button = tk.Button(window, text="Open Profile", command=open_profile_window)
profile_button.pack()

progress_button = tk.Button(window, text="View Progress", command=open_progress_window)
progress_button.pack()

# Start the app
window.mainloop()