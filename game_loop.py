import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

import buttons

def run(game_state):
    """Runs the main game loop.

    Args:
        game_state (dict): A dictionary containing the game state.
    """
    # Unpack the game state
    screen = game_state["screen"]
    button1_rect = game_state["button1_rect"]
    button2_rect = game_state["button2_rect"]
    card_image1 = game_state["card_image1"]
    card_image2 = game_state["card_image2"]
    card_image3 = game_state["card_image3"]
    card_image4 = game_state["card_image4"]
    card1_rect = game_state["card1_rect"]
    card2_rect = game_state["card2_rect"]
    card3_rect = game_state["card3_rect"]
    card4_rect = game_state["card4_rect"]
    running = game_state["running"]

    # Main game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            # Quit the game if the user closes the window or presses the escape key
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            # Check if a button was clicked
            elif event.type == MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(event.pos):
                    # Button 1 was clicked
                    print("Button 1 was clicked")
                if button2_rect.collidepoint(event.pos):
                    # Button 2 was clicked
                    print("Button 2 was clicked")

        # Clear the screen
        screen.fill((255, 255, 255))  # White background
        
        # Draw the buttons
        buttons.draw(screen, game_state)
        
        # Draw the cards
        screen.blit(card_image1, card1_rect)
        screen.blit(card_image2, card2_rect)
        screen.blit(card_image3, card3_rect)
        screen.blit(card_image4, card4_rect)
        
        # Update the display
        pygame.display.flip()
