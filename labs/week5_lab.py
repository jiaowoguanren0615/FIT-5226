from base_env.base_grid import Grid
from base_env.base_agent import Agent

from typing import Tuple, Any
import random
import numpy as np
import argparse
from utils import AverageMeter, MetricLogger



def get_argparser():
    parser = argparse.ArgumentParser('FIT-5226 WEEK5 Solution Script', add_help=False)
    parser.add_argument("--rows", type=int, default=5, help="rows of grid")
    parser.add_argument("--cols", type=int, default=5, help="cols of grid")
    parser.add_argument("--A_position", type=tuple, default=(1, 3), help="position of agentA")
    parser.add_argument("--B_position", type=tuple, default=(2, 4), help="position of agentB")
    parser.add_argument("--epochs", type=int, default=100, help="total epochs for simulate")
    return parser



def random_policy():
    """固定的随机策略：每次都在4个动作中随机挑一个"""
    return np.random.choice([1, 2, 3, 4])  # N,S,W,E

class GridWorld(Grid):
    def __init__(self,
                 rows: int,
                 cols: int,
                 A_position: Tuple[int, int],
                 B_position: Tuple[int, int]
        ):
        super(GridWorld, self).__init__(rows=rows, cols=cols)

        self.rows = rows
        self.cols = cols

        self.agentA = Agent()
        self.agentA.set_position(A_position[0], A_position[1])

        self.agentB = Agent()
        self.agentB.set_position(B_position[0], B_position[1])

        self.state = None # (x, y, has_load)


    def reset(self):
        """随机初始化智能体位置 & 货物未被拾取"""
        x = random.randint(0, self.rows - 1)
        y = random.randint(0, self.cols - 1)
        has_load = 0
        self.state = (x, y, has_load)
        return self.state


    def step(self, action) -> Tuple[Any, float, bool]:
        """
        根据 action 更新状态并返回:
          next_state, reward, done, info
        """

        reward = -1 # 分数 用于奖惩 每走一步 reward = -1（鼓励尽快完成任务）

        # print(reward)
        x, y, has_load = self.state

        # 如果到了A并且还没拿货，自动拾取
        if (x, y) == (self.agentA.x, self.agentA.y) and has_load == 0:
            has_load = 1
            reward += 1

        # 判断是否送达B
        done = False

        # 如果已经携带货物并且到了B，任务完成
        if has_load == 1 and (x, y) == (self.agentB.x, self.agentB.y):
            done = True
            # 可以给一个大的正奖励
            reward = 10
            has_load -= 1

        # 根据动作更新坐标
        if action == 1:  # North
            y = max(y - 1, 0)
        elif action == 2:  # South
            y = min(y + 1, self.cols - 1)
        elif action == 3:  # West
            x = max(x - 1, 0)
        elif action == 4:  # East
            x = min(x + 1, self.rows - 1)


        next_state = (x, y, has_load)
        self.state = next_state

        return next_state, reward, done



def main(args):
    env = GridWorld(rows=args.rows, cols=args.cols,
                    A_position=args.A_position, B_position=args.B_position)
    state = env.reset()

    metric_logger = MetricLogger(delimiter=" | ")
    avg_reward_meter = AverageMeter()

    for epoch in range(args.epochs):
        action = random_policy()
        next_state, reward, done = env.step(action)


        avg_reward_meter.update(reward)
        metric_logger.update(reward=reward)

        print(f"Step {epoch + 1:2d}: Action = {action}, Reward = {reward:.4f}, "
              f"Average Reward = {avg_reward_meter.avg:.4f}, State = {next_state}")
        if done:
            print("Task completed!")
            break



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'FIT-5226 WEEK5 Solution Script', parents=[get_argparser()])
    args = parser.parse_args()
    main(args)