from container import Container
import heapq

class Sheduler:
    def __init__(self) -> None:
        self.clock=0 #全局clock值
        self.totalMem=0 #当前池子中的内存
        self.containers={} #当前池子中的容器
        self.sortedContainerId=[] #根据priority对池子的id进行降序排列
        self.functionInstance={} #函数类型对应的容器列表

    def addContainer(self,c: Container):
        c.priority=self.calPriority(c)
        

    def getVisitedTime(self,functionType):
        return sum([c.visited_time for c in self.containers if c.functionType==functionType])

    def calPriority(self,c:Container):
        return self.clock+self.getVisitedTime(c.functionType)*c.cost/c.mem

        
        