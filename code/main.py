"""
    pygame er biblioteket som vi bruker for å lage hele programmet
    python weather kommer til å bli brukt 
"""
import pygame

# from event_handel import eventhandel

window = pygame.display.set_mode((400,400))

class Main_handel:
    """
    inholder alt.
    """
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((400,400))
        self.running= True # om main loopen skal kjøre

    def event_handel(self, ev):
        """runs pygame events

        Args:
            ev (list): list of all events in pygame and wether they are true or false.
        """
        if ev.type == pygame.QUIT:
            self.running = False

    def name(self):
        """idk
        """
        pass

    def main(self):
        """funksjonen som skal inholde alt av påkaling for at ting går framover.
        """

        while self.running:
            event = pygame.event.wait()
            self.event_handel(event)

            pygame.display.flip()

main = Main_handel()
main.main()
