from app import create_app
from flask_migrate import upgrade

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        upgrade()  # Выполнение миграций при запуске
    app.run()
