# Tasks: In-Memory Python Console Todo App (Phase I)

**Input**: Design documents from `/specs/2-in-memory-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup

**Purpose**: Project initialization and basic directory structure.

- [x] T001 Initialize a new Python 3.13 project using `uv init`.
- [x] T002 Create the source directory structure: `src/todo/`.
- [x] T003 Create the test directory structure: `tests/unit/`.
- [x] T004 [P] Create empty initializer files: `src/__init__.py`, `src/todo/__init__.py`, `tests/__init__.py`, `tests/unit/__init__.py`.
- [x] T005 [P] Create empty application files: `src/todo/models.py`, `src/todo/engine.py`, `src/todo/main.py`.
- [x] T006 [P] Create an empty test file: `tests/unit/test_engine.py`.

---

## Phase 2: User Story 1 - Task Creation, Viewing, and Updating (Priority: P1) 🎯 MVP

**Goal**: Enable users to add, view, and edit tasks. This provides the core functionality of the application.

**Independent Test**: Run the application. Use the `add` command to create a task, `view` to see it, `edit` to change it, and verify the output is correct at each step.

### Implementation for User Story 1

- [x] T007 [US1] Define the `Todo` dataclass in `src/todo/models.py` with attributes: `id`, `title`, `is_completed`, and `created_at`.
- [x] T008 [US1] Implement the `TodoManager` class structure in `src/todo/engine.py`, including the in-memory `tasks` list and a counter for task IDs.
- [x] T009 [US1] Implement the `add_task(title: str)` method in `src/todo/engine.py`.
- [x] T010 [US1] Implement the `list_tasks()` method in `src/todo/engine.py`.
- [ ] T011 [US1] Implement the `update_task(task_id: int, new_title: str)` method in `src/todo/engine.py`.
- [ ] T012 [US1] Implement the main REPL (`while True`) loop and basic command parsing in `src/todo/main.py`.
- [ ] T013 [US1] Implement the `add` command handler in `src/todo/main.py` to call the engine.
- [ ] T014 [US1] Implement the `view` command handler in `src/todo/main.py` to call the engine and format the output.
- [ ] T015 [US1] Implement the `edit` command handler in `src/todo/main.py` to call the engine.
- [ ] T016 [US1] Implement the `exit` command handler in `src/todo/main.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 3: User Story 2 - Task Completion (Priority: P2)

**Goal**: Allow users to mark tasks as complete, providing a core part of the workflow.

**Independent Test**: Add a task, then use the `done` command with the task's ID. Viewing the list should show the task with a "Complete" status.

### Implementation for User Story 2

- [ ] T017 [US2] Implement the `mark_complete(task_id: int)` method in `src/todo/engine.py`.
- [ ] T018 [US2] Implement the `done` command handler in `src/todo/main.py` to call the engine.
- [ ] T019 [US2] Enhance the `view` command's output in `src/todo/main.py` to visually distinguish between "Pending" and "Complete" tasks.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 4: User Story 3 - Task Deletion (Priority: P3)

**Goal**: Allow users to remove tasks that are no longer needed.

**Independent Test**: Add a task, then use the `del` command with its ID. Viewing the list should confirm the task is gone.

### Implementation for User Story 3

- [ ] T020 [US3] Implement the `delete_task(task_id: int)` method in `src/todo/engine.py`.
- [ ] T021 [US3] Implement the `del` command handler in `src/todo/main.py` to call the engine.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Finalize the application with error handling and testing.

- [ ] T022 Implement robust error handling in `src/todo/main.py` for invalid commands and non-existent task IDs.
- [ ] T023 [P] Write unit tests in `tests/unit/test_engine.py` to cover all methods in the `TodoManager` class.
- [ ] T024 Add a help command or message in `src/todo/main.py` that lists all available commands.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Must be completed first.
- **User Stories (Phases 2-4)**: Depend on Setup. They should be completed in priority order (US1 -> US2 -> US3) for the clearest development path.
- **Polish (Phase 5)**: Depends on all user stories being complete.

### Implementation Strategy

Follow the phases sequentially:
1.  Complete **Phase 1** to set up the project.
2.  Complete **Phase 2 (US1)** to build the core MVP.
3.  Complete **Phase 3 (US2)** to add completion logic.
4.  Complete **Phase 4 (US3)** to add deletion logic.
5.  Complete **Phase 5** to finalize the application.
