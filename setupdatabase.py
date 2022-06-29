from base import db, Puppy

# creates all the tables model --. db table
db.create_all()

binx = Puppy('Binx', 3)
almond = Puppy('Almond', 2)


db.session.add_all([binx, almond])

db.session.commit()

print(binx.id)
print(almond.id)

