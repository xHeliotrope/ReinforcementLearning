import torch as T
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
import numpy as np

class DeepQTurtle(nn.Module):
    """inspired by https://www.youtube.com/watch?v=1XX6N-Gq7Tc
    """
    def __init__(self, ALPHA):
        super(DeepQTurtle, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 8, stride=4, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 4, stride=2)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.fc1 = nn.Linear(128*19*8, 512)
        self.fc2 = nn.Linear(512, 6)

        self.optimizer = optim.RMSprop(self.parameters(), lr=ALPHA)
        self.loss = nn.MSELoss()
        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.to(self.device)

    def forward(self, observation):
        observation = T.Tensor(observation).to(self.device)
        observation = observation.view(-1, 1, 185, 95)
        observation = F.relu(self.conv1(observation))
        observation = F.relu(self.conv2(observation))
        observation = F.relu(self.conv3(observation))
        observation = observation.view(-1, 128*19*8)
        observation = F.relu(self.fc1(observation))

        actions = self.fc2(observation)
        return actions
