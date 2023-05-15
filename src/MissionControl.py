from Pose import Pose
from collections import deque

# Define a classe MissionControl, que representa a fila de pontos a serem seguidos
class MissionControl(deque):

    # Define a sequência de pontos para cada formato disponível
    spiral = [Pose(-1.0, 0.0), Pose(-1.0, -1.0),
                Pose(1.0, -1.0), Pose(1.0, 1.0),
                Pose(-1.0, 1.0)]

    def __init__(self):
        super().__init__()
        for pose in MissionControl.spiral:
            self.enqueue(pose)
        
    def enqueue(self, x):
        super().append(x)
    
    def dequeue(self):
        return super().popleft()