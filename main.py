import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    Rect,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

import cards
import buttons
import game_loop

# Initialize Pygame
pygame.init()

# Set the window size
window_width = 800
window_height = 600

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Set the button size and positions
button_width = 200
button_height = 50
button1_rect = Rect(200, 550, button_width, button_height)
button2_rect = Rect(400, 550, button_width, button_height)

# Load the card images
card_image1 = cards.load_image("img/club.png")
card_image2 = cards.load_image("img/diamond.png")
card_image3 = cards.load_image("img/heart.png")
card_image4 = cards.load_image("img/spade.png")

# Set the card size
card_width, card_height = card_image1.get_size()

# Calculate the card positions
card_x = (window_width - (card_width * 2)) // 2
card_y = (window_height - (card_height * 2)) // 2
card1_rect = Rect(card_x, card_y, card_width, card_height)
card3_rect = Rect(card_x + card_width, card_y, card_width, card_height)
card2_rect = Rect(card_x, card_y + card_height, card_width, card_height)
card4_rect = Rect(card_x + card_width, card_y + card_height, card_width, card_height)

# Set the game state
game_state = {
    "running": True,
    "screen": screen,
    "button1_rect": button1_rect,
    "button2_rect": button2_rect,
    "card_image1": card_image1,
    "card_image2": card_image2,
    "card_image3": card_image3,
    "card_image4": card_image4,
    "card1_rect": card1_rect,
    "card2_rect": card2_rect,
    "card3_rect": card3_rect,
    "card4_rect": card4_rect,
}

# Run the game loop
game_loop.run(game_state)

# Quit Pygame
pygame.quit()
