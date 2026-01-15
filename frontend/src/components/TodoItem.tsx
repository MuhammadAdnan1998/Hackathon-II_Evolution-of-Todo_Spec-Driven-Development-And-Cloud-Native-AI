import React from 'react';
import { Todo } from '../services/api';

interface TodoItemProps {
  todo: Todo;
  onToggle: (todo: Todo) => void;
  onDelete: (id: number) => void;
  onEdit: (todo: Todo) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete, onEdit }) => {
  const handleToggle = () => {
    onToggle({ ...todo, completed: !todo.completed });
  };

  const handleDelete = () => {
    onDelete(todo.id!);
  };

  const handleEdit = () => {
    onEdit(todo);
  };

  // Format the due date for display
  const formatDate = (dateString: string | null) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString();
  };

  // Determine priority class for styling
  const priorityClass = `priority-${todo.priority}`;

  return (
    <div className={`todo-item ${todo.completed ? 'completed' : ''}`}>
      <div className="todo-content">
        <div className="todo-header">
          <input
            type="checkbox"
            checked={todo.completed}
            onChange={handleToggle}
            className="todo-checkbox"
          />
          <span className={`todo-title ${todo.completed ? 'completed-text' : ''}`}>
            {todo.title}
          </span>
          <span className={`todo-priority ${priorityClass}`}>{todo.priority}</span>
        </div>

        {todo.due_date && (
          <div className="todo-meta">
            <span>Due: {formatDate(todo.due_date)}</span>
          </div>
        )}

        {todo.tags && (
          <div className="todo-tags">
            {todo.tags.split(',').map((tag, index) => (
              <span key={index} className="tag">{tag.trim()}</span>
            ))}
          </div>
        )}
      </div>

      <div className="todo-actions">
        <button onClick={handleEdit} className="edit-btn">Edit</button>
        <button onClick={handleDelete} className="delete-btn">Delete</button>
      </div>
    </div>
  );
};

export default TodoItem;