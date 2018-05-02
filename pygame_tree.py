import pygame, math
 
pygame.init()
width = 4000
height = 3000
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
 
def drawTree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth *10)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth *10)
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - 20, depth - 1)
        drawTree(x2, y2, angle + 20, depth - 1)

drawTree(width/2, height*3/4, -90, 20)
pygame.display.flip()

pygame.image.save(screen, "C:/Users/Jonas/Desktop/tree_img.png")
pygame.quit()
print("Done!")