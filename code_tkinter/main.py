import tkinter as tk
import asyncio
import python_weather

async def get_weather():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        return client.get('halden')

class TK (tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("hello world!")

class frame1(tk.Frame):
    def __init__(self, parent_app):
        super().__init__(parent_app)
        self.weather_text = tk.Text()
        self.weather_text.insert(1.0, "hello world")
        self.weather_text.grid(row=1,column=2, padx=200)
        self.grid(row=1, column=1)
    
    


app = TK()
frame = frame1(app)
app.mainloop()