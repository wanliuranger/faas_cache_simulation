import numpy

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


class gd_record:
    def __init__(self,containerId,value) -> None:
        self.containerId=containerId
        self.value=value
        self.original_value=value


class Greedy_Dual:
    def __init__(self) -> None:
        self.priority_lst=[]
        self.containerid_to_index={}

    def add_to_gd(self,containerId,value):
        record=gd_record(containerId,value)
        self.priority_lst.append(record)
        self.containerid_to_index[containerId]=len(self.priority_lst)-1
    
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
        self.priority_lst.pop(small_index)

    def 
    