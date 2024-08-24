from app import create_app
from database import db, User, Usuario

def init_db():
    db.connect()
    db.create_tables([User, Usuario])

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
