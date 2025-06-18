## Python packages(PIP):
- `fastapi` - Lightweight API
- `uvicorn` - Web server
- `PyJWT` - JWT tokens
- `python-dotenv` - `.env` support
- `cryptography` - Cryptograghy
- `sqlalchemy` - ORM
- `psycopg2-binary` - PostgreSQL driver
- `pydantic` - Validation schemas
- `` - Alembic

## DB and User creation:
Open PostgreSQL console: \
`psql -U postgres`

```sql
CREATE DATABASE med_booking;
CREATE USER <your_user> WITH PASSWORD '<your_password>';
GRANT ALL PRIVILEGES ON DATABASE med_booking TO <your_user>;
```
To check that DB was successfully and user has all permissions for DB created by command `\l` \
To check that User was successfully created by command `\du`
