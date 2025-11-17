"""
    pygame er biblioteket som vi bruker for å lage hele programmet
    python weather kommer til å bli brukt 
"""
import pygame

#local files
import important_functions
import buttons_template
import button_functions


class Main_handel:
    """
    inholder alt.
    """
    def __init__(self, window) -> None:
        self.window = window
        self.running= True # om main loopen skal kjøre
        self.button_func = button_functions.button_func()
    def event_handel(self, ev):
        """runs pygame events

        Args:
            ev (list): list of all events in pygame and wether they are true or false.
        """
        if ev.type == pygame.QUIT:
            self.running = False
    
    def button_one(self, state: bool):
        if state == True:
                pygame.draw.circle(self.window, "red", (100,100), 20)

    def main(self):
        """funksjonen som skal inholde alt av påkaling for at ting går framover.
        """
        button = buttons_template.Button((100,100,100,100), "#ffff00")
        while self.running:

            self.window.fill("#58ff82")
            event = pygame.event.wait()
            self.event_handel(event)
            
            
            button.create_button()
            
            
            button_state = button.button_cliced(event)
            while button_state == True:
                self.button_func.button_one(button_state)
            pygame.display.flip()

main = Main_handel(important_functions.window)
main.main()
