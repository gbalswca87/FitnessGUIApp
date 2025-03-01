import tkinter as tk
from tkinter import Toplevel

# This stores the user's profile information
user_profile = {
    "name": "",
    "goal": "",
    "running_per_week": 0,
    "walking_per_week": 0,
    "swimming_per_week": 0,  # We're tracking swimming instead of cycling now
}

# Function to convert miles to kilometers
def miles_to_km():
    miles = float(miles_entry.get())  # Get the miles input from the user
    km = miles * 1.60934  # Conversion factor for miles to km
    result_label.config(text=str(miles) + " miles is " + str(round(km, 2)) + " km")  # Show the result

# converts kilometers to miles
def km_to_miles():
    km = float(km_entry.get())  # Get the km input from the user
    miles = km / 1.60934  # Conversion factor for km to miles
    result_label.config(text=str(km) + " km is " + str(round(miles, 2)) + " miles")  # Show the result

# This function opens the user profile screen
def open_profile_window():
    profile_window = Toplevel(window)  # Create a new window for the profile
    profile_window.title("User Profile")  # Set the title of the window
    profile_window.geometry("300x300")  # Set the size of the window
    profile_window.config(bg="lightblue")  # Set the background color of the window

    # Add a text box for the user to input their name
    name_label = tk.Label(profile_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(profile_window)
    name_entry.pack()

    # Add a text box for the user to input their goal
    goal_label = tk.Label(profile_window, text="Goal:")
    goal_label.pack()
    goal_entry = tk.Entry(profile_window)
    goal_entry.pack()

    # Add a text box for the user to input how many times they run each week
    running_label = tk.Label(profile_window, text="Running per week:")
    running_label.pack()
    running_entry = tk.Entry(profile_window)
    running_entry.pack()

    # Add a text box for walking frequency per week
    walking_label = tk.Label(profile_window, text="Walking per week:")
    walking_label.pack()
    walking_entry = tk.Entry(profile_window)
    walking_entry.pack()

    # Add a text box for swimming frequency per week (instead of cycling now)
    swimming_label = tk.Label(profile_window, text="Swimming per week:")
    swimming_label.pack()
    swimming_entry = tk.Entry(profile_window)
    swimming_entry.pack()

    # This function saves the profile data when the user clicks save
    def save_profile():
        user_profile["name"] = name_entry.get()  # Save the name
        user_profile["goal"] = goal_entry.get()  # Save the goal
        user_profile["running_per_week"] = int(running_entry.get() or 0)  # Save running data
        user_profile["walking_per_week"] = int(walking_entry.get() or 0)  # Save walking data
        user_profile["swimming_per_week"] = int(swimming_entry.get() or 0)  # Save swimming data
        profile_window.destroy()  # Close the profile window after saving

    # Button to save the profile data
    save_button = tk.Button(profile_window, text="Save", command=save_profile)
    save_button.pack()

# This function shows the user's progress in another window
def open_progress_window():
    progress_window = Toplevel(window)  # Create a new window to display progress
    progress_window.title("Fitness Progress")  # Set the title of the window
    progress_window.geometry("300x200")  # Set the window size
    progress_window.config(bg="lightyellow")  # Set the background color

    # Label that says "Your Progress"
    progress_label = tk.Label(progress_window, text="Your Progress:")
    progress_label.pack()

    # Display how many times the user runs per week
    running_label = tk.Label(progress_window, text="Running: " + str(user_profile["running_per_week"]) + " times/week")
    running_label.pack()

    # Display how many times the user walks per week
    walking_label = tk.Label(progress_window, text="Walking: " + str(user_profile["walking_per_week"]) + " times/week")
    walking_label.pack()

    # Display how many times the user swims per week
    swimming_label = tk.Label(progress_window, text="Swimming: " + str(user_profile["swimming_per_week"]) + " times/week")
    swimming_label.pack()

    # Button to go back to the main window
    back_button = tk.Button(progress_window, text="Back", command=progress_window.destroy)
    back_button.pack()

# Main window where the user interacts with the app
window = tk.Tk()
window.title("Fitness App")  # Title of the main window
window.geometry("300x400")  # Size of the window
window.config(bg="lightgreen")  # Background color

# Label and input box for miles
miles_label = tk.Label(window, text="Miles:")
miles_label.pack()
miles_entry = tk.Entry(window)
miles_entry.pack()
miles_button = tk.Button(window, text="Convert to KM", command=miles_to_km)  # Convert miles to km
miles_button.pack()

# Label and input box for kilometers
km_label = tk.Label(window, text="Kilometers:")
km_label.pack()
km_entry = tk.Entry(window)
km_entry.pack()
km_button = tk.Button(window, text="Convert to Miles", command=km_to_miles)  # Convert kilometers to miles
km_button.pack()

# Label to show the conversion result
result_label = tk.Label(window, text="")
result_label.pack()

# Button to open the user profile window
profile_button = tk.Button(window, text="Open Profile", command=open_profile_window)
profile_button.pack()

# Button to view the progress of the user
progress_button = tk.Button(window, text="View Progress", command=open_progress_window)
progress_button.pack()

# Start the Tkinter main loop to run the app
window.mainloop()
