from apps import db

class Users(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.Integer)
    age = db.Column(db.SmallInteger)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(100))
    role = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def is_active(self):
        return True

    def get_id(self):
        return self.id

