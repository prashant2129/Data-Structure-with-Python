
write_stack = []
rewrite_stack = []

def changes():
    text = input("Enter any text: ")
    write_stack.append(text)
    rewrite_stack.clear()  # clear redo history after new change

def undo_operation():
    if write_stack:
        a = write_stack.pop()
        rewrite_stack.append(a)
    else:
        print("No text to undo.")

def redo_operation():
    if rewrite_stack:
        a = rewrite_stack.pop()
        write_stack.append(a)
    else:
        print("No text to redo.")

def display():
    if write_stack:
        print("Current Text: ", end="")
        for i in write_stack:
            print(i, end=" ")
        print()
    else:
        print("No text available to display.")

while True:
    print("\n--- MENU ---")
    print("1. Enter the text")
    print("2. Undo the operation")
    print("3. Redo the operation")
    print("4. Display text")
    print("5. Exit")

    try:
        choice = int(input("Enter the operation to perform: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        changes()
    elif choice == 2:
        undo_operation()
    elif choice == 3:
        redo_operation()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Thank you! Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
