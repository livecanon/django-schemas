![rick and morty](./resources/main.png)

## Table of contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Development](#development)
- [Testing](#testing)
- [Credits](#credits)

## Requirements:

- [docker](https://www.docker.com/)

## Setup:

Create and start containers:

```
make start-development
```

Apply migrations:

```
make migrate-development
```

Load fixtures:

```
make loaddata-development
```

Create superuser:

```
make createuser-development
```

### Endpoints:

- `/api/locations/`
- `/api/characters/`
- `/api/episodes/`
- `/api/docs/`

## Development

1. Create and activate the virtual environment
2. Install packages
   ```
   pip install -r requirements-dev.txt
   ```

**NOTE 1.** `core/` is mounted as [bind mount](https://docs.docker.com/storage/bind-mounts/) so we can change the source code and see the changes directly, without having to rebuild the image.

## Testing

In order to run tests locally, you need to have postgres installed locally.

To install posgres, see https://www.postgresql.org/download/

After successful installation, create a user `rick` with password `rick`:

```
psql
CREATE USER <user> WITH PASSWORD '<password>';
ALTER USER <user> WITH SUPERUSER;
```

To run tests, from the `core` folder, run:

```
pytest
```

## Credits

https://rickandmortyapi.com/
