from flask_script import Manager, Server
from app import create_app

app = create_app('development')
app.debug = True

manager = Manager(app)
manager.add_command('run', Server)

if __name__ == "__main__":
    manager.run()
