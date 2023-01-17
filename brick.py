import pygame


def get_brick_w(screen_w, n_bricks_x):
    return 2 * screen_w / (3 * n_bricks_x + 1)


def get_brick_h(screen_h, n_bricks_y):
    return screen_h / (3 * n_bricks_y + 1)


def get_bricks(n_bricks_x, n_bricks_y, brick_w, brick_h):
    bricks = []
    for i in range(n_bricks_x):
        for j in range(n_bricks_y):
            brick_x = i * brick_w + (i + 1) * brick_w / 2
            brick_y = j * brick_h + (j + 1) * brick_h / 2

            brick = Brick(brick_x, brick_y, brick_w, brick_h, color=(255, 255, 255))
            bricks.append(brick)
    return bricks


class Brick:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def __repr__(self):
        return f"Paddle(x={self.x}, y={self.y}, w ={self.w}, h={self.h}, color={self.color} )"

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
