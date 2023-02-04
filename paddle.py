import pygame


class Paddle:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def move(self, x_pos, window_w):
        self.x = x_pos - self.w // 2
        if self.x + self.w > window_w:
            self.x = window_w - self.w
        elif self.x < 0:
            self.x = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

    def __repr__(self):
        return f"Paddle(x={self.x}, y={self.y}, w ={self.w}, h={self.h}, color={self.color} )"
