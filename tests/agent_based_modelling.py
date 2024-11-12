import random
import matplotlib.pyplot as plt

class Sheep:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)

class Shepherd:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_towards_sheep(self, sheep_list):
        # Simple logic: move towards the center of mass of the sheep
        avg_x = sum(sheep.x for sheep in sheep_list) / len(sheep_list)
        avg_y = sum(sheep.y for sheep in sheep_list) / len(sheep_list)
        self.x += (avg_x - self.x) * 0.1
        self.y += (avg_y - self.y) * 0.1

def simulate(num_sheep, num_steps):
    sheep_list = [Sheep(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_sheep)]
    shepherd = Shepherd(5, 5)

    for step in range(num_steps):
        for sheep in sheep_list:
            sheep.move()
        shepherd.move_towards_sheep(sheep_list)

        # Visualization (optional)
        if step % 10 == 0:
            plt.clf()
            plt.xlim(0, 10)
            plt.ylim(0, 10)
            for sheep in sheep_list:
                plt.scatter(sheep.x, sheep.y, color='blue')
            plt.scatter(shepherd.x, shepherd.y, color='red', marker='^')
            plt.pause(0.1)

# Example usage
num_sheep = 100
num_steps = 200
simulate(num_sheep, num_steps)
plt.show()
