from models import User

def login_in(request, login_user, check_password_hash, db):
    name = request.form["username"]
    password = request.form["password"]
    user = db.session.execute(db.Select(User).where(User.name == name)).scalar()
    if name == "" or password == "":
        alert = "Something is empty!"
    elif not user:
        alert = "This user is not exist!"
    elif check_password_hash(user.password, password):
        login_user(user)
        return 0, None
    else:
        alert = "Wrong password"
    return 1, alert
