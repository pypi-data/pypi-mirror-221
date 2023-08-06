from threading import Thread

class Task:
    
    class TaskIsNotRunning(Exception):
        
        def __init__(self, name: str):
            super().__init__(f"(Task){name} has not been started yet.")
    
    def __init__(self, name: str, handler, method, args: tuple, iterations):
        self.method = method
        self.handler = handler
        self.name = name
        self.args = args
        self.iterations = iterations
        self.active = False
        
        self.thread = None
        
        
    def start(self):
        self.active = True
        
        def threadMethod(*args):
            if 0 < self.iterations <= 100:
                for i in range(self.iterations):
                    self.method(*args + (i+1))
                self.active = False
            else:
                while self.active:
                    self.method(*args)
             
        self.thread = Thread(target=threadMethod, name=self.name, 
                        args=self.args)
        
        self.thread.start()
        
    def kill(self):
        if self.active:
            self.active = False
            self.thread.join()
            self.thread = None
            print(f"(UserThread){self.name} has been terminated.")
        else:
            raise Task.TaskIsNotRunning(self.name)



class TaskHandler:
    
    class TaskNotFound(Exception):
        """Raised when a task doesnt exist

        Attributes:
            name -- The task name that caused the error
            message -- Explanation of the error
        """
        def __init__(self, name: str):
            self.name = name
            self.message = f"Task \"{self.name}\" does not exist. Have you created it?"
            super().__init__(self.message)
        
    class TaskAlreadyRunning(Exception):
        """Raised when a already running task is run a second time
        
        Attributes:
            name -- The task name that caused the error
            message -- Explanation of the error
        """
        def __init__(self, name: str):
            self.name = name
            self.message = f"Task \"{self.name}\" is already running."
            super().__init__(self.message)
    
    def __init__(self):
        self.tasks = []
    
    
    def create(self, name: str, method, args:tuple=(), iterations: int=0):
        """Create a new background task
        
        When using a set number of iterations, it will return an extra int argument to the tasks method; ex. (*args, ..., iteration_num:int)

        Args:
            name (str): the name of the task
            method (method): the method it will run
            args (tuple, optional): a tuple the of the arguments to pass. Defaults to ().
            iterations (int, optional): amount of iterations to run, 0 is a loop. Defaults to 0.
        """
        
        self.tasks.append(Task(name, self, method, args, iterations))
        
    def run(self, name: str):
        """Run a specified task by name

        Args:
            name (str): the name of the task
        """
        task = self.find(name)
        
        if task.active:
            raise TaskHandler.TaskAlreadyRunning(name)
        
        task.start()
        
        
    
    def kill(self, name: str):
        """Kill a specified background task by name

        Args:
            name (str): the name of the task

        Raises:
            TaskHandler.TaskNotFound: raised when no task with that name exists

        Returns:
            __Task: the task that was ended
        """
        task = self.find(name)
        
        task.kill()
        
        return task
        
    def toggle(self, name: str):
        """Toggle the background task

        Args:
            name (str): the name of the task to toggle
        """
        task = self.find(name)
        
        if task.active:
            self.kill(name)
        else:
            self.run(name)
            
    def end(self):
        "Kill all tasks"
        for task in self.tasks:
            if task.active:
                task.kill()
                    
        
    def find(self, name: str):
        "Find a task by name"
        for task in self.tasks:
            if task.name == name:
                return task
        raise TaskHandler.TaskNotFound(name)