import redis
import sys
from faker import Faker
from uuid import uuid4
from random import choice, randint
from string import ascii_lowercase
import time

USAGE_DOCSTRING = """
python redis_client.py [create_sorted_set | create_keys | delete_sorted_set]
"""

r = redis.Redis(host='redis_server', port=6379, db=0)
fake = Faker()

MAPPINGS = 1000000
MIN_RANK = 0
MAX_RANK = 9
SLEEP_SECONDS = 1
SORTED_SET_NAME = 'foobar'

def _get_rand_string(n):
    return ''.join(choice(ascii_lowercase) for i in range(n))


def create_keys():
    for i in range(MAPPINGS):
        name = 'test1.{0}::field1.{1}'.format(_get_rand_string(35), _get_rand_string(35))
        value = randint(0, 100)
        #print(name, value, amount)
        # Increment the score of ``value`` in sorted set ``name`` by ``amount``
        r.set(name=name, value=value)


def create_sorted_set():
    for i in range(MAPPINGS):
        name = SORTED_SET_NAME
        value = 'test1.{0}::field1.{1}'.format(_get_rand_string(35), _get_rand_string(35))
        amount = randint(0, 100)
        #print(name, value, amount)
        # Increment the score of ``value`` in sorted set ``name`` by ``amount``
        r.zincrby(name=name, value=value, amount=amount)


def delete_sorted_set():
    i = 0
    sum = 0
    rank_range = MAX_RANK - MIN_RANK + 1
    zcard_value = r.zcard(SORTED_SET_NAME)
    hourly_rate = (rank_range/SLEEP_SECONDS) * 3600
    while zcard_value > 0:
        hours_remaining = zcard_value / float(hourly_rate)
        print('Deleting {0} members ({1} deleted, {2} hours remaining) (page {3})'.format(rank_range, sum, hours_remaining, i))
        r.zremrangebyrank(SORTED_SET_NAME, MIN_RANK, MAX_RANK)
        time.sleep(SLEEP_SECONDS)
        i += 1
        sum += rank_range
        zcard_value = r.zcard(SORTED_SET_NAME)


def db_size():
    print(r.dbsize())


def main():
    if len(sys.argv) < 2:
        print(USAGE_DOCSTRING)
        raise SystemExit()

    mode = sys.argv[1]
    if mode == 'create_sorted_set':
        print('Creating sorted set...')
        create_sorted_set()
    elif mode == 'delete_sorted_set':
        print('Deleting sorted set...')
        delete_sorted_set()
    elif mode == 'create_keys':
        print('Creating keys...')
        create_keys()
    elif mode == 'db_size':
        print('Displaying DB size')
        db_size()

if __name__ == '__main__':
    main()
