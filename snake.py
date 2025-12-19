"""
Snake multiplayer game implementation.

"""

#build a module to run a multiplayer snake game
import pygame

class SnakeGame:
    def __init__(self, width=600, height=400):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Multiplayer Snake Game')
        self.clock = pygame.time.Clock()
        self.snakes = []
        self.food = None
        self.running = True

    def add_snake(self, color, start_pos):
        snake = {'color': color, 'positions': [start_pos], 'direction': (0, 0)}
        self.snakes.append(snake)

    def place_food(self):
        import random
        x = random.randint(0, (self.width - 10) // 10) * 10
        y = random.randint(0, (self.height - 10) // 10) * 10
        self.food = (x, y)

    def run(self):
        self.place_food()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))

            for snake in self.snakes:
                for pos in snake['positions']:
                    pygame.draw.rect(self.screen, snake['color'], pygame.Rect(pos[0], pos[1], 10, 10))

            if self.food:
                pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food[0], self.food[1], 10, 10))

            pygame.display.flip()
            self.clock.tick(15)

        pygame.quit()
    
if __name__ == "__main__":
    game = SnakeGame()
    game.add_snake((0, 255, 0), (100, 100))  # Green snake
    game.add_snake((0, 0, 255), (200, 200))  # Blue snake
    game.run()  