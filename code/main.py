"""
    pygame er biblioteket som vi bruker for å lage hele programmet
    python weather kommer til å bli brukt 
"""
import pygame

from event_handel import eventhandel

window = pygame.display.set_mode((400,400))

class Main_handel:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((400,400))
        self.running= True # om main loopen skal kjøre

    def quit(self, ev):
        if ev.type == pygame.QUIT:
            self.running = False
            

    def main(self):
        """funksjonen som skal inholde alt av påkaling for at ting går framover.
        """
        
        while self.running:
            event = pygame.event.get()
            eventhandel(event)

