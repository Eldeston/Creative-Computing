# Imports graphical window
from tkinter import *
from tkinter import ttk as ttk

# Imports requests for getting API data
import requests

class MainAPI() :
    def __init__(self) :
        self.url = f"https://www.themealdb.com/api/json/v1/1"

        print(
f"""
The Meal DB : Free Recipe API
The API and site will always remain free at point of access.

URL: {self.url}
"""
        )
    
    def connectAPI(self, prompt) :
        # Announce connection
        print("Connecting to API...")
        response = requests.get(self.url + prompt)
    
        if response.status_code == 200 :
            print(f"Successfully retrieved data. Status code: {response.status_code}")
            return response.json()
        elif response.status_code == 404 :
            print(f"Invalid user input. Status code: {response.status_code}")
        else :
            print(f"Failed to retrieve data. Status code: {response.status_code}")
        
        return None

class Application(Tk) :
    def __init__(self) :
        # Call inherited init
        super().__init__()

        # Set window size
        self.geometry(f"360x360")
        # Sets the window's name/title
        self.title("MEALY DISPLAYINATOR 3000")

        # Font style
        self.font0 = ("Arial", 32, "bold")
        self.font1 = ("Arial", 16, "bold")
        # Creates a ttk style
        ttk.Style().configure("frame0.TFrame", background = "light gray")

        # Starts maximized
        self.after(1, self.wm_state, 'zoomed')
        # Start window
        self.displayMenu()

    def displayMenu(self) :
        # Clears initial frame
        self.clearFrame()

        # Main frame for container
        self.frame0 = ttk.Frame(self, style = "frame0.TFrame", padding = 32)
        self.frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

        # Layout by grid
        Label(self.frame0, text = "MEALY DISPLAYINATOR 3000", font = self.font0).grid(column = 0, row = 0)
        Label(self.frame0, text = "Developed by Eldeston", font = self.font1).grid(column = 0, row = 1)
        Button(self.frame0, text = "Press me", font = self.font1, command = lambda: self.displayMenu()).grid(column = 0, row = 2)
        Button(self.frame0, text = "Press me", font = self.font1, command = lambda: self.displayMenu()).grid(column = 0, row = 3)
    
    def clearFrame(self) :
        # Clears frame
        for widget in self.frame0.winfo_children() : widget.grid_forget()

# Debug API for connection
responseData = MainAPI().connectAPI("/search.php?s=Arrabiata")
responseString = ""

# Check for a response
try :
    # Display test results
    for key, value in responseData["meals"][0].items() :
        responseString += f"{key} : {value}\n"

    # Announce starting
    print(f"\n{responseString}\nStarting application...")

    # Begin application
    Application().mainloop()
except :
    # Announce closing
    print("\nClosing application...")