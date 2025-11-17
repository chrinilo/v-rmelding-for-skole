import pygame
from important_functions import window
from icecream import ic

class Button:
    def __init__(self, size: tuple, colour: str):
        self.size = size
        self.colour = colour

    def create_button(self):
        pygame.draw.rect(window,self.colour,self.size)
    
    def button_cliced(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            
            if (self.size[0] <= pygame.mouse.get_pos()[0] <= self.size[0]+ self.size[2] and
                self.size[1] <= pygame.mouse.get_pos()[1] <= self.size[1]+ self.size[3]):
                return True
        return False
