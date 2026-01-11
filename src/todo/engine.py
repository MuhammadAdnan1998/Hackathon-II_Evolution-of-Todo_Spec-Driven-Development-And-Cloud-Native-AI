from .models import Todo
from typing import Optional, List

class TodoManager:
    def __init__(self):
        self.tasks: List[Todo] = []
        self._next_task_id: int = 1

    def add_task(self, title: str) -> Todo:
        """Adds a new task to the list."""
        task = Todo(id=self._next_task_id, title=title)
        self.tasks.append(task)
        self._next_task_id += 1
        return task

    def list_tasks(self) -> List[Todo]:
        """Lists all tasks."""
        return self.tasks

    def _find_task_by_id(self, task_id: int) -> Optional[Todo]:
        """Finds a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, new_title: str) -> Optional[Todo]:
        """Updates a task's title."""
        task = self._find_task_by_id(task_id)
        if task:
            task.title = new_title
            return task
        return None

    def mark_complete(self, task_id: int) -> Optional[Todo]:
        """Marks a task as complete."""
        task = self._find_task_by_id(task_id)
        if task:
            task.is_completed = True
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task."""
        task = self._find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
