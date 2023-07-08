# Write your solution here:
class Task:
    id = 0

    def __init__(self, description: str,  programmer: str, workload: int):
        Task.id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__is_finished = False
        self.id = Task.id

    def is_finished(self):
        return self.__is_finished

    def mark_finished(self):
        self.__is_finished = True

    def __str__(self):
        if(self.is_finished()):
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"
    
class OrderBook:

    def __init__(self):
        self.orders = []

    def add_order(self, description: str,  programmer: str, workload: int):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return list(set([order.programmer for order in self.orders]))
    
    def mark_finished(self, id: int):
        ids = [order.id for order in self.orders]
        if(id in ids):
            for order in self.orders:
                if(id == order.id):
                    order.mark_finished()
                    return
        else:
            raise ValueError("no task found with such id")
            
    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if(programmer not in self.programmers()):
            raise ValueError
        tasks = [task for task in self.orders if task.programmer == programmer]
        finished = [task for task in tasks if task.is_finished()]
        unfinished = [task for task in tasks if not task.is_finished()]
        return (len(finished), len(unfinished), sum([task.workload for task in finished]), sum([task.workload for task in unfinished]))
    
    def __str__(self):
        if(self.is_finished()):
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"
    
### Example solution
def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        raise ValueError("wrong id")