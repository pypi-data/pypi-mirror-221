import pygame
import pygame.locals


def line(screen, start, end, color=(0, 0, 0, 255), width=5):
    pygame.draw.line(screen.screen, color, start, end, width)

def circle(screen, position, radius, border={"width": 5, "color": (0, 0, 0, 255)}, fillColor=(0, 0, 0, 0)):
    if fillColor != (0, 0, 0, 0):
        pygame.draw.circle(screen.screen, fillColor, position, radius)
    pygame.draw.circle(
        screen.screen, border["color"], position, radius, border["width"])

def ellipse(screen, start, end, border={"width": 5, "color": (0, 0, 0, 255)}, fillColor=(0, 0, 0, 0), rotation=0):
    rect = pygame.Rect(start[0], start[1], end[0] -
                        start[0], end[1] - start[1])
    if fillColor != (0, 0, 0, 0):
        pygame.draw.ellipse(screen.screen, fillColor, rect)
    pygame.draw.ellipse(
        screen.screen, border["color"], rect, border["width"])

def polygon(screen, points, border={"width": 5, "color": (0, 0, 0, 255)}, fillColor=(0, 0, 0, 0)):
    if fillColor != (0, 0, 0, 0):
        pygame.draw.polygon(screen.screen, fillColor, points)
    pygame.draw.polygon(
        screen.screen, border["color"], points, border["width"])

def table(screen, start, end, rows, columns):
    size = (end[0]-start[0], end[1]-start[1])
    columnSize = size[0]/columns
    rowSize = size[1]/rows
    polygon(screen, [(start[0], start[1]), (start[1],
                    end[0]), (end[0], end[1]), (end[1], start[0])])
    for i in range(columns):
        line(screen, (start[0]+(columnSize*i),
                    start[1]), (start[0]+(columnSize*i), end[1]))
    for j in range(rows):
        line(screen, (start[0], start[1]+(rowSize*j)),
                    (end[1], start[1]+(rowSize*j)))
