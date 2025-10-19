## Requirements
- Python 3.10+
- Docker and Docker Compose
- PostgreSQL

## Configuration

1. Clone the repository:
```
git clone <repo_url>
cd <repo_folder>
```
2. Create an .env file with the necessary environment variables (see .env.example):
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```
3. Install Python dependencies:
```
pip install -r requirements.txt
```
## Makefile commands

`Makefile` provides convenient commands for managing a Django project Locally and with Docker:

| Command | Description |
|----------------|---------------------------------------------------------------------|
| `make build` | Build Docker images using `docker-compose build`. |
| ``make up'' | Run the application and PostgreSQL in a detached mode (`docker-compose up -d`). |
| `make down' | Stop and remove containers (`docker-compose down'). |
| `make logs` | Monitor container logs for a web service (`docker-compose logs -f web`). |
| `make migrate' | Run Django migrations inside a web container (`docker-compose exec web python manage.py migrate`). |
| `make test' | Run integration tests in a temporary container (`docker-compose run --rm test`). |
| `make fresh-start' | Stop and remove all containers and volumes, rebuild images, start containers, wait 10 seconds, and run migrations. |
| `make superuser' | Create a Django superuser inside the web container (`docker-compose exec web python manage.py createsuperuser`). |

## Start the project
- Using Python (local development):
```
python manage.py migrate
python manage.py runserver
```
- Using Docker Compose:
```
docker-compose up --build
```
## API Endpoints
| Endpoint | Method | Description |
|----------------------------|----------|------------------------------------|
| /api/auth/register/ | POST | Register a new user (email/password) |
| /api/auth/login/ | POST | Log in with email/password |
| /api/auth/logout/ | POST | Logout from the client side using JWT |
| /api/auth/social/google/ | POST | Login or register via Google OAuth |

## Tests

Tests cover:
- Successful and failed user registration (password mismatch, duplicate email)
- Successful and failed user registration (incorrect password)
- Tests are run in isolation using `APITestCase`
