import redis
from faker import Faker
from uuid import uuid4

r = redis.Redis(host='redis', port=6379, db=0)
fake = Faker()

MAPPINGS = 10

def s1():
    r.set("name", "jason")

def s2():
    result = r.get("name")
    print(result)

def set_multiple():
    for i in range(10):
        key = fake.name()
        val = fake.name()
        print(key, val)
        r.set(key, val)

def set_zincrby():
    for i in range(MAPPINGS):
        name, value, amount = 'class2', str(uuid4()), 1
        print(name, value, amount)
        # Increment the score of ``value`` in sorted set ``name`` by ``amount``
        r.zincrby(name=name, value=value, amount=amount)

def main():
    set_zincrby()

if __name__ == '__main__':
    main()
