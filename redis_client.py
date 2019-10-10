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

MAPPINGS = 1000

def _get_rand_string(n):
    return ''.join(choice(ascii_lowercase) for i in range(n))


def create_keys():
    for i in range(MAPPINGS):
        name = 'class.{0}::person.{1}'.format(_get_rand_string(35), _get_rand_string(35))
        value = randint(0, 100)
        #print(name, value, amount)
        # Increment the score of ``value`` in sorted set ``name`` by ``amount``
        r.set(name=name, value=value)


def create_sorted_set():
    for i in range(MAPPINGS):
        name = 'class2'
        value = 'class.{0}::person.{1}'.format(_get_rand_string(35), _get_rand_string(35))
        amount = randint(0, 100)
        #print(name, value, amount)
        # Increment the score of ``value`` in sorted set ``name`` by ``amount``
        r.zincrby(name=name, value=value, amount=amount)


def delete_sorted_set():
    i = 0
    while r.zcard('class2') > 0:
        print('Deleting 100 members (page {0})'.format(i))
        r.zremrangebyrank('class2', 0, 99)
        time.sleep(1)
        i += 1


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
