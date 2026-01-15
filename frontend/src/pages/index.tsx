import React, { useState } from 'react';
import TodoForm from '../components/TodoForm';
import TodoList from '../components/TodoList';
import { Todo, todoApi } from '../services/api';

const HomePage: React.FC = () => {
  const [editingTodo, setEditingTodo] = useState<Todo | null>(null);
  const [showForm, setShowForm] = useState(false);

  const handleSubmit = async (todoData: Omit<Todo, 'id'>) => {
    try {
      if (editingTodo) {
        // Update existing todo
        const updatedTodo = await todoApi.updateTodo(editingTodo.id!, {
          ...todoData,
          id: editingTodo.id
        });
        // In a real app, we would update the list, but for now just refresh
        setEditingTodo(null);
        setShowForm(false);
      } else {
        // Create new todo
        await todoApi.createTodo(todoData);
        setShowForm(false);
      }
    } catch (err) {
      console.error('Error saving todo:', err);
      alert('Failed to save todo');
    }
  };

  const handleEdit = (todo: Todo) => {
    setEditingTodo(todo);
    setShowForm(true);
  };

  const handleCancel = () => {
    setEditingTodo(null);
    setShowForm(false);
  };

  return (
    <div className="todo-app">
      <header className="todo-header">
        <h1>Todo App</h1>
        <button
          className="add-todo-btn"
          onClick={() => {
            setEditingTodo(null);
            setShowForm(true);
          }}
        >
          Add Todo
        </button>
      </header>

      <main className="todo-main">
        {showForm ? (
          <div className="todo-form-container">
            <h2>{editingTodo ? 'Edit Todo' : 'Create New Todo'}</h2>
            <TodoForm
              onSubmit={handleSubmit}
              initialTodo={editingTodo || undefined}
              onCancel={handleCancel}
            />
            <button onClick={handleCancel} className="cancel-btn">
              Cancel
            </button>
          </div>
        ) : (
          <div className="todo-list-container">
            <TodoList onEdit={handleEdit} />
          </div>
        )}
      </main>
    </div>
  );
};

export default HomePage;