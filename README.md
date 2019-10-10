# Docker Composed Redis Server and Redis Client
This repo includes a basic docker compose environment for creating a Redis server and client containers. The client
container ships with the redis-cli and can access the redis server (i.e. `redis-cli -h redis_server`). There's also a demo python script which can be accessed from within the Redis client container to make Redis server calls.

## Why would I want to use this?
Not everyone has a Redis server and ready-to-go local environment for querying a Redis server (redis-cli, Pyhon redis packages, etc.). It can be useful to test various redis commands quickly in a local environment.

## Example use cases
* Analyzing the server performance of various Redis commands with large data sets (test with `docker stats`).
* Playing with various Redis commands in a local environment.
* Testing Python scripts that make Redis API calls.
* Use this repo as a starter Docker compose application that leverages Redis.

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

# redis-cli -h redis_server
```

## Running a python script in the Redis client container against the Redis server
```
docker-compose run redis_client python redis_client.py create_keys
```
