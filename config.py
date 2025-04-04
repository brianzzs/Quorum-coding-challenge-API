import os
from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / 'data'
    VOTE_RESULTS_CSV = DATA_DIR / 'vote_results.csv'
    LEGISLATORS_CSV = DATA_DIR / 'legislators.csv'
    BILLS_CSV = DATA_DIR / 'bills.csv'
    VOTES_CSV = DATA_DIR / 'votes.csv'
    DATABASE_PATH = DATA_DIR / 'database.db'

    DATA_DIR.mkdir(parents=True, exist_ok=True) 