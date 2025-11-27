import pygame

from important_functions import *

class button_func:
    def __init__(self) -> None:
        self.window = window
    def button_one(self):
        pygame.draw.circle(self.window, "red", (100,100), 20)
