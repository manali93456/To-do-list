task_list=[]
print('welcome to the todo list')
task_num=int(input('how many task you want to enter'))#5
for i in range(1,task_num+1):
    task_name=input(f'enter task{i}')
    task_list.append(task_name)
print(f'your tasks are:{task_list}')
while True:
    operation=int(input('enter 1 for Add task\nenter 2 for delete task\nenter 3 for update task\n enter 4 for view task\n enter 5 for stop todolist'))
    if(operation == 1):
        add_task=input('enter task which you want to add your todo list')
        task_list.append(add_task)
    elif(operation == 2):
        del_task=input('which task you want to delete')
        if(del_task in task_list):
            indx=task_list.index(del_task)
            del task_list[indx]
    elif(operation == 3):
        updt=input('enter task which you want to update')
        if(updt in task_list):
            new_task=input('enter new task')
            indx=task_list.index(updt)
            task_list[indx]=new_task
    elif(operation == 4):
        print(f'your task is\n{task_list}')

    elif(operation == 5):
        print('Todo list is closing...')
        break
    else:
        print('please enter valid number')
    
print('program finish')