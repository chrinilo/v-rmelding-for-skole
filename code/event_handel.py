def eventhandel(event):
    """håndterer alt av events som kan skje. dette kan være ting som mus click eller bevegelse 

    Args:
        event (_type_): en liste med alle events og om de er sann

    Returns:
        _type_: _description_
    """
    event = pygame.event.get()
    
    if event.type == pygame.QUIT:
        return False
    