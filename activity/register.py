from models import User
import random


"""
Sprawdza, czy w formularzu wszystkie wymagane pola zostały wypełnione.
Zwraca True, jeśli którekolwiek pole jest puste.
"""
def is_form_data_invalid(username, password):
    return not username or not password

"""
Sprawdza, czy hasło i potwierdzenie hasła są takie same.
Zwraca True, jeśli hasła się różnią.
"""
def do_passwords_match(password, confirm_password):
    return password == confirm_password

"""
Sprawdza, czy użytkownik istnieje w bazie na podstawie e-maila lub nazwy użytkownika.
Zwraca użytkownika, jeśli taki istnieje.
"""
def user_exists(db, username):
    user_by_username = db.session.execute(db.select(User).where(User.name == username)).scalar()
    return user_by_username

"""
Tworzy nowego użytkownika i zapisuje go w bazie danych.
"""
def create_new_user(db, username, password, generate_password_hash):
    hash_password = generate_password_hash(password, salt_length=8)
    new_user = User(name=username,
                    password=hash_password,
                    code=generate_user_tag(db))

    db.session.add(new_user)

    db.session.commit()
    print("Juz")
    return new_user

"""
Główna funkcja do rejestracji użytkownika, która zarządza walidacją i dodawaniem użytkownika do bazy danych.
"""
def register_user(request, db, alerts, login_user, generate_password_hash):
    print("start")
    # Pobranie danych z formularza
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirmPassword", "")

    # Walidacja danych z formularza
    if user_exists(db, username):
        alerts.append("Ten użytkownik już istnieje lub nazwa jest zajęta!")
    elif not do_passwords_match(password, confirm_password):
        alerts.append("Hasła nie są takie same!")
    elif is_form_data_invalid(username, password):
        alerts.append("Niektóre pola są puste!")
    else:
        # Tworzenie i logowanie nowego użytkownika
        new_user = create_new_user(db, username, password, generate_password_hash)
        login_user(new_user)
        return 0, []
    return 1, alerts

def generate_user_tag(db):
    # Keep generating tags until a unique one is found
    for i in range(99999):
        tag = random.randint(0, 9999)  # Generate a random 4-digit number
        tag_str = f"{tag:04d}"         # Format it as a 4-digit string (e.g., 0001, 0423, etc.)
        if not db.session.execute(db.select(User).where(User.code == tag_str)).scalar():  # Check if it's unique
            return tag_str



