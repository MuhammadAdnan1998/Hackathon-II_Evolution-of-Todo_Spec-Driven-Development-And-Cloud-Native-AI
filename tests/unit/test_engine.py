import unittest
import sys
import os

# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from todo.engine import TodoManager
from todo.models import Todo

class TestTodoManager(unittest.TestCase):

    def setUp(self):
        """Set up a new TodoManager for each test."""
        self.manager = TodoManager()

    def test_add_task(self):
        """Test adding a task."""
        self.assertEqual(len(self.manager.list_tasks()), 0)
        task = self.manager.add_task("Test Task")
        self.assertIsInstance(task, Todo)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(len(self.manager.list_tasks()), 1)
        self.assertEqual(self.manager.list_tasks()[0], task)

    def test_list_tasks(self):
        """Test listing tasks."""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_update_task(self):
        """Test updating a task."""
        task = self.manager.add_task("Original Title")
        updated_task = self.manager.update_task(task.id, "New Title")
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(self.manager.list_tasks()[0].title, "New Title")

    def test_update_nonexistent_task(self):
        """Test updating a non-existent task."""
        updated_task = self.manager.update_task(999, "New Title")
        self.assertIsNone(updated_task)

    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = self.manager.add_task("Test Task")
        self.assertFalse(task.is_completed)
        completed_task = self.manager.mark_complete(task.id)
        self.assertIsNotNone(completed_task)
        self.assertTrue(completed_task.is_completed)
        self.assertTrue(self.manager.list_tasks()[0].is_completed)

    def test_mark_nonexistent_task_complete(self):
        """Test marking a non-existent task as complete."""
        completed_task = self.manager.mark_complete(999)
        self.assertIsNone(completed_task)

    def test_delete_task(self):
        """Test deleting a task."""
        task = self.manager.add_task("Test Task")
        self.assertEqual(len(self.manager.list_tasks()), 1)
        result = self.manager.delete_task(task.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.list_tasks()), 0)

    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task."""
        result = self.manager.delete_task(999)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
