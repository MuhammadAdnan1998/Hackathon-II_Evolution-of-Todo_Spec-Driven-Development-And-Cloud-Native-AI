# Implementation Plan: In-Memory Python Console Todo App (Phase I)

**Branch**: `2-in-memory-todo-app` | **Date**: 2026-01-03 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/2-in-memory-todo-app/spec.md`

## 1. Scope and Dependencies

-   **In Scope**: A command-line interface (CLI) application for managing todo tasks. All CRUD (Create, Read, Update, Delete) operations are supported. Task state is managed entirely in-memory for the duration of a single application session.
-   **Out of Scope**: Persistent storage (database, file-based), multi-user support, graphical user interface (GUI), and network connectivity are explicitly excluded in Phase I.
-   **External Dependencies**: The project will be built with Python 3.13+ and managed using `uv`. The only external dependency considered is `rich` for enhanced terminal UI, which is optional.

## 2. Key Decisions and Rationale

-   **Architectural Pattern**: A simplified Controller-Service-Repository pattern (Controller/Engine/Model) is chosen to establish a modular and testable codebase. This separation of concerns will facilitate scalability into Phase II, where persistence and potentially other features will be introduced.
-   **Data Storage**: A simple Python `list` within a manager class will be used for in-memory storage. This approach is the simplest possible solution that meets the Phase I constraint of no persistent storage.
-   **CLI Interaction Model**: A `while True` Read-Eval-Print Loop (REPL) will be used to handle user commands. This avoids external dependencies (like `click` or `argparse`) and is sufficient for the simple command structure required.

## 3. Interfaces and API Contracts (CLI Commands)

The CLI serves as the user-facing API. The following commands will be supported:

-   **`add <title>`**:
    -   **Input**: A string `title` for the new task.
    -   **Output**: Confirmation message, e.g., `Success: Added task "Buy milk"`.
-   **`view`**:
    -   **Input**: None.
    -   **Output**: A formatted list of all tasks with their ID, title, and status.
-   **`done <id>`**:
    -   **Input**: The integer `id` of the task to mark as complete.
    -   **Output**: Confirmation message, e.g., `Success: Task 1 marked as complete`.
-   **`edit <id> <new_title>`**:
    -   **Input**: The integer `id` of the task and the new string `new_title`.
    -   **Output**: Confirmation message, e.g., `Success: Task 1 updated`.
-   **`del <id>`**:
    -   **Input**: The integer `id` of the task to delete.
    -   **Output**: Confirmation message, e.g., `Success: Task 1 deleted`.
-   **`exit`**:
    -   **Input**: None.
    -   **Output**: A farewell message before terminating the application.
-   **Error Handling**: Invalid commands or incorrect arguments (e.g., non-existent ID) will result in clear, user-friendly error messages.

## 4. Non-Functional Requirements (NFRs)

-   **Performance**: All operations must feel instantaneous to the user, with responses appearing immediately after a command is entered.
-   **Reliability**: The application must handle invalid inputs gracefully (e.g., `del 99` when no such ID exists) without crashing.
-   **Usability**: The CLI output must be clearly formatted and easy to read.

## 5. Data Management

-   **Source of Truth**: The `tasks: list[Todo]` attribute within the `TodoManager` class is the single source of truth.
-   **Schema**: A `Todo` data class will be defined in `models.py` with the attributes: `id: int`, `title: str`, `is_completed: bool`, `created_at: datetime`.
-   **Data Lifecycle**: All data is ephemeral and will be lost when the application session ends.

## 6. Operational Readiness

-   **Observability**: Application state changes and errors will be communicated to the user via clear `print` statements to the console.
-   **Deployment**: The application will be run directly from the source code via `python src/todo/main.py`. No complex deployment is required for this phase.

## 7. Risk Analysis and Mitigation

-   **Primary Risk**: Accidental data loss due to the in-memory nature of the application (e.g., closing the terminal).
-   **Mitigation**: This is an accepted constraint of Phase I. The application's ephemeral nature will be clearly communicated.

## 8. Evaluation and Validation

-   **Definition of Done**: The feature is complete when all CLI commands (add, view, done, edit, del, exit) are implemented correctly and function as described in the specification. The application must pass all automated and manual checks for functionality and error handling.

## Project Structure

### Source Code

```text
src/
└── todo/
    ├── __init__.py
    ├── models.py      # Contains the Todo data class schema.
    ├── engine.py      # Core logic: TodoManager class for all CRUD operations.
    └── main.py        # CLI entry point: REPL, command parsing, and calls to the engine.

tests/
├── __init__.py
└── unit/
    ├── __init__.py
    ├── test_engine.py # Unit tests for the TodoManager class.
```

**Structure Decision**: A simple, single-project structure is adopted. The `src/todo/` directory encapsulates the application logic, separating concerns into models, business logic (engine), and the user interface (main). This modular approach aligns with the goal of future scalability.
