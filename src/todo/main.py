from .engine import TodoManager

def print_help():
    """Prints the help message."""
    print("\nAvailable Commands:")
    print("  add <title>      - Add a new task")
    print("  view             - View all tasks")
    print("  edit <id> <new>  - Edit a task's title")
    print("  done <id>        - Mark a task as complete")
    print("  del <id>         - Delete a task")
    print("  help             - Show this help message")
    print("  exit             - Exit the application\n")

def main():
    """Main function to run the To-do application CLI."""
    manager = TodoManager()
    print("Welcome to your To-do List! Type 'help' for commands.")


    while True:
        command_line = input("> ").strip()
        if not command_line:
            continue

        parts = command_line.split(maxsplit=1)
        command = parts[0].lower()
        args_str = parts[1] if len(parts) > 1 else ""

        if command == "add":
            if not args_str:
                print("Error: The 'add' command requires a title.")
            else:
                task = manager.add_task(args_str)
                print(f"Success: Added task \"{task.title}\" with ID {task.id}.")

        elif command == "view":
            tasks = manager.list_tasks()
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("--- Your To-do List ---")
                for task in tasks:
                    status = "Complete" if task.is_completed else "Pending"
                    print(f"  {task.id}. {task.title} [{status}]")
                print("-----------------------")

        elif command == "edit":
            try:
                task_id_str, new_title = args_str.split(maxsplit=1)
                task_id = int(task_id_str)
                task = manager.update_task(task_id, new_title)
                if task:
                    print(f"Success: Task {task_id} updated.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Error: 'edit' requires a task ID and a new title.")
                print("Usage: edit <id> <new_title>")

        elif command == "done":
            try:
                task_id = int(args_str)
                task = manager.mark_complete(task_id)
                if task:
                    print(f"Success: Task {task_id} marked as complete.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Error: 'done' requires a valid task ID.")
                print("Usage: done <id>")

        elif command == "del":
            try:
                task_id = int(args_str)
                if manager.delete_task(task_id):
                    print(f"Success: Task {task_id} deleted.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Error: 'del' requires a valid task ID.")
                print("Usage: del <id>")

        elif command == "help":
            print_help()

        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
