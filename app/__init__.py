import os
import duckdb
from flask import Flask
from flask_cors import CORS
from config import Config
from .api.bill import bill_bp as bill_blueprint
from .api.legislator import legislator_bp as legislator_blueprint
from .api.vote_results import vote_results_bp as vote_results_blueprint
from flask_injector import FlaskInjector
from .injection import AppModule


def init_db(app):
    """Initializes the database and loads data from CSV if tables are empty."""
    db_path = str(app.config['DATABASE_PATH'])
    vote_results_csv = str(app.config['VOTE_RESULTS_CSV'])
    legislators_csv = str(app.config['LEGISLATORS_CSV'])
    bills_csv = str(app.config['BILLS_CSV'])
    votes_csv = str(app.config['VOTES_CSV'])

    try:
        with duckdb.connect(database=db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS vote_result (bill_id INTEGER, legislator_id INTEGER, vote_id INTEGER, vote_type INTEGER)")
            conn.execute("CREATE TABLE IF NOT EXISTS legislator (id INTEGER, name TEXT)")
            conn.execute("CREATE TABLE IF NOT EXISTS bill (id INTEGER, title TEXT, sponsor_id INTEGER)")
            conn.execute("CREATE TABLE IF NOT EXISTS vote (id INTEGER, bill_id INTEGER)")

            
            count = conn.execute("SELECT COUNT(*) FROM vote_result").fetchone()[0]
            if count == 0:
                print(f"Loading data from {vote_results_csv} into vote_result table...")
                conn.execute(f"COPY vote_result FROM '{vote_results_csv}' (HEADER, DELIMITER ',')")
                print("Data loaded into vote_results.")
            else:
                print("vote_results table already contains data.")

            count = conn.execute("SELECT COUNT(*) FROM legislator").fetchone()[0]
            if count == 0:
                print(f"Loading data from {legislators_csv} into legislator table...")
                conn.execute(f"COPY legislator FROM '{legislators_csv}' (HEADER, DELIMITER ',')")
                print("Data loaded into legislator.")
            else:
                print("legislator table already contains data.")

            count = conn.execute("SELECT COUNT(*) FROM bill").fetchone()[0]
            if count == 0:
                print(f"Loading data from {bills_csv} into bill table...")
                conn.execute(f"COPY bill FROM '{bills_csv}' (HEADER, DELIMITER ',')")
                print("Data loaded into bill.")
            else:
                print("bill table already contains data.")  

            count = conn.execute("SELECT COUNT(*) FROM vote").fetchone()[0]
            if count == 0:
                print(f"Loading data from {votes_csv} into vote table...")
                conn.execute(f"COPY vote FROM '{votes_csv}' (HEADER, DELIMITER ',')")
                print("Data loaded into vote.")
            else:
                print("vote table already contains data.")


    except Exception as e:
        print(f"Database initialization failed: {e}")
        raise

def create_app(config_class=Config):
    app = Flask(__name__)

    CORS(app, resources={
        r"/*": {
            "origins": [
                "http://localhost:3000",
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                "http://127.0.0.1:3000"
            ],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "X-API-Key"],
            "supports_credentials": True,
            "expose_headers": ["Content-Type", "X-API-Key"],
            "max_age": 3600
        }
    })
    app.config.from_object(config_class)

    with app.app_context():
        init_db(app)

    app.register_blueprint(bill_blueprint)
    app.register_blueprint(legislator_blueprint)
    app.register_blueprint(vote_results_blueprint)

    FlaskInjector(app=app, modules=[AppModule()])

    @app.route('/')
    def hello_world():
        return 'This is the Quorum-Coding-Challenge-API'

    return app 