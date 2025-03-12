from base_env.base_agent import Agent
from base_env.base_grid import Grid

class GridEnv(Grid):
    def __init__(self, rows, cols):
        super(GridEnv, self).__init__(rows=rows, cols=cols)
        self.happiness = []
        self.similarity = []


    def step(self, threshold=.5):
        pass

# if __name__ == '__main__':
#     agent_1 = Agent(agent_type='A')
#     agent_2 = Agent(agent_type='B')
#     agent_3 = Agent(agent_type='B')
#     agent_4 = Agent(agent_type='B')
#
#     grid = GridEnv(5, 5)
#     grid.initialize(agent_1, 2, 1)
#     grid.initialize(agent_2, 2, 2)
#     grid.initialize(agent_3, 2, 3)
#     grid.initialize(agent_4, 2, 4)
#
#     similarity = grid.count_similarity(agent_1.x, agent_1.y, 'A')
#     print(f"agent_1 similarity is: {similarity}")
#
#     print(f"Agent1 位置: ({agent_1.x}, {agent_1.y})")
#
#     similarity = grid.count_similarity(agent_2.x, agent_2.y, 'B')
#     print(f"agent_2 similarity is: {similarity}")
#
#     similarity = grid.count_similarity(agent_3.x, agent_3.y, 'B')
#     print(f"agent_3 similarity is: {similarity}")
