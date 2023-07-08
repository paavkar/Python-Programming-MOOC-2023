# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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
    

class OrderBookApplication:

    def __init__(self):
        self.__order_book = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("desciption: ")
        try:
            programmer, workload = input("programmer and workload estimate: ").split(" ")
            self.__order_book.add_order(description, programmer, int(workload))
            print("added!")
        except:
            print("erroneous input")
            return

    def list_finished(self):
        finished = self.__order_book.finished_orders()
        if finished:
            for task in finished:
                print(task)
        else:
            print("no finished tasks")

    def list_unfinished(self):
        unfinished = self.__order_book.unfinished_orders()
        if unfinished:
            for task in unfinished:
                print(task)
        else:
            print("no unfinished tasks")

    def mark_finished(self):
        try:
            task_id = int(input("id: "))
            self.__order_book.mark_finished(task_id)
            print("marked as finished")
        except:
            print("erroneous input")
            return

    def list_programmers(self):
        programmers = self.__order_book.programmers()
        for programmer in programmers:
            print(programmer)

    def programmer_status(self):
        programmer = input("programmer: ")
        try:
            tasks = self.__order_book.status_of_programmer(programmer)
            print(f"tasks: finished {tasks[0]} not finished {tasks[1]}, hours: done {tasks[2]} scheduled {tasks[3]}")
        except:
            print("erroneous input")
            return

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if(command == "0"):
                break
            elif(command == "1"):
                self.add_order()
            elif(command == "2"):
                self.list_finished()
            elif(command == "3"):
                self.list_unfinished()
            elif(command == "4"):
                self.mark_finished()
            elif(command == "5"):
                self.list_programmers()
            elif(command == "6"):
                self.programmer_status()
            else:
                self.help()

application = OrderBookApplication()
application.execute()