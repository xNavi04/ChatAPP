from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

user_rooms = db.Table("user_rooms",
                      db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                      db.Column("room_id", db.Integer, db.ForeignKey("rooms.id"), primary_key=True))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    image = db.Column(db.String)
    image_mimetype = db.Column(db.String)
    messages = db.relationship("Message", back_populates="sender")


class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    messages = db.relationship("Message", back_populates="room")
    participants = db.relationship("User", secondary=user_rooms, backref=db.backref("users", lazy="dynamic"))


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))
    text = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    room = db.relationship("Room", back_populates="messages")
    sender = db.relationship("User", back_populates="messages")