import numpy
from sqlalchemy import func, true

def remove_from_gd_queue(priority_lst):
    small=priority_lst[0]
    small_index=0
    for i in range(len(priority_lst)):
        if (priority_lst[i].value<small.value):
            small=priority_lst[i]
            small_index=i
    for p in priority_lst:
        p.value=p.value-small.value
    priority_lst.pop(small_index)

def update_gd_queue(priority_lst, index, value):
    priority_lst[index].value=value


class container_record:
    def __init__(self,functionId,containerId,value) -> None:
        self.functionId=functionId
        self.containerId=containerId
        self.value=value
        self.original_value=value
        self.visited=False


class Greedy_Dual:
    def __init__(self) -> None:
        self.priority_lst=[]
        self.containerid_to_index={}
        self.functionId_to_containerId={}

    def add_to_gd(self,functionId,containerId,value):
        record=container_record(functionId,containerId,value)
        self.priority_lst.append(record)
        self.containerid_to_index[containerId]=len(self.priority_lst)-1
        if (functionId in self.functionId_to_containerId):
            self.functionId_to_containerId[functionId].append(containerId)
        else:
            self.functionId_to_containerId[functionId]=[]
            self.functionId_to_containerId[functionId].append(containerId)
        self.functionId_to_containerId[functionId].sort(key=lambda x:self.priority_lst[self.containerid_to_index[x]].value,reverse=True)
    
    def gd_queue_pop(self):
        small=self.priority_lst[0]
        small_index=0
        for i in range(len(self.priority_lst)):
            if (self.priority_lst[i].value<small.value):
                small=self.priority_lst[i]
                small_index=i
        for p in self.priority_lst:
            p.value=p.value-small.value
        del self.containerid_to_index[small.containerId]
        self.functionId_to_containerId[small.functionId].remove(small.containerId)
        self.functionId_to_containerId[small.functionId].sort(key=lambda x:self.priority_lst[self.containerid_to_index[x]].value,reverse=True)
        self.priority_lst.pop(small_index)

    def clear_visit_state(self):
        for r in self.priority_lst:
            r.visited=False;

    def visit_container(self,functionId) -> bool:
        if (functionId in self.functionId_to_containerId):
            idx=len(self.functionId_to_containerId[functionId])-1
            while (idx>=0):
                if (self.priority_lst[self.containerid_to_index[self.functionId_to_containerId[functionId][idx]]].visited==False):
                    self.priority_lst[self.containerid_to_index[self.functionId_to_containerId[functionId][idx]]].visited=True;
                    self.priority_lst[self.containerid_to_index[self.functionId_to_containerId[functionId]]].value=self.priority_lst[self.containerid_to_index[self.functionId_to_containerId[functionId]]].original_value
                    self.functionId_to_containerId[functionId].sort(key=lambda x:self.priority_lst[self.containerid_to_index[x]].value,reverse=True)
                    return True
        return False
    