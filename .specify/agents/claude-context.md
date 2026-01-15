# Claude Agent Context: Full-Stack Todo Web Application

## Technologies Added

### Frontend Technologies
- **Next.js 14+**: React-based framework for production-grade applications
- **TypeScript**: Strongly typed programming language that builds on JavaScript
- **React Hooks**: Mechanism for managing state and side effects in functional components
- **CSS Modules/Styled Components**: Styling solutions for component-scoped styles

### Backend Technologies
- **FastAPI 0.100+**: Modern, fast web framework for building APIs with Python
- **Python 3.11+**: High-level programming language for backend development
- **Pydantic**: Data validation and settings management using Python type hints
- **SQLModel**: SQL databases with Python, combining SQLAlchemy and Pydantic

### Database Technologies
- **SQLModel**: Combines SQLAlchemy and Pydantic for type-safe database interactions
- **PostgreSQL**: Powerful, open-source object-relational database system
- **Neon**: Serverless PostgreSQL, providing auto-scaling and branching capabilities
- **SQLAlchemy**: SQL toolkit and object relational mapper for Python

### API and Communication
- **REST API**: Architectural style for designing networked applications
- **OpenAPI**: Specification for building APIs with documentation
- **JSON**: Standard data interchange format for API communication
- **HTTP Methods**: Standardized request methods (GET, POST, PUT, DELETE)

### Development and Deployment
- **Environment Variables**: Configuration management for different deployment environments
- **Twelve-Factor App Methodology**: Best practices for building software-as-a-service apps
- **CORS**: Cross-Origin Resource Sharing for secure API communication
- **Dependency Management**: Proper handling of project dependencies

## Key Implementation Notes

### Architecture Patterns
- **Separation of Concerns**: Clear distinction between frontend, backend, and database layers
- **Modular Design**: Components and modules designed to be independent and reusable
- **API-First Design**: Backend provides well-defined APIs consumed by frontend
- **State Management**: Proper handling of application state on both frontend and backend

### Data Model Considerations
- **Todo Entity**: Core entity with id, title, completion status, priority, tags, and due date
- **Validation Rules**: Client and server-side validation for data integrity
- **Relationships**: Designed for potential expansion with user and tag relationships
- **Timestamps**: Automatic creation and update timestamps for audit trails

### API Design Principles
- **RESTful Endpoints**: Standardized URL patterns and HTTP methods
- **Consistent Responses**: Predictable response formats for all API calls
- **Error Handling**: Standardized error response format with appropriate status codes
- **Filtering and Pagination**: Support for querying subsets of data efficiently

## Constraints and Guidelines

### Development Constraints
- All code must be generated from specifications (no manual coding)
- Maintain compatibility with Phase I architecture where possible
- Follow PEP 8 for Python and modern JavaScript/TypeScript standards
- Use environment variables for configuration management

### Quality Standards
- Implement comprehensive error handling
- Include proper input validation
- Follow security best practices
- Maintain responsive design for mobile compatibility