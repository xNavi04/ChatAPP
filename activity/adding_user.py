from models import User, Room

class AddUser:
    def __init__(self, request, db, current_user):
     self.request = request
     self.db = db
     self.current_user = current_user
     self.user = None
     self.code = None
     self.room = None
     self.alert = []

    def insert_user_and_code(self):
        username = self.request.form["username"]
        self.code = self.request.form["code"]
        self.user = self.db.session.execute(
                self.db.select(User).where(User.name == username, User.code == self.code, User.id != self.current_user.id)).scalar()

    def find_room_with_current_user_and_user(self):
        self.room = self.db.session.execute(self.db.select(Room).where(Room.participants.contains(self.user), Room.participants.contains(self.current_user))).scalar()

    def adding_user(self):
        self.insert_user_and_code()
        if not self.user:
            self.alert.append("Złe dane!")
        else:
            self.find_room_with_current_user_and_user()
            if not self.room:
                current_user = self.db.get_or_404(User, self.current_user.id)
                user = self.db.get_or_404(User, self.user.id)
                self.db.session.add(Room(participants=[current_user, user]))
                self.db.session.commit()
                self.alert.append("Dodano!")
            else:
                self.alert.append("Już go dodałes wczesniej!")
        return self.alert