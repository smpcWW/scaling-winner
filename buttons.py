import pygame

def draw(screen, game_state):
    """Draws the buttons on the screen.

    Args:
        screen (pygame.Surface): The surface to draw the buttons on.
        game_state (dict): A dictionary containing the game state.
    """
    # Unpack the game state
    button1_rect = game_state["button1_rect"]
    button2_rect = game_state["button2_rect"]

    # Draw the buttons
    pygame.draw.rect(screen, (0, 255, 0), button1_rect)  # Green
    pygame.draw.rect(screen, (255, 0, 0), button2_rect)  # Red
    
    # Set the font and text colors
    font = pygame.font.Font(None, 36)
    text_color = (0, 0, 0)  # Black
    
    # Calculate the text positions
    text1_x = button1_rect.x + (button1_rect.width // 2) - (font.size("HIT")[0] // 2)
    text1_y = button1_rect.y + (button1_rect.height // 2) - (font.size("HIT")[1] // 2)
    text2_x = button2_rect.x + (button2_rect.width // 2) - (font.size("STAY")[0] // 2)
    text2_y = button2_rect.y + (button2_rect.height // 2) - (font.size("STAY")[1] // 2)
    
    # Render the text
    text1 = font.render("HIT", True, text_color)
    text2 = font.render("STAY", True, text_color)
    
    # Draw the text
    screen.blit(text1, (text1_x, text1_y))
    screen.blit(text2, (text2_x, text2_y))
