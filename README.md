# URL Shortener

A URL Shortener is a backend service that converts long, complex URLs into short, easy-to-share links. When a user accesses the shortened URL, the service looks up the corresponding original URL and redirects the user to it.

This project is built using **FastAPI, SQLAlchemy, SQLite, Redis, and JWT authentication**.

### Key Features

* **URL shortening** — Generates a unique short code for a long URL.
* **Custom aliases** — Allows users to optionally create a custom short alias.
* **URL expiration** — Supports expiry dates for shortened URLs.
* **User authentication** — Uses JWT-based authentication for protected APIs.
* **Password security** — Stores passwords as secure hashes rather than plaintext.
* **URL ownership** — Associates shortened URLs with the authenticated user who created them.
* **Redis caching** — Caches frequently accessed short URLs to reduce database queries and improve redirect performance.
* **Fast redirects** — Resolves a short code to its original URL and redirects the client.
* **SQLite persistence** — Uses SQLite as the primary database for storing users and URLs.

### System Flow

```text
User
 │
 ▼
FastAPI
 │
 ├── Authentication ──► JWT
 │
 ├── Create Short URL ──► SQLite
 │
 └── Redirect
       │
       ▼
     Redis
       │
    ┌──┴───┐
    │      │
   HIT    MISS
    │      │
    │      ▼
    │    SQLite
    │      │
    │      ▼
    │    Redis
    │      │
    └──┬───┘
       ▼
 Original URL
```

### Technology Stack

| Component         | Technology        |
| ----------------- | ----------------- |
| Backend           | FastAPI           |
| ORM               | SQLAlchemy        |
| Database          | SQLite            |
| Cache             | Redis             |
| Authentication    | JWT               |
| Password Hashing  | Argon2            |
| API Documentation | Swagger / OpenAPI |

The project demonstrates the fundamentals of building a production-style backend service, including REST API design, authentication, database modeling, caching, URL resolution, and separation of routing, business logic, and persistence layers.
