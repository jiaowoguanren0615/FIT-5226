import random
from base_env.logger_record import log_function

random.seed(2025) # fix random seed


class Agent(object):
    def __init__(self, agent_type=None):
        self.x = None
        self.y = None
        self.agent_type = agent_type

    @log_function
    def set_position(self, x, y):
        self.x, self.y = x, y

    @log_function
    def sense(self, grid):
        # Example: sense neighboring cells
        neighborhood = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = (self.x + dx) % grid.rows, (self.y + dy) % grid.cols
                if (dx, dy) != (0, 0):
                    neighborhood.append(grid.grid[nx][ny])
        return neighborhood

    @log_function
    def act(self, grid, perception, threshold):
        # Schelling model decision to move or stay
        similar = sum(1 for agent in perception if agent and agent.agent_type == self.agent_type)
        total = sum(1 for agent in perception if agent)
        similarity = similar / total if total != 0 else 0
        if similarity < threshold:
            empty_cells = grid.empty_positions
            if empty_cells:
                grid.move(self)


    def __repr__(self):
        return f"<Agent type={self.agent_type} pos=({self.x},{self.y})>"