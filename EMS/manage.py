from flask.cli import FlaskGroup
from EMS import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
