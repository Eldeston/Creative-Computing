import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests, json, os
from io import BytesIO

API_BASE = "https://www.themealdb.com/api/json/v1/1/"
FAV_FILE = "favorites.json"

# -------------------------------------------------------------
# API Wrapper Class
# -------------------------------------------------------------
class MealAPI:
    @staticmethod
    def _get(url):
        try:
            r = requests.get(url)
            return r.json()
        except:
            return None

    @staticmethod
    def search(name):
        return MealAPI._get(f"{API_BASE}search.php?s={name}")

    @staticmethod
    def lookup(meal_id):
        return MealAPI._get(f"{API_BASE}lookup.php?i={meal_id}")

    @staticmethod
    def random():
        return MealAPI._get(f"{API_BASE}random.php")

# -------------------------------------------------------------
# Main Application Class
# -------------------------------------------------------------
class MealApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MealDB Recipe Explorer - Enhanced Edition")
        self.geometry("1100x700")
        self.minsize(1000, 650)

        self.current_theme = "light"
        self.meal_images = {}

        self.themes = {
            "light": {"bg": "#f5f6fa", "fg": "#2c3e50", "accent": "#3498db", "card": "#ffffff"},
            "dark": {"bg": "#1e1e1e", "fg": "#ffffff", "accent": "#7289da", "card": "#2c2c2c"},
            "netflix": {"bg": "#141414", "fg": "#e50914", "accent": "#e50914", "card": "#1f1f1f"},
            "minimal": {"bg": "#ffffff", "fg": "#000000", "accent": "#555555", "card": "#ffffff"}
        }

        self.apply_theme()
        self.build_layout()

    # ---------------------------------------------------------
    # THEME HANDLING
    # ---------------------------------------------------------
    def apply_theme(self):
        theme = self.themes[self.current_theme]
        self.configure(bg=theme["bg"])

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TLabel", background=theme["bg"], foreground=theme["fg"], font=("Segoe UI", 11))
        style.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"),
                        background=theme["accent"], foreground="white")
        style.map("TButton", background=[("active", theme["accent"])])

    # ---------------------------------------------------------
    # BUILD UI LAYOUT
    # ---------------------------------------------------------
    def build_layout(self):
        theme = self.themes[self.current_theme]

        # Gradient Header
        header = tk.Canvas(self, height=80, bd=0, highlightthickness=0)
        header.pack(fill="x")
        for i in range(80):
            color = f"#{int(20+i*2):02x}{int(80+i):02x}{int(150+i):02x}"
            header.create_line(0, i, 2000, i, fill=color)
        header.create_text(550, 40, text="🍽️ MealDB Recipe Explorer", fill="white", font=("Segoe UI", 26, "bold"))

        # Sidebar
        sidebar = tk.Frame(self, width=200, bg=theme["card"], highlightbackground=theme["accent"], highlightthickness=1)
        sidebar.pack(side="left", fill="y")

        ttk.Button(sidebar, text="Search Meals", command=self.show_search).pack(fill="x", pady=10)
        ttk.Button(sidebar, text="Random Meal", command=self.show_random).pack(fill="x", pady=10)
        ttk.Button(sidebar, text="Favorites", command=self.show_favorites).pack(fill="x", pady=10)
        

        # Main Content
        self.content = tk.Frame(self, bg=theme["bg"])
        self.content.pack(side="right", fill="both", expand=True)

        self.show_search()

    # ---------------------------------------------------------
    # PAGES
    # ---------------------------------------------------------
    def clear(self):
        for w in self.content.winfo_children():
            w.destroy()

    def show_search(self):
        self.clear()

        theme = self.themes[self.current_theme]

        frame = tk.Frame(self.content, bg=theme["bg"])
        frame.pack(pady=20)

        tk.Label(frame, text="Search Meal", font=("Segoe UI", 16, "bold"), bg=theme["bg"], fg=theme["fg"]).pack()

        search_entry = tk.Entry(frame, width=40, font=("Segoe UI", 12), relief="flat", bd=4)
        search_entry.pack(pady=10)

        ttk.Button(frame, text="Search", command=lambda: self.perform_search(search_entry.get())).pack()

    def perform_search(self, query):
        data = MealAPI.search(query)
        if not data or not data["meals"]:
            messagebox.showinfo("No Results", "No meals found.")
            return

        self.show_results(data["meals"])

    def show_results(self, meals):
        self.clear()

        theme = self.themes[self.current_theme]

        wrapper = tk.Frame(self.content, bg=theme["bg"])
        wrapper.pack(fill="both", expand=True)

        for meal in meals:
            card = tk.Frame(wrapper, bg=theme["card"], bd=1, relief="ridge")
            card.pack(pady=10, padx=20, fill="x")

            tk.Label(card, text=meal["strMeal"], font=("Segoe UI", 14, "bold"), bg=theme["card"], fg=theme["fg"]).pack(anchor="w", padx=10, pady=5)

            ttk.Button(card, text="View", command=lambda m=meal: self.show_meal(m)).pack(anchor="e", padx=10, pady=5)

    def show_meal(self, meal):
        self.clear()
        theme = self.themes[self.current_theme]

        frame = tk.Frame(self.content, bg=theme["bg"])
        frame.pack(fill="both", expand=True, padx=20)

        # Load image
        img_url = meal["strMealThumb"]
        img_data = requests.get(img_url).content
        image = Image.open(BytesIO(img_data)).resize((300, 300))
        img_tk = ImageTk.PhotoImage(image)
        self.meal_images[meal["idMeal"]] = img_tk

        tk.Label(frame, image=img_tk, bg=theme["bg"]).pack(pady=10)
        tk.Label(frame, text=meal["strMeal"], font=("Segoe UI", 18, "bold"), bg=theme["bg"], fg=theme["fg"]).pack()

        # Collapsible Sections
        self.add_collapse(frame, "Ingredients", self.get_ingredients(meal))
        self.add_collapse(frame, "Instructions", meal["strInstructions"])

        ttk.Button(frame, text="Add to Favorites", command=lambda: self.add_favorite(meal)).pack(pady=10)

    def get_ingredients(self, meal):
        items = []
        for i in range(1, 21):
            ing = meal.get(f"strIngredient{i}")
            meas = meal.get(f"strMeasure{i}")
            if ing and ing.strip():
                items.append(f"• {ing} - {meas}")
        return "\n".join(items)

    # Collapsible Panel Helper
    def add_collapse(self, parent, title, content):
        frame = tk.Frame(parent)
        frame.pack(fill="x", pady=6)
       
        btn = ttk.Button(frame, text=f"▼ {title}", width=30)
        btn.pack(anchor="w")
        
        text = tk.Label(frame, text=content, wraplength=800, justify="left")

        def toggle():
            if text.winfo_ismapped():
                text.pack_forget()
                btn.config(text=f"▶ {title}")
            else:
                text.pack(anchor="w", padx=20)
                btn.config(text=f"▼ {title}")

        btn.config(command=toggle)

    # ---------------------------------------------------------
    # RANDOM
    # ---------------------------------------------------------
    def show_random(self):
        data = MealAPI.random()
        self.show_meal(data["meals"][0])

    # ---------------------------------------------------------
    # FAVORITES
    # ---------------------------------------------------------
    def add_favorite(self, meal):
        try:
            if os.path.exists(FAV_FILE):
                favs = json.load(open(FAV_FILE))
            else:
                favs = []
            
            if meal["idMeal"] not in [m["idMeal"] for m in favs]:
                favs.append(meal)
                json.dump(favs, open(FAV_FILE, "w"), indent=4)
                messagebox.showinfo("Added", "Saved to favorites")
        except:
            messagebox.showerror("Error", "Could not save favorite")

    def show_favorites(self):
        self.clear()

        theme = self.themes[self.current_theme]

        if not os.path.exists(FAV_FILE):
            tk.Label(self.content, text="No Favorites Yet", font=("Segoe UI", 16)).pack()
            return

        favs = json.load(open(FAV_FILE))

        for meal in favs:
            card = tk.Frame(self.content, bg=theme["card"], bd=1, relief="ridge")
            card.pack(pady=10, padx=20, fill="x")

            tk.Label(card, text=meal["strMeal"], font=("Segoe UI", 14, "bold"), bg=theme["card"]).pack(anchor="w", padx=10, pady=5)
            ttk.Button(card, text="View", command=lambda m=meal: self.show_meal(m)).pack(anchor="e", padx=10, pady=5)

    # ---------------------------------------------------------
    # THEME SWITCHER
    # ---------------------------------------------------------
    # (Theme switching removed)


# -------------------------------------------------------------
# RUN APP
# -------------------------------------------------------------
if __name__ == "__main__":
    MealApp().mainloop()