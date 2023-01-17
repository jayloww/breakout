import pygame
from brick import get_brick_h, get_brick_w, get_bricks


def cords_in_rect(x, y, rect_x, rect_y, rect_w, rect_h):
    return rect_x <= x <= rect_x + rect_w and rect_y <= y <= rect_y + rect_h


clock = pygame.time.Clock()


class Game:
    def __init__(self, w, h, paddle, ball, n_bricks_x, n_bricks_y):
        self.w = w
        self.h = h
        self.paddle = paddle
        self.ball = ball
        state = "ongoing"
        self.state = state
        self.font = pygame.font.SysFont("Arial", 30, )
        self.score = 0

        brick_w = get_brick_w(w, n_bricks_x)
        brick_h = get_brick_h(h, n_bricks_y)
        self.bricks = get_bricks(n_bricks_x, n_bricks_y, brick_w, brick_h)

    def update(self, screen):
        self.ball.move()

        if cords_in_rect(self.ball.x, self.ball.y, self.paddle.x, self.paddle.y, self.paddle.w, self.paddle.h):
            self.ball.dy *= -1

        if self.ball.x < self.ball.r or self.ball.x >= self.w - self.ball.r:
            self.ball.dx *= -1

        if self.ball.y < self.ball.r:
            self.ball.dy *= -1

        if self.ball.y >= self.h - self.ball.r:
            self.state = "lost"

        prev_bricks = self.bricks
        self.bricks = [brick for brick in self.bricks if
                       not cords_in_rect(self.ball.x, self.ball.y, brick.x, brick.y, brick.w, brick.h)]

        if len(prev_bricks) > len(self.bricks):
            self.ball.dy *= -1
            self.score += 100
            for brick in prev_bricks:
                if brick not in self.bricks:
                    missing_brick = brick

            surface_popup_score = self.font.render("+100", False, (250, 250, 250))
            text_rect_popup_score = surface_popup_score.get_rect(center=(self.w / 2, self.h / 2))
            screen.blit(surface_popup_score, text_rect_popup_score)
            pygame.display.flip()

        if len(self.bricks) == 0:
            self.state = "won"

    def draw(self, screen):
        screen.fill((0, 0, 0))
        if self.state == "ongoing":
            self.paddle.draw(screen)
            self.ball.draw(screen)
            for brick in self.bricks:
                brick.draw(screen)
        else:
            surface_state = self.font.render(f"You {self.state}", False, (250, 250, 250))
            surface_score = self.font.render(f"Score {self.score}", False, (250, 250, 250))

            text_rect_state = surface_state.get_rect(center=(self.w / 2, self.h / 2))
            text_rect_score = surface_score.get_rect(center=(self.w / 2, self.h / 2 + 30))

            screen.blit(surface_state, text_rect_state)
            screen.blit(surface_score, text_rect_score)

        pygame.display.flip()
