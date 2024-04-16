from faker import Faker
import pytest

fake = Faker()
a = fake.email()
a = a.split('@')[1]
print(a)

