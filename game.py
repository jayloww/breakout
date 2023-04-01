import pygame
import time
from brick import get_brick_h, get_brick_w, get_bricks
from util import cords_in_rect

TEXT_COLOR = (149, 42, 163)
SCORE_DURATION = 0.2


class Game:
    def __init__(self, w, h, paddle, ball, n_bricks_x, n_bricks_y):
        self.w = w
        self.h = h
        self.paddle = paddle
        self.ball = ball
        self.state = "ongoing"
        self.font = pygame.font.SysFont("Arial", 30)
        self.score = 0
        # time when last block got destroyed
        self.block_destroyed = None
        self.destroyed_bricks = []

        brick_w = get_brick_w(w, n_bricks_x)
        brick_h = get_brick_h(h, n_bricks_y)
        self.bricks = get_bricks(n_bricks_x, n_bricks_y, brick_w, brick_h)

    def update(self):
        self.ball.move()

        if cords_in_rect(
            self.ball.x,
            self.ball.y,
            self.paddle.x,
            self.paddle.y,
            self.paddle.w,
            self.paddle.h,
        ):
            self.ball.dy *= -1

        if self.ball.x < self.ball.r or self.ball.x >= self.w - self.ball.r:
            self.ball.dx *= -1

        if self.ball.y < self.ball.r:
            self.ball.dy *= -1

        if self.ball.y >= self.h - self.ball.r:
            self.state = "lost"

        any_bricks_destroyed = False
        new_bricks = []
        for i, brick in enumerate(self.bricks):
            if cords_in_rect(
                self.ball.x, self.ball.y, brick.x, brick.y, brick.w, brick.h
            ):
                any_bricks_destroyed = True
                self.destroyed_bricks.append(brick)
            else:
                new_bricks.append(brick)

        if any_bricks_destroyed:
            self.ball.dy *= -1
            self.score += 100
            self.block_destroyed = time.time()

        self.bricks = new_bricks

        if len(self.bricks) == 0:
            self.state = "won"

    def draw(self, screen):
        screen.fill((0, 0, 0))
        if self.state == "ongoing":
            self.paddle.draw(screen)
            self.ball.draw(screen)
            for brick in self.bricks:
                brick.draw(screen)
            if self.block_destroyed:
                if time.time() - self.block_destroyed < SCORE_DURATION:
                    for brick in self.destroyed_bricks:
                        surface_popup_score = self.font.render("+100", False, TEXT_COLOR)
                        text_rect_popup_score = surface_popup_score.get_rect(
                            center=(brick.x + brick.w / 2, brick.y + brick.h / 2)
                        )
                        screen.blit(surface_popup_score, text_rect_popup_score)
                else:
                    self.destroyed_bricks.clear()
        else:
            surface_state = self.font.render(f"You {self.state}", False, TEXT_COLOR)
            surface_score = self.font.render(f"Score {self.score}", False, TEXT_COLOR)

            text_rect_state = surface_state.get_rect(center=(self.w / 2, self.h / 2))
            text_rect_score = surface_score.get_rect(
                center=(self.w / 2, self.h / 2 + 30)
            )

            screen.blit(surface_state, text_rect_state)
            screen.blit(surface_score, text_rect_score)

        pygame.display.flip()
