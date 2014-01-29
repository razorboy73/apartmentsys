from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, and_, or_, func
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

Base = declarative_base()
engine = create_engine('sqlite:///:test.db', echo = True)
Session = sessionmaker(bind=engine)
session = Session()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(70))
    fullname = Column(String(70))
    password = Column(String(70))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


print User.__table__
print User.__mapper__
Base.metadata.create_all(engine)

ed_user = User("Ed","Ed Jones","Swingline")

session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
print "our_user", our_user

print ed_user
print ed_user.name
print ed_user.fullname
print ed_user.password
print ed_user.id

session.add_all([
    User("wendy","Wendy williams","foobar"),
    User('mary', 'Mary Contrary', 'xxg527'),
    User('fred', 'Fred Flinstone', 'blah')
])


ed_user.password="123"

print ed_user.password
print session.new

session.commit()

for x in session.query(User):
    print x.id, x.fullname


ed_user.name = "JimJohn"

print ed_user.name

fake_user = User("fake", "Ima faker", "234")

session.add(fake_user)

print session.query(User).filter(User.name.in_(["JimJohn", "fake"])).all()

session.rollback()

print 'rolled back', ed_user.name

print fake_user in session

print "after roll back", session.query(User).filter(User.name.in_(["JimJohn", "fake"])).all()

for instance in session.query(User).order_by(User.id):
    print instance.name, instance.id, instance.fullname

for name, fullname in session.query(User.name, User.fullname):
    print name, fullname

for row in session.query(User, User.name).all():
    print row.User

print "renaming columns"
for row in session.query(User.name.label('sexy_rexy')).all():
    print(row.sexy_rexy)

for name, in session.query(User.name).\
        filter_by(fullname = "Ed Jones"):
    print name

print "Python style"
for name in session.query(User).\
        filter(User.fullname == "Ed Jones"):
    print name




query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
#print query.all()
#print query.first()

#try:
#    user = query.one()
#except MultipleResultsFound, e:
#    print e

try:
    user=query.filter(User.id ==99).one()
except NoResultFound, e:
    print e

for user in session.query(User).\
    filter("id<3").\
    order_by("id").all():
    print user.name

q = session.query(User.id, User.name)
print q.order_by("name").all()
f = session.query(User).count()
print "there are: ", f

print session.query(func.count('*')).select_from(User).scalar()

print session.query(func.count(User.id)).scalar()