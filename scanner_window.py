import pygame
import sys
import scanner_Network
import result_window

pygame.init()

current_screen = 1
my_list = []
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the window
WIDTH = 500
HEIGHT = 700

# Set up the window
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("PORT SCANNER")

# Set up the font
font = pygame.font.SysFont("Arial", 24)

# Set up the input box
input_box = pygame.Rect(50, 100, 400, 40)
input_text = ""
input_entered = False

# Set up the "Delete" key flag
delete_pressed = False

    # Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and input_text:
                input_entered = True
                pygame.key.set_repeat(0, 0) # disable text input
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if event.unicode.isprintable():
                    input_text += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if input_box.collidepoint(event.pos):
                    # If the user clicked the input box
                    pygame.key.set_repeat(500, 50) # enable text input
                else:
                    pygame.key.set_repeat(0, 0) # disable text input

    # Clear the screen
    screen.fill(BLACK)

    # Draw the headline label
    headline_label = font.render("PORT SCANNER", True, WHITE)
    headline_rect = headline_label.get_rect(center=(WIDTH//2, 50))
    screen.blit(headline_label, headline_rect)

    # Draw the input box
    pygame.draw.rect(screen, (255, 255, 255), input_box, 2)
    text_surface = font.render(input_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Update the screen
    pygame.display.flip()

    # Check if "Enter" was pressed
    if input_entered:
        print("Input:", input_text)
        pygame.quit()
        break

#My test IP : 192.168.20.5
my_list = scanner_Network.scanner(input_text, my_list)
list_length = len(my_list)
print(my_list,list_length)
result_window.set_result(my_list,list_length)
