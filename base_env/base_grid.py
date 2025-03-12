import functools
import random
from base_env.base_agent import Agent
from abc import ABC

random.seed(2025) # fix random seed

class Grid(ABC):
    ## Base Module
    def __init__(self, rows: int, cols: int, **kwargs):
        # initial parameters
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.empty_positions = [(x, y) for x in range(rows) for y in range(cols)]
        self.agents = []
        self.occupied_positions = []


    def initialize(self, agent: Agent, x: int, y: int):
        if self.grid[x][y] is None:
            self.grid[x][y] = agent
            agent.set_position(x, y)
            self.agents.append(agent)
            self.empty_positions.remove((x, y))
            self.occupied_positions.append((x, y))


    def populate(self, agent_class, count, **kwargs):
        free_positions = [(x, y) for x in range(self.rows) for y in range(self.cols) if self.grid[x][y] is None]
        for _ in range(min(count, len(free_positions))):
            x, y = random.choice(free_positions)
            free_positions.remove((x, y))
            agent = agent_class(**kwargs)
            self.initialize(agent, x, y)


    def get_all_neighbors(self, x, y):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                neighbors.append(self.grid[nx][ny]) # include None Type
        return neighbors

    def update_position(self, agent, new_x, new_y):
        self.grid[agent.x][agent.y] = None
        self.empty_positions.append((agent.x, agent.y))
        self.occupied_positions.remove((agent.x, agent.y))

        self.grid[new_x][new_y] = agent
        self.empty_positions.remove((new_x, new_y))
        self.occupied_positions.append((new_x, new_y))

        agent.set_position(new_x, new_y)

    def move(self, agent):
        if self.empty_positions:
            target_x, target_y = random.choice(self.empty_positions)
            self.update_position(agent, target_x, target_y)
            return

    def count_similarity(self, x, y, agent_type):
        neighbors = self.get_all_neighbors(x, y)
        same_type_count = sum(1 for agent in neighbors if agent is not None and agent.agent_type == agent_type)
        total_agents = sum(1 for agent in neighbors if agent is not None)
        similarity = same_type_count / total_agents if total_agents != 0 else 0
        return similarity


    def step(self, threshold=.5):
        # main method for re-writing
        pass

    @staticmethod
    @functools.lru_cache(maxsize=512)
    def is_valid_position(x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols


# if __name__ == '__main__':
#     agent_1 = Agent(agent_type='A')
#     agent_2 = Agent(agent_type='B')
#     agent_3 = Agent(agent_type='B')
#
#     grid = Grid(5, 5)
#     grid.initialize(agent_1, 2, 1)
#     grid.initialize(agent_2, 2, 2)
#     grid.initialize(agent_3, 2, 3)
#
#     similarity = grid.count_similarity(agent_1.x, agent_1.y, 'A')
#     print(f"agent_1 similarity is: {similarity}")
#
#     print(f"Agent1 位置: ({agent_1.x}, {agent_1.y})")
#
#     grid.move(agent_1)
#     print(f"Agent1 新位置: ({agent_1.x}, {agent_1.y})")
#
#     similarity = grid.count_similarity(agent_2.x, agent_2.y, 'B')
#     print(f"agent_2 similarity is: {similarity}")
#     grid.move(agent_2)
#     print(f"Agent2 新位置: ({agent_2.x}, {agent_2.y})")