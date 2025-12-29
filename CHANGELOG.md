# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/)
et ce projet suit le versionnement sémantique.

---

## [0.1.0] - 2025-01-XX

### Added
- Complete CRUD API for tasks (Create, Read, Update, Delete)
- Task endpoints:
  - GET /tasks/
  - POST /tasks/
  - GET /tasks/{id}
  - PUT /tasks/{id}
  - DELETE /tasks/{id}
  - DELETE /tasks/
- Request/response validation with Pydantic
- Automatic API documentation with Swagger UI and ReDoc
- Unit tests with pytest and FastAPI TestClient
- In-memory storage for tasks (fake database)

### Changed
- Project structure improved (routes, schemas, tests)
- Renamed endpoints from generic items to tasks for clarity

### Notes
- This is the first stable version of the API.
- Future versions will introduce database persistence and authentication.
