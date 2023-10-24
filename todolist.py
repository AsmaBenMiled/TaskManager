tasks = []  # Liste des tâches


def main():
  msg = """1 - Add tasks to a list
2 - Mark task as complete
3 - View tasks
4 - Quit"""


  while True:
      print(msg)
      choice = input("Enter your choice: ")

      if choice == "1":
          add_task()
      elif choice == "2":
          mark_task_as_complete()
      elif choice == "3":
          view_tasks()
      elif choice == "4":
          break
      else:
          print("Invalid choice, please enter a number between 1 and 4!")
          print("-"*30)
 

def add_task():
  #get task from user
 task = input("Enter the task: ")
  #etat, task status dict with key value: add detalis related to the task
 task_info = {"task": task, "completed": False}
  #add task to the list "tasks"
 tasks.append(task_info)
 print("Task added to the list successfully!")
 print("+"*30)
print("WELCOME !")


def mark_task_as_complete():
  # Get a list of incomplete tasks: check the status if the task is not completed, add it to the list
  incompl_tasks = []
  for task in tasks:
      if task["completed"] == False:
          incompl_tasks.append(task)
        
   #si liste vide     
  if len(incompl_tasks) == 0:
    print("No tasks to mark as complete")
    print("!"*30)
    return

  # Show incomplete tasks to the user
  for i, task in enumerate(incompl_tasks):
        print(f"{i + 1}- {task['task']}")
        print("*"*30)

  #get task from user: from dict of the list use index to change status
  try:
   task_num = int(input("choose the task number to complete: "))

   if task_num < 1 or task_num > len(incompl_tasks):
     print("Invalid task number !")
     print("-"*30)
     return
     
   #mark task as completed : tache n° terminée 
   incompl_tasks[task_num - 1]["completed"] = True 

   print("Task marked completed")
   print("-"*30)
  except ValueError:
    print("Invalid input, please enter a number")
    print("-"*30)



def view_tasks():
  #no tasks 
  if not tasks:
    print("No tasks to view ")
    print("!"*30)

  #show tasks 
  for i, task in enumerate(tasks):
    status = "✔" if task["completed"]  else "❌"
    print(f"{i + 1}. {task['task']} {status}")
    print("*"*30)


main()
