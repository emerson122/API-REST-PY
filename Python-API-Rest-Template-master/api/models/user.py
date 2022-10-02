from api import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    lastname = db.Column(db.String(64))
    hash = db.Column(db.String(128))
    salt = db.Column(db.String(128))

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "lastname": self.lastname,
            "hash": self.hash.hex() if type(self.hash) == bytes else self.hash,
            "salt": self.salt.hex() if type(self.salt) == bytes else self.salt
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)
