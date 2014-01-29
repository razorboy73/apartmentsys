from sqlalchemy import Column, Integer, String

class User(Object):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User(?,?,?)>".format(self.name, self.fullname, self.password)