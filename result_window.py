import pygame
import sys

my_list = []
list_length = len(my_list)

def set_result(my_list,list_length) :

    list_lenght = len(my_list)
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Set up the window
    WIDTH = 500
    HEIGHT = 700

    # Initialize Pygame
    pygame.init()

    # Create a new window
    list_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PORT SCANNER RESULT")

    # Set up the font
    font = pygame.font.SysFont("Arial", 24)
    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        list_screen.fill(BLACK)

        # Draw the headline label
        headline_label = font.render("PORT SCANNER RESULT IS : "+str(list_lenght), True, WHITE)
        headline_rect = headline_label.get_rect(center=(WIDTH//2, 50))
        list_screen.blit(headline_label, headline_rect)

        # Draw the contents of my_list
        y_offset = 100
        for port in my_list:
            label_text = "[*] Port {} is open".format(port)
            label = font.render(label_text, True, WHITE)
            label_rect = label.get_rect(center=(WIDTH//2, y_offset))
            list_screen.blit(label, label_rect)
            y_offset += 50

        # Update the screen
        pygame.display.flip()
        
if __name__ == '__main__': 
    print(set_result(my_list,list_length))