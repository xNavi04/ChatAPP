from models import User

class Profile:
    def __init__(self, db, request, current_user):
        self.username = None
        self.code = None
        self.image = None
        self.alerts = []
        self.db = db
        self.current_user = current_user
        self.request = request

    def insert_username_code_and_image(self):
        self.username = self.request.form["username"]
        self.code = self.request.form["code"]
        self.image = self.request.files["image"]

    def invoke_update_image(self):
        self.current_user.image = self.image.read()
        self.current_user.image_mimetype = self.image.mimetype
        self.db.session.commit()

    def invoke_edit_profile(self):
        self.insert_username_code_and_image()
        if self.db.session.execute(self.db.select(User).where(User.code == self.code, User.id != self.current_user.id)).scalar():
            self.alerts.append("Ten kod jest aktualnie zajęty!")
        elif self.username and self.code:
            self.current_user.name = self.username
            self.current_user.code = self.code
            if self.image:
                self.invoke_update_image()
            self.db.session.commit()
        else:
            self.alerts.append("Coś jest puste!")

