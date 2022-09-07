class Container:
    def __init__(self,memory,cost,functionType,containerId) -> None:
        self.mem=memory
        self.visited=False
        self.visited_time=0
        self.priority=0
        self.cost=cost
        self.functionType=functionType
        self.containerId=containerId
