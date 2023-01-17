import pygame.draw


class Ball:
    def __init__(self, x, y, dx, dy, r, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color = color

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def __repr__(self):
        return f"Ball(x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy}, r={self.r}, color={self.color}"
