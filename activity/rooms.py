from models import Room, User

class Rooms:
    @staticmethod
    def sorted_room(rooms):
        room_m = []
        room_nm = []
        for room in rooms:
            if len(room.messages) > 0:
                room_m.append(room)
            else:
                room_nm.append(room)
        rooms = []
        if room_m:
            rooms = sorted(room_m, key=lambda messages: messages.messages[0].date, reverse=True)
        for r in room_nm:
            rooms.append(r)
        return rooms
    def get_rooms(self, db, current_user_id):
        current_user = db.get_or_404(User, current_user_id)
        rooms = db.session.execute(db.select(Room).where(Room.participants.contains(current_user))).scalars().all()
        rooms = self.sorted_room(rooms)
        return rooms