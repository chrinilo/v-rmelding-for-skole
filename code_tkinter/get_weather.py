import python_weather, asyncio
import time

class Weather:
    def __init__(self, location: str, time: int) -> None:
        self.location = location
        self.time = time
    
    async def weather_make(self):
        async with python_weather.Client() as client:
            weather = await client.get("halden")
            return weather
            
    


    
    async def temp_now(self):
        weather = await self.weather_make()
        return weather.temperature
    

    async def feels_like_now(self):
        weather = await self.weather_make()
        return weather.feels_like
        
    
weather = Weather("halden",2)
print(asyncio.run(weather.temp_now()))