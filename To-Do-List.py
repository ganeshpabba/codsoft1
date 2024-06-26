def main():
    tasks = []
    while True:
        print("\n======# To-Do-List #======")
        print("1. Add task")
        print("2. Show Tasks")
        print("3. Mark Task as done")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print()
            n_tasks = int(input("how many task you want to add: "))

            for i in range(n_tasks):
                task = input("enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task addded!")

        elif choice == "2":
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "done" if task["done"] else "not done"
                print(f"{index+1}. {task['task']}-{status}")

        elif choice == "3":
            task_index = int(input("enter the task number yo mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("task marked as done!")
            else:
                print("invalid task number.")

        elif choice == "4":
            print("exiting the to-do-list.")
            break

        else:
            print("invalid choice. please try again ")


if __name__ == "__main__":
    main()
