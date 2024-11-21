from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from models import Room, Message, User
from base64 import b64encode
from werkzeug.security import generate_password_hash, check_password_hash
from activity.login import login_in
from activity.register import register_user
from activity.rooms import Rooms
from activity.chat_room import ChatRoom
from activity.adding_user import AddUser
from activity.edit_profile import Profile

def init_routes(app, login_manager, socketio, db):
    @login_manager.user_loader
    def load_user(user_id):
        return db.get_or_404(User, user_id)
    @socketio.on("connect")
    def handle_connect():
        print("Client connected!")
    @socketio.on("user_join")
    def handle_user_join(username):
        print(f"User {username} joined!")
    @app.route("/")
    def index_page():
        content = {
            "current_user": current_user
        }
        template = "home.html"
        return render_template(template, **content)
    @app.route("/chat")
    def find_chat_page():
        rooms_class = Rooms()
        rooms = rooms_class.get_rooms(db=db, current_user_id=current_user.id)
        content = {
            "current_user": current_user,
            "rooms": rooms,
            "b64encode": b64encode
        }
        template = "chat.html"
        return render_template(template, **content)

    @app.route('/get_content/<int:num>')
    def get_content(num):
        room = db.get_or_404(Room, num)
        content = {
            "current_user": current_user,
            "room": db.get_or_404(Room, num),
            "host": db.session.execute(db.select(User).where(User != current_user, User.users.contains(room))).scalar(),
            "b64encode": b64encode
        }
        template = "content.html"
        return render_template(template, **content)
    @app.route("/chat/<int:num>", methods=["POST", "GET"])
    @login_required
    def chat_page(num):
        if current_user.id == num:
            return abort(404)

        chat_page_class = ChatRoom(db, num, current_user)

        chat_page_class.get_host_and_room()

        if not chat_page_class.room:
            chat_page_class.add_chat_room()

        if request.method == "POST":
            chat_page_class.add_message(request, socketio)

        context = {
            "host": chat_page_class.host,
            "current_user": current_user,
            "room": chat_page_class.room,
            "b64encode": b64encode,
            "socketio": socketio
        }
        template = "chatRoom.html"
        return render_template(template, **context)
    @app.route("/login", methods=["POST", "GET"])
    def login_page():
        alert = ""
        if request.method == "POST":
            x, y = login_in(request, login_user, check_password_hash, db)
            if x == 1:
                alert = y
            else:
                return redirect(url_for("index_page"))
        content = {
            "logged_in": current_user.is_authenticated,
            "alert": alert,
            "current_user": current_user
        }
        template = "login.html"
        return render_template(template, **content)
    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("login_page"))
    @app.route("/deleteMessage/<int:num>/<int:kar>/<int:kal>", methods=["POST", "GET"])
    def delete_message(num, kar, kal):
        db.session.delete(db.get_or_404(Message, num))
        db.session.commit()
        host_id = str(kar)
        client_id = str(kal)
        socketio.emit("chat", {"hostID": host_id, "clientID": client_id})
        return redirect(request.referrer)
    @app.route("/deleteRoom/<int:num>")
    def delete_room(num):
        room = db.session.execute(db.select(Room).where(Room.participants.contains(current_user),
                                                        Room.participants.contains(db.get_or_404(User, num)))).scalar()
        messages = db.session.execute(db.select(Message).where(Message.room == room)).scalars().all()
        for message in messages:
            db.session.delete(message)
        db.session.commit()
        if room:
            db.session.delete(room)
            db.session.commit()
        return redirect(url_for("find_chat_page"))
    @app.route("/addUser", methods=["GET", "POST"])
    def add_user_page():
        adding_user = AddUser(request, db, current_user)
        if request.method == "POST":
            adding_user.adding_user()
        content = {
            "alerts": adding_user.alert,
            "current_user": current_user
        }
        template = "findUser.html"
        return render_template(template, **content)
    @app.route("/editProfile", methods=["GET", "POST"])
    @login_required
    def edit_profile_page():
        edit_profile = Profile(db, request, current_user)
        if request.method == "POST":
            edit_profile.invoke_edit_profile()
            return redirect(url_for("index_page"))

        content = {
            "username": current_user.name,
            "code": current_user.code,
            "alerts": edit_profile.alerts,
            "current_user": current_user
        }
        template = "edit.html"
        return render_template(template, **content)
    @app.route("/register", methods=["POST", "GET"])
    def register():
        alerts = []
        if request.method == "POST":
            x, y = register_user(request, db, alerts, login_user, generate_password_hash)
            if x == 1:
                alerts = y
            else:
                return redirect(url_for("index_page"))
        content = {
            "alerts": alerts,
            "current_user": current_user,
        }
        template = "register.html"
        return render_template(template, **content)
