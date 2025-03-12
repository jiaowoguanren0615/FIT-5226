import random

random.seed(2025) # fix random seed


class Agent(object):
    def __init__(self, agent_type):
        self.x = None
        self.y = None
        self.agent_type = agent_type


    def set_position(self, x, y):
        self.x, self.y = x, y

    def sense(self, grid):
        # Example: sense neighboring cells
        neighborhood = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = (self.x + dx) % grid.rows, (self.y + dy) % grid.cols
                if (dx, dy) != (0, 0):
                    neighborhood.append(grid.grid[nx][ny])
        return neighborhood

    def act(self, grid, perception):
        # Example: Schelling model decision to move or stay
        similar = sum(1 for agent in perception if agent and agent.agent_type == self.agent_type)
        total = sum(1 for agent in perception if agent)
        if total > 0 and (similar / total) < 0.5:  # If less than 50% similar neighbors
            # Move to a random empty nearby cell
            empty_cells = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                           if (dx, dy) != (0, 0) and
                           grid.grid[(self.x + dx) % grid.rows][(self.y + dy) % grid.cols] is None]
            if empty_cells:
                move_dx, move_dy = random.choice(empty_cells)
                grid.move_agent(self, move_dx, move_dy)