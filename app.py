import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    Rect,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

# Initialize Pygame
pygame.init()

# Set the window size
window_width = 800
window_height = 600

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Set the button size
button_width = 200
button_height = 50

# Set the button positions at the bottom of the window
button1_rect = Rect(200, 550, button_width, button_height)
button2_rect = Rect(400, 550, button_width, button_height)

# Load the card images and get their size
card_image1 = pygame.image.load("img/club.png")
card_image2 = pygame.image.load("img/diamond.png")
card_image3 = pygame.image.load("img/heart.png")
card_image4 = pygame.image.load("img/spade.png")
card_width, card_height = card_image1.get_size()

# Calculate the scale factor
scale_factor = 0.5

# Scale the card images
card_image1 = pygame.transform.scale(card_image1, (int(card_width * scale_factor), int(card_height * scale_factor)))
card_image2 = pygame.transform.scale(card_image2, (int(card_width * scale_factor), int(card_height * scale_factor)))
card_image3 = pygame.transform.scale(card_image3, (int(card_width * scale_factor), int(card_height * scale_factor)))
card_image4 = pygame.transform.scale(card_image4, (int(card_width * scale_factor), int(card_height * scale_factor)))

# Get the display resolution
display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h

# Calculate the center point
center_x = display_width // 2
center_y = display_height // 2

# Set the card size and positions
card1_rect = Rect(center_x - card_width, center_y - card_height, card_width, card_height)
card2_rect = Rect(center_x, center_y - card_height, card_width, card_height)
card3_rect = Rect(center_x - card_width, center_y, card_width, card_height)
card4_rect = Rect(center_x, center_y, card_width, card_height)

# Set a flag to control the main game loop
running = True

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
    screen.fill((255, 255, 255))
    
    # Draw the buttons
    pygame.draw.rect(screen, (0, 255, 0), button1_rect)  # Green
    pygame.draw.rect(screen, (255, 0, 0), button2_rect)  # Red
    
    # Create the text for the buttons
    font = pygame.font.Font(None, 36)
    text1 = font.render("HIT", True, (0, 0, 0))
    text2 = font.render("STAY", True, (0, 0, 0))
    
    # Get the text size
    text1_width, text1_height = font.size("HIT")
    text2_width, text2_height = font.size("STAY")
    
    # Calculate the text position
    text1_x = button1_rect.centerx - text1_width // 2
    text1_y = button1_rect.centery - text1_height // 2
    text2_x = button2_rect.centerx - text2_width // 2
    text2_y = button2_rect.centery - text2_height // 2
    
    # Blit the text onto the buttons
    screen.blit(text1, (text1_x, text1_y))
    screen.blit(text2, (text2_x, text2_y))
    
    # Draw the cards
    screen.blit(card_image1, card1_rect)
    screen.blit(card_image2, card2_rect)
    screen.blit(card_image3, card3_rect)
    screen.blit(card_image4, card4_rect)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
