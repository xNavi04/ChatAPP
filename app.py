from config import create_app
from routes import init_routes

app, login_manager, socketio, db = create_app()

init_routes(app, login_manager, socketio, db)

if __name__ == "__main__":
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)