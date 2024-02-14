class to_do_list:
  def __init__(self) :
    self.task=[]
  
  def create_task(self,task):
    self.task.append(str(task))
    print(f"Task '{task}' added\n\n--------------------------------\n")
  
  def remove_task(self,task):
    if not self.task:
      print("  Oops! no task in here :(\n\n--------------------------------\n")
    elif task in self.task:
      self.task.remove(task)
      print(f"Task '{task}' Removed\n\n--------------------------------\n")
    else:
      print(f"task '{task}' not registered\n\n--------------------------------\n") 

  def display(self):
    if not self.task:
      print("  Oops! no task in here :(\n\n--------------------------------\n")
    else:
      for task in enumerate(self.task):
        print(f"{task}")

def main():

  todolist = to_do_list()

  while(True):
    print("\n1.Add task\n2.Remove task\n3.Display task\n")
    ch=input("enter your choice (add/rem/dis/exit):\n")

    if ch=='add':
      task_name=str(input("enter the task:"))
      todolist.create_task(task_name)

    elif ch=='rem':
      task_name=input("enter your task to remove:")
      todolist.remove_task(task_name)

    elif ch=='dis':
      todolist.display()

    elif ch=='exit':
      print("exiting")
      break
    else:
      print("invalid choice re-run the program")

if __name__=="__main__":
  main()
