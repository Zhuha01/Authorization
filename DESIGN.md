# Authentication Service

## Overview
This document describes the development and partial implementation of an authentication service. The service provides secure user authentication using traditional email/password as well as Google

## Architecture
- **Framework:** Django + Django REST Framework
- **Authentication:** JWT tokens for stateless authentication
- **Social Login Integration:** Django Allauth for OAuth 2.0 flows
- **Database:** PostgreSQL
- **Containerization:** Docker + Docker Compose

## API Development
| Endpoint | Method | Description |
|-----|--------------|------------|
| `/api/auth/register/` | POST | Register a new user using email/password |
| `/api/auth/login/` | POST | Get JWT tokens using email/password |
| `/api/auth/logout/` | POST | Revoke access token (client-side) |
| `/api/auth/social/google/` | POST | Login or register via Google OAuth |

## Security measures
- Passwords are hashed using Django's built-in secure hashing.
- Social logins use OAuth 2.0 with secure token exchange.
- CSRF protection is enabled for session-based endpoints.
- JWT tokens with short-lived access tokens and refresh tokens.
- Privacy settings are stored in the `.env` file.

## User profile
- Stores: username, email, first name, last name, profile image URL.
- Auto-populates from social provider if available.

## Testing strategy
- Integration tests using `APITestCase`.
- Test cases cover:
- Successful registration and login
- Password mismatch handling
- Login failure with invalid credentials
- Tests are run in isolation.

## Dockerization
- The application is containerized using Docker.
- The Docker Compose file contains the PostgreSQL database service.

## Development Utilities

- Makefile: provides common commands to simplify development workflow, e.g., run server, run tests, build Docker image

- requirements.txt: lists all required Python libraries for the project