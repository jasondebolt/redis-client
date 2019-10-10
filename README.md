# Docker Composed Redis Server and Redis Client

## Building the containers (running only Redis server container)
```
docker-compose up
```

## Running the Redis client container shell
```
docker-compose run redis_client /bin/bash
```

## Connecting to the Redis-CLI on the Redis client container
```
docker-compose run redis_client /bin/bash
bash-4.2# redis-cli -h redis_server
```

## Running a python script in the Redis client container against the Redis server
```
docker-compose run redis_client python redis_client.py
```
