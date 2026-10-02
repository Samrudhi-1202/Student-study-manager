tasks = []

while True:
    print("\n===== STUDENT STUDY MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            subject = input("Enter subject: ")
            task = input("Enter task: ")
            deadline = input("Enter deadline: ")

            tasks.append({
                "subject": subject,
                "task": task,
                "deadline": deadline,
                "completed": False
            })

            print("Task added successfully!")

        case "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("\n===== YOUR TASKS =====")

                for i, t in enumerate(tasks, 1):
                    if t["completed"]:
                        status = "Completed"
                    else:
                        status = "Pending"

                    print(i, "-", t["subject"])
                    print("   Task     :", t["task"])
                    print("   Deadline :", t["deadline"])
                    print("   Status   :", status)

        case "3":
            if not tasks:
                print("No tasks available.")
            else:
                print("\n===== SELECT TASK =====")

                for i, t in enumerate(tasks, 1):
                    print(i, "-", t["task"])

                number = input("Enter task number: ")

                if number.isdigit():
                    number = int(number)

                    if 1 <= number <= len(tasks):
                        tasks[number - 1]["completed"] = True
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a number.")

        case "4":
            if not tasks:
                print("No tasks available.")
            else:
                print("\n===== SELECT TASK =====")

                for i, t in enumerate(tasks, 1):
                    print(i, "-", t["task"])

                number = input("Enter task number to delete: ")

                if number.isdigit():
                    number = int(number)

                    if 1 <= number <= len(tasks):
                        tasks.pop(number - 1)
                        print("Task deleted successfully!")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a number.")

        case "5":
            print("Thank you for using Student Study Manager!")
            break

        case _:
            print("Invalid choice. Please enter 1 to 5.")