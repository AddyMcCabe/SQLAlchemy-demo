from tokenize import maybe
from base import db, Puppy

# CREATE
my_puppy = Puppy('Thor', 1)
db.session.add(my_puppy)
db.session.commit()

# READ
all_puppies = Puppy.query.all()
print(all_puppies)

# SELECT BY ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# FILTERS
puppy_binx = Puppy.query.filter_by(name='Binx')
print(puppy_binx.all())

# //////////// UPDATE

first_puppy = Puppy.query.get(1)
first_puppy.age = 4
db.session.add(first_puppy)
db.session.commit()
print(puppy_one)

# /////////// DELETE
third_puppy = Puppy.query.get(2)
db.session.delete(third_puppy)
db.session.commit()

all_pups = Puppy.query.all()
print(all_pups)

