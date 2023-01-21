PROJECT = core

# ------------ Development ------------
COMPOSE_DEV='docker-compose.dev.yml'
FIXTURES_PATH='./resources/fixtures'

start-development:
	docker-compose -f ${COMPOSE_DEV} up --build

bash-development:
	docker-compose -f ${COMPOSE_DEV} exec api sh

migrations:
	docker-compose -f ${COMPOSE_DEV} exec api sh -c 'python ./${PROJECT}/manage.py makemigrations'

migrate-development:
	docker-compose -f ${COMPOSE_DEV} exec api sh -c 'python ./${PROJECT}/manage.py migrate'

loaddata-development:
	docker-compose -f ${COMPOSE_DEV} cp ./resources/characters/. api:/vol/static_data/media/characters
	docker-compose -f ${COMPOSE_DEV} exec api sh -c 'python ./${PROJECT}/manage.py loaddata ${FIXTURES_PATH}/location.json'
	docker-compose -f ${COMPOSE_DEV} exec api sh -c 'python ./${PROJECT}/manage.py loaddata ${FIXTURES_PATH}/character.json'
	docker-compose -f ${COMPOSE_DEV} exec api sh -c 'python ./${PROJECT}/manage.py loaddata ${FIXTURES_PATH}/episode.json'

createuser-development:
	docker-compose -f ${COMPOSE_DEV} exec api sh -c 'python ./${PROJECT}/manage.py createsuperuser'

# ------------ Production ------------
COMPOSE_PROD='docker-compose.prod.yml'

start-production:
	docker-compose -f ${COMPOSE_PROD} up --build

migrate-production:
	docker-compose -f ${COMPOSE_PROD} exec api sh -c 'python ./${PROJECT}/manage.py migrate'

createuser-production:
	docker-compose -f ${COMPOSE_PROD} exec api sh -c 'python ./${PROJECT}/manage.py createsuperuser'
