"""
Unit tests for CLI Task Manager
"""

import json
import os
import unittest

# Patch the TASKS_FILE before importing the module
import task_manager
task_manager.TASKS_FILE = "test_tasks.json"

from task_manager import (
    load_tasks, save_tasks, add_task,
    list_tasks, complete_task, delete_task
)

TEST_FILE = "test_tasks.json"


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Reset test file before each test."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        task_manager.TASKS_FILE = TEST_FILE

    def tearDown(self):
        """Clean up test file after each test."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_load_tasks_empty(self):
        tasks = load_tasks()
        self.assertEqual(tasks, [])

    def test_add_task_default_priority(self):
        add_task("Test task")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test task")
        self.assertEqual(tasks[0]["priority"], "medium")
        self.assertFalse(tasks[0]["completed"])

    def test_add_task_high_priority(self):
        add_task("Urgent task", "high")
        tasks = load_tasks()
        self.assertEqual(tasks[0]["priority"], "high")

    def test_add_multiple_tasks(self):
        add_task("Task 1")
        add_task("Task 2")
        add_task("Task 3")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 3)

    def test_complete_task(self):
        add_task("Complete me")
        complete_task(1)
        tasks = load_tasks()
        self.assertTrue(tasks[0]["completed"])

    def test_complete_nonexistent_task(self):
        # Should not raise; just prints a message
        complete_task(999)

    def test_delete_task(self):
        add_task("Delete me")
        delete_task(1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_delete_nonexistent_task(self):
        # Should not raise; just prints a message
        delete_task(999)

    def test_save_and_load_tasks(self):
        sample = [{"id": 1, "title": "Test", "priority": "low",
                   "completed": False, "created_at": "2025-01-01 10:00"}]
        save_tasks(sample)
        loaded = load_tasks()
        self.assertEqual(loaded, sample)


if __name__ == "__main__":
    unittest.main()
