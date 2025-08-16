print ("Hello Python world!")

import pygame
pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

 # forklaring af screen.fill((255, 255, 255)) = fill er en funktion der fylder skærmen
    # (0,0,0) er sort, (R,G,B) (255, 255, 255) er hvid.

pygame.draw.line(screen, (0, 0, 0), (100, 380), (540, 380)) # Draw a black line
pygame.draw.line(screen, (0, 0, 0), (100, 200), (540, 200)) # tegn toppen af huset, lave tal fra venstre og op til højre og ned
pygame.draw.line(screen, (0, 0, 0), (100, 200), (100, 380)) # tegn den venstre væg
pygame.draw.line(screen, (0, 0, 0), (540, 200), (540, 380)) # tegn den højre 


# Draw the ground
# Draw the bottom of the house
# Draw two walls
# Draw the roof

# forklaring : (x,y) til (x2,y2) er en linje under funktionen pygame.draw.line.
    # der findes flere forskellige funktioner man kan tegne med, f. eks pygame.draw.rect() 
    # eller pygame.draw.circle(), eller pygame.draw.polygon()

pygame.draw.polygon(screen, (0, 0, 0), [(100, 200), (320, 50), (540, 200)]) # tegner taget
# (100,200 betyder første punkt i polygonen 
# (320, 50) er det andet punkt i polygonen, og (540, 200) er det tredje punkt i polygonen.
# Det er vigtigt at bemærke, at tallenene vises i rækkefølge så lavere tal kommer oppe fra og ned, eller venstre til højre

pygame.draw.rect(screen,(0,0,0), (150, 200, 150, 180))
#(x, y, width, height)) 

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears
# Close the Pygame window
pygame.quit()   
