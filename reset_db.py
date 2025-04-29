from app import app, db

def reset_db():
    with app.app_context():
        # Recria o banco de dados
        db.drop_all()
        db.create_all()
        print("Banco de dados recriado com sucesso!")

if __name__ == '__main__':
    reset_db()