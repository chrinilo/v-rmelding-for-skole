import tkinter as tk
import asyncio
import python_weather

class Weather:
    def __init__(self, location: str) -> None:
        self.location = location
        
    
    async def weather_make(self):
        async with python_weather.Client() as client:
            weather = await client.get(location=self.location)
            return weather

    async def temp_now(self):
        weather = await self.weather_make()
        weather.datetime
        return weather.temperature#, weather.datetime
    
    

    async def feels_like_now(self):
        weather = await self.weather_make()
        return weather.feels_like
    
    async def get_city(self):
        weather = await self.weather_make()
        return weather.location
        
    
    async def forcast(self):
        weather = await self.weather_make()
        temp_days = []
        for days in weather:
            temp_hours = []
            for hours in days:
                temp_hours.append(hours.temperature)
            temp_days.append(temp_hours)
            print(temp_days)
        return temp_days

class TK (tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("hello world!")

class Frame1(tk.Frame):
    def __init__(self, parent_app):
        super().__init__(parent_app)
        self._location = tk.StringVar(self, "halden")
        self.weather = Weather("oslo")
        self.parent = parent_app
        
        self.curent_viewscreen = int
    
    
    def delete_children(self) -> None:
        """
        deletets all lables and buttons on the screen.
        """
        for c in self.winfo_children():
            for ch in c.winfo_children():
                print(ch)
                ch.destroy()
            c.destroy()
    
    def city_textbox(self) -> None:
        """
        makes the textbox for which city you want to .
        """
        self.text_box_lable = tk.Label(self, text="by navn:")
        self.text_box_lable.grid(row=4, column=0)
        
        self.text_box = tk.Text(self, height=1, width=5)
        self.text_box.grid(row=4,column=1)
        
        self.text_box_button = tk.Button(self, text="søk", command=lambda:self.change_city())
        self.text_box_button.grid(row=4, column=2)
    
    def change_city(self) -> None:
        print(self.text_box.get('1.0',tk.END).replace('\n', ''))
        try:
            self.weather = Weather ( self.text_box.get ( '1.0',tk.END ).replace ( '\n', '' ) )
        except:
            self.weather = Weather ("oslo")
        finally:
            match self.curent_viewscreen:
                case 1:
                    self.viewscreen_1()
                    print('1')
                case 2:
                    self.viewscreen_2()
                    print('2')
                case 3:
                    self.viewscreen_3()


    def viewscreen_1(self) -> None:
        """
        loads everything for the temprature now button.
        """
        self.delete_children()
        get_temp_now = asyncio.run(self.weather.temp_now())
        self.weather_text = tk.Label(self, text=f"{get_temp_now}")
        self.weather_text.grid(row=1,column=0,padx=(200,0), pady=(10,5),columnspan=1) # 
        
        tk.Label(self, text=asyncio.run(self.weather.get_city())).grid(row=2, column=0)
        
        self.city_textbox()
        
        self.pack(fill="x", expand=True)
        self.curent_viewscreen = 1
        
    def viewscreen_2(self) -> None:
        """
        loads the curent forcast in three hour intervals.
        """
        self.delete_children()
        
        forcast = asyncio.run(self.weather.forcast())
        tk.Label(self, text="klokken:").grid(row=0, column=0)
        # prints tha lables for the forcast
        for i in range(len(forcast)):
            for j in range(len(forcast[i])):
                tk.Label(self, text=(j*3)).grid(row=i, column=j+1)
            tk.Label(self, text=f"dag: {(i+1)}").grid(row=i+1, column=0)
        # prints the forcast for the next three days
        for i in range(len(forcast)):
            for j in range(len(forcast[i])):
                tk.Label(self, text=f"{forcast[i][j]}").grid(row=i+1,column=j+1,padx=10, pady=(10,5),columnspan=1)
        # makes the textbox
        self.city_textbox()
        self.pack(fill="x", expand=True)
        self.curent_viewscreen = 2
    
    def viewscreen_3(self) -> None:
        self.delete_children()
        get_temp_now = asyncio.run(self.weather.feels_like_now())
        self.weather_text = tk.Label(self, text=f"feels like {get_temp_now}℃")
        self.weather_text.grid(row=1,column=0,padx=(200,0), pady=(10,5),columnspan=1) # 
        
        tk.Label(self, text=asyncio.run(self.weather.get_city())).grid(row=2, column=0)
        
        self.city_textbox()
        
        self.pack(fill="x", expand=True)
        self.curent_viewscreen = 3

class Frame2(tk.Frame):
    def __init__(self,parent_app, weather_frame):
        super().__init__(parent_app)
        self.which_viewscreen = tk.IntVar(self, 0) # not in use
        self.weather = weather_frame
        
    def make_buttons(self):
        """
        loads the buttons to change the viewscreen
        """
        

        tk.Radiobutton(self, text="tempratur nå", value=1, variable=self.which_viewscreen, indicatoron=False, bg="white",
                        command=lambda:(self.weather.viewscreen_1())).grid(row=2,column=1, padx=0, pady=(30,0  ))
        tk.Radiobutton(self, text="temp 3 dager", value=2, variable=self.which_viewscreen, indicatoron=False, bg="white",
                        command=lambda:(self.weather.viewscreen_2())).grid(row=2,column=2, padx=20, pady=(30,0))
        tk.Radiobutton(self, text="feels like", value=3, variable=self.which_viewscreen, indicatoron=False, bg="white",
                        command=lambda:(self.weather.viewscreen_3())).grid(row=2,column=3, padx=0, pady=(30,0))
        self.pack()

app = TK()
frame1 = Frame1(app)
frame2 = Frame2(app, frame1)
frame2.make_buttons()
app.mainloop()