import tkinter as tk
import asyncio
import python_weather

class Weather:
    def __init__(self, location: str) -> None:
        self.location = location
        
    
    async def weather_make(self):
        async with python_weather.Client() as client:
            weather = await client.get("halden")
            return weather

    async def temp_now(self):
        weather = await self.weather_make()
        weather.datetime
        return weather.temperature, weather.datetime
    
    

    async def feels_like_now(self):
        weather = await self.weather_make()
        return weather.feels_like
    
    async def forcast(self):
        weather = await self.weather_make()

class TK (tk.Tk):
    def __init__(self):
        self.weather = Weather("halden")
        super().__init__()
        self.geometry("400x400")
        self.title("hello world!")

class Frame1(tk.Frame):
    def __init__(self, parent_app, weather):
        super().__init__(parent_app)
        self.test = tk.StringVar(self, "asyncio.run(weather.temp_now())")
        self.parent = parent_app
        
    def button(self):
        self.test.set( self.test.get())
        
    def viewscreen_1(self):
        
        for c in self.winfo_children():
            for ch in c.winfo_children():
                # if isinstance(ch, tk.Button) or isinstance(ch, tk.Label):
                    print(ch)
                    ch.destroy()
            c.destroy()
        
        self.weather_text = tk.Label(self, textvariable=self.test)
        self.weather_text.pack(pady=(10,5)) # row=1,column=2
        
        self.but = tk.Button(self, command=self.button, text="helloworld")
        self.but.pack()
        
        print(self.winfo_children())
        self.pack(fill="x", expand=True)
        

class Frame2(tk.Frame):
    def __init__(self,parent_app, weather_frame):
        super().__init__(parent_app)
        self.which_viewscreen = tk.IntVar(self, 0)
        self.weather = weather_frame
        
    def make_buttons(self):
        tk.Radiobutton(self, text="tempratur nå", value=1, variable=self.which_viewscreen, indicatoron=False, bg="white",
                        command=lambda:(self.weather.viewscreen_1())).grid(row=2,column=1, padx=0, pady=(30,0  ))
        tk.Radiobutton(self, text="temp 3 dager", value=2, variable=self.which_viewscreen, indicatoron=False, bg="white").grid(row=2,column=2, padx=20, pady=(30,0))
        tk.Radiobutton(self, text="humidety", value=3, variable=self.which_viewscreen, indicatoron=False, bg="white").grid(row=2,column=3, padx=0, pady=(30,0))
        self.pack()

# weather = Weather("halden")
weather = 1
app = TK()
frame1 = Frame1(app, weather)
frame2 = Frame2(app, frame1)
frame2.make_buttons()
app.mainloop()