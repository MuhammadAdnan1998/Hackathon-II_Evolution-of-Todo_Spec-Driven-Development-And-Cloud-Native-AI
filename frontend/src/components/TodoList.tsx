import React, { useState, useEffect } from 'react';
import TodoItem from './TodoItem';
import { Todo, todoApi } from '../services/api';

interface TodoListProps {
  onEdit: (todo: Todo) => void;
}

const TodoList: React.FC<TodoListProps> = ({ onEdit }) => {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [completedFilter, setCompletedFilter] = useState<boolean | null>(null);
  const [priorityFilter, setPriorityFilter] = useState<string>('');
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [tagFilter, setTagFilter] = useState<string>('');
  const [sortBy, setSortBy] = useState<string>('');
  const [sortOrder, setSortOrder] = useState<string>('asc');

  useEffect(() => {
    fetchTodos();
  }, [completedFilter, priorityFilter, searchTerm, tagFilter, sortBy, sortOrder]);

  const fetchTodos = async () => {
    try {
      setLoading(true);
      const fetchedTodos = await todoApi.getTodos({
        completed: completedFilter,
        priority: priorityFilter || undefined,
        search: searchTerm || undefined,
        tags: tagFilter || undefined,
        sort_by: sortBy || undefined,
        sort_order: sortOrder || undefined
      });
      setTodos(fetchedTodos);
      setError(null);
    } catch (err) {
      setError('Failed to fetch todos');
      console.error('Error fetching todos:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleToggle = async (todo: Todo) => {
    try {
      const updatedTodo = await todoApi.updateTodo(todo.id!, { ...todo, completed: !todo.completed });
      setTodos(todos.map(t => t.id === updatedTodo.id ? updatedTodo : t));
    } catch (err) {
      setError('Failed to update todo');
      console.error('Error updating todo:', err);
    }
  };

  const handleDelete = async (id: number) => {
    try {
      await todoApi.deleteTodo(id);
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (err) {
      setError('Failed to delete todo');
      console.error('Error deleting todo:', err);
    }
  };

  const handleFilterChange = () => {
    fetchTodos();
  };

  if (loading) {
    return <div className="loading">Loading todos...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="todo-list">
      <div className="filters">
        <div className="filter-group">
          <label htmlFor="completed-filter">Status:</label>
          <select
            id="completed-filter"
            value={completedFilter === null ? '' : completedFilter ? 'completed' : 'pending'}
            onChange={(e) => {
              if (e.target.value === '') {
                setCompletedFilter(null);
              } else {
                setCompletedFilter(e.target.value === 'completed');
              }
            }}
          >
            <option value="">All</option>
            <option value="pending">Pending</option>
            <option value="completed">Completed</option>
          </select>
        </div>

        <div className="filter-group">
          <label htmlFor="priority-filter">Priority:</label>
          <select
            id="priority-filter"
            value={priorityFilter}
            onChange={(e) => setPriorityFilter(e.target.value)}
          >
            <option value="">All</option>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
        </div>

        <div className="filter-group">
          <label htmlFor="search">Search:</label>
          <input
            type="text"
            id="search"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search by title..."
          />
        </div>

        <div className="filter-group">
          <label htmlFor="tag-filter">Tag:</label>
          <input
            type="text"
            id="tag-filter"
            value={tagFilter}
            onChange={(e) => setTagFilter(e.target.value)}
            placeholder="Filter by tag..."
          />
        </div>

        <div className="filter-group">
          <label htmlFor="sort-by">Sort by:</label>
          <select
            id="sort-by"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
          >
            <option value="">None</option>
            <option value="priority">Priority</option>
            <option value="due_date">Due Date</option>
            <option value="created_at">Created Date</option>
          </select>
        </div>

        <div className="filter-group">
          <label htmlFor="sort-order">Order:</label>
          <select
            id="sort-order"
            value={sortOrder}
            onChange={(e) => setSortOrder(e.target.value)}
          >
            <option value="asc">Ascending</option>
            <option value="desc">Descending</option>
          </select>
        </div>
      </div>

      {todos.length === 0 ? (
        <div className="no-todos">No todos found</div>
      ) : (
        <div className="todos-container">
          {todos.map(todo => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onToggle={handleToggle}
              onDelete={handleDelete}
              onEdit={onEdit}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default TodoList;