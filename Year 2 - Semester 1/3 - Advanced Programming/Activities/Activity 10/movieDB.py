# Imports graphical window
from tkinter import *
from tkinter import ttk as ttk

# Imports requests for getting API data
import requests

# -------------------------------- Main Application -------------------------------- #

class Application :
    def __init__(self, mainFrame):
        self.mainFrame = mainFrame
    
    def clearFrame(self) :
        for widget in self.mainFrame.winfo_children() : widget.grid_forget()

    def getWeather(self, label, entry) :
        location = entry.get()
        key = "c2818a5a2fd26aa5fa49daea5a13a59e"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}&units=metric"

        response = requests.get(url)

        if response.status_code == 200 :
            weather = response.json()

            textContent = f"""Successfully retrieved data. Status code: {response.status_code}

Entry: {location}
Location : {weather["name"]}
Temp : {weather["main"]["temp"]}
Pressure : {weather["main"]["pressure"]}
Humidity : {weather["main"]["humidity"]}
Sea Level : {weather["main"]["sea_level"]}
Ground Level : {weather["main"]["grnd_level"]}"""

            label.config(text = textContent)
        elif response.status_code == 404 :
            label.config(text = f"Invalid user input. Status code: {response.status_code}")
        else :
            label.config(text = f"Failed to retrieve data. Status code: {response.status_code}")

    def displayMenu(self) :
        # Clear display first
        self.clearFrame()

        # Display stats
        Label(self.mainFrame, text = "Stats", font = ("Arial", 32, "bold"), bg = "light gray").grid(column = 0, row = 3, columnspan = 2, sticky = "W")
        label0 = Label(self.mainFrame, text = "N/A", font = ("Arial", 16, "bold"), bg = "light gray")
        label0.grid(column = 0, row = 4, columnspan = 2, sticky = "W")

        # Control menu
        Label(self.mainFrame, text = "Weather Display", font = ("Arial", 32, "bold"), bg = "light gray").grid(column = 0, row = 0, columnspan = 2, sticky = "W")
        Label(self.mainFrame, text = "Enter Location:", font = ("Arial", 16, "bold"), bg = "light gray").grid(column = 0, row = 1, sticky = "W")
        entry0 = Entry(self.mainFrame, font = ("Arial", 16, "bold"))
        entry0.grid(column = 1, row = 1, columnspan = 2, sticky = "W")
        Button(self.mainFrame, text = "View Location Weather", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: self.getWeather(label0, entry0)).grid(column = 0, row = 2, columnspan = 3, sticky = "EW")

# -------------------------------- Main Window -------------------------------- #

# Initializes a main TKinter window
mainWindow = Tk()
# Sets the window's name/title
mainWindow.title("Weather App")
# Set window size
mainWindow.geometry(f"360x360")
# Starts maximized
mainWindow.after(1, mainWindow.wm_state, 'zoomed')

# -------------------------------- Main Frame -------------------------------- #

ttk.Style().configure("frame0.TFrame", background = "light gray")
frame0 = ttk.Frame(mainWindow, style = "frame0.TFrame", padding = 32)
# Initial frame to contain all the elements
frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

# Create object
app = Application(frame0)

# Display
app.displayMenu()

# -------------------------------- Main Loop -------------------------------- #

# Required at the end
mainWindow.mainloop()