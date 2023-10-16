# TO-DO FILE

# task = int(input("Enter the number of task required : "))
todos = []
# here, the while loop
while 1:
    user_prompt = input('Type add or show or exit or edit or complete: ')
    user_prompt = user_prompt.strip()  # this is used to avoid the space error like 'add ' f
    # this match is like switch case of the c and c++
    # it is the decision-making
    match user_prompt:
        case 'add':
            todo = input('Enter the todo: ')
            todos.append(todo.title())
        case 'show' | 'display':
            for index,item in enumerate(todos):
                print(f"{index+1}. {item.capitalize()}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))  # here, int is used to convert the input str to int
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[int(number)] = new_todo
        case 'exit':
            break
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case whatever:  # this whatever displays when you enter the unknown value in the user_prompt
            print('Hey, you enter the unknown command')
    # task -= 1

print('Bye!')