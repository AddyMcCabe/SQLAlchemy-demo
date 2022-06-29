# CREATE ENTRIES INTO TABLES
from models import db, Viking, Weapon, Pet

# CREATE 2 VIKINGS
thorfinn = Viking('Thorfinn')
thorkell = Viking('Thorkell')

# ADD VIKINGS TO DB
db.session.add_all([thorfinn, thorkell])
db.session.commit()

# CHECK !
print(Viking.query.all())

thorfinn = Viking.query.filter_by(name='Thorfinn').first()
print(thorfinn)

# CREATE PET OBJECT
ketlingr = Pet('Ketlingr', thorfinn.id)

# GIVE THORFINN SOME WEAPONS
weapon1 = Weapon('Dagger', thorfinn.id)
weapon2 = Weapon('Shield', thorfinn.id)

db.session.add_all([ketlingr, weapon1, weapon2])
db.session.commit()

# GRAB THORFINN AFTER CONDITIONS
thorfinn = Viking.query.filter_by(name='Thorfinn').first()
print(thorfinn)

print(thorfinn.report_weapons())

