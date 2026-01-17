import React, { useState } from 'react';
import { Todo } from '../services/api';

interface TodoFormProps {
  onSubmit: (todo: Omit<Todo, 'id'>) => void;
  initialTodo?: Todo;
  onCancel?: () => void;
}

const TodoForm: React.FC<TodoFormProps> = ({ onSubmit, initialTodo, onCancel }) => {
  const [title, setTitle] = useState(initialTodo?.title || '');
  const [completed, setCompleted] = useState(initialTodo?.completed || false);
  const [priority, setPriority] = useState<'low' | 'medium' | 'high'>(initialTodo?.priority || 'medium');
  const [tags, setTags] = useState(initialTodo?.tags || '');
  const [dueDate, setDueDate] = useState(initialTodo?.due_date || '');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      title,
      completed,
      priority,
      tags: tags || null,
      due_date: dueDate.trim() === '' ? null : dueDate,
    });
  };

  return (
    <form onSubmit={handleSubmit} className="todo-form">
      <div className="form-group">
        <label htmlFor="title">Title:</label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          placeholder="Enter todo title"
        />
      </div>

      <div className="form-group">
        <label>
          <input
            type="checkbox"
            checked={completed}
            onChange={(e) => setCompleted(e.target.checked)}
          />
          Completed
        </label>
      </div>

      <div className="form-group">
        <label htmlFor="priority">Priority:</label>
        <select
          id="priority"
          value={priority}
          onChange={(e) => setPriority(e.target.value as 'low' | 'medium' | 'high')}
        >
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="tags">Tags (comma-separated):</label>
        <input
          type="text"
          id="tags"
          value={tags}
          onChange={(e) => setTags(e.target.value)}
          placeholder="e.g., work, personal"
        />
      </div>

      <div className="form-group">
        <label htmlFor="dueDate">Due Date:</label>
        <input
          type="date"
          id="dueDate"
          value={dueDate}
          onChange={(e) => setDueDate(e.target.value)}
        />
      </div>

      <div className="form-actions">
        <button type="submit">Save Todo</button>
        {onCancel && <button type="button" onClick={onCancel}>Cancel</button>}
      </div>
    </form>
  );
};

export default TodoForm;