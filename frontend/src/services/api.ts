// API service for frontend-backend communication
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

export interface Todo {
  id?: number;
  title: string;
  completed: boolean;
  priority: 'low' | 'medium' | 'high';
  tags?: string | null;
  due_date?: string | null;
  created_at?: string;
  updated_at?: string;
}

export const todoApi = {
  // Get all todos with optional filters
  getTodos: async (params?: {
    completed?: boolean;
    priority?: string;
    search?: string;
    tags?: string;
    sort_by?: string;  // 'priority', 'due_date', 'created_at'
    sort_order?: string;  // 'asc' or 'desc'
    limit?: number;
    offset?: number;
  }): Promise<Todo[]> => {
    const queryParams = new URLSearchParams();
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null) {
          queryParams.append(key, String(value));
        }
      });
    }

    const response = await fetch(`${API_BASE_URL}/api/todos?${queryParams}`);
    if (!response.ok) {
      throw new Error(`Failed to fetch todos: ${response.status}`);
    }
    return response.json();
  },

  // Create a new todo
  createTodo: async (todo: Omit<Todo, 'id'>): Promise<Todo> => {
    const response = await fetch(`${API_BASE_URL}/api/todos`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(todo),
    });

    if (!response.ok) {
      throw new Error(`Failed to create todo: ${response.status}`);
    }
    return response.json();
  },

  // Get a specific todo by ID
  getTodoById: async (id: number): Promise<Todo> => {
    const response = await fetch(`${API_BASE_URL}/api/todos/${id}`);
    if (!response.ok) {
      throw new Error(`Failed to fetch todo: ${response.status}`);
    }
    return response.json();
  },

  // Update a todo
  updateTodo: async (id: number, todo: Partial<Todo>): Promise<Todo> => {
    const response = await fetch(`${API_BASE_URL}/api/todos/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(todo),
    });

    if (!response.ok) {
      throw new Error(`Failed to update todo: ${response.status}`);
    }
    return response.json();
  },

  // Delete a todo
  deleteTodo: async (id: number): Promise<void> => {
    const response = await fetch(`${API_BASE_URL}/api/todos/${id}`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      throw new Error(`Failed to delete todo: ${response.status}`);
    }
  },
};