from models import User, Room, Message
from datetime import datetime

class ChatRoom:
    def __init__(self, db, client_id, current_user):
        self.db = db
        self.current_user = current_user
        self.host = None
        self.room = None
        self.client_id = client_id

    def get_host_and_room(self):
        self.host = self.db.get_or_404(User, self.client_id)
        self.room = self.db.session.execute(self.db.select(Room)
                                  .where(Room.participants.contains(self.current_user),
                                         Room.participants.contains(self.host))).scalar()


    def add_chat_room(self):
        current_user = self.db.get_or_404(User, self.current_user.id)
        host = self.db.get_or_404(User, self.host.id)
        self.room = Room(participants=[current_user, host])
        self.db.session.add(self.room)
        self.db.session.commit()


    def add_message(self, request, socketio):
        x = request.form["xmsg"]
        date = datetime.now()
        room = self.db.get_or_404(Room, self.room.id)
        current_user = self.db.get_or_404(User, self.current_user.id)
        message = Message(room=room,
                          sender=current_user,
                          text=x,
                          date=date)
        self.db.session.add(message)
        self.db.session.commit()
        socketio.emit("chat", {"hostID": str(current_user.id), "clientID": str(self.client_id)}, broadcast=True)

