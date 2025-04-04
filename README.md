# Quorum Coding Challenge API

This project is a Flask API to serve data related to legislators, bills, and votes, based on the provided CSV files.

## Prerequisites

*   Python 3.8+
*   pip (Python package installer)
*   Node.js and npm (for the UI (folder quorum-coding-challenge-ui))

## API Setup

1.  **Might not be needed, but if you can't run this via python run.py, you should create a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the API

1.  **Start the Flask development server:**
    ```bash
    python run.py
    ```
    The API will typically be available at `http://127.0.0.1:5000`. The database will be initialized automatically on the first run using the CSV files in the `data/` directory.

## UI Setup & Running

1.  **Navigate to the UI project directory:**
    The UI project repository can be found here: [Quorum Coding Challenge UI](https://github.com/brianzzs/Quorum-coding-challenge-ui)

    ```bash
    cd ../quorum-coding-challenge-ui
    ```

3.  **Install Node dependencies:**
    ```bash
    npm install
    ```

4.  **Start the UI development server:**
    ```bash
    npm run dev
    ```
    The UI should then be accessible in your browser, likely at `http://localhost:3000` or `http://localhost:5173` (check the terminal output). The UI will interact with the running API.

## API Endpoints

The following endpoints are available:
I put in the folder a Insomnia collection where you can test the endpoints as well.

*   `GET /bill/`: Get all bills with sponsor information.
*   `GET /bill/id/<int:bill_id>`: Get a specific bill by its ID.
*   `GET /bill/vote-summary`: Get a summary of votes (support/oppose counts) for every bill.
*   `GET /legislator/`: Get all legislators.
*   `GET /legislator/id/<int:legislator_id>`: Get a specific legislator by ID.
*   `GET /legislator/id/<int:legislator_id>/bills-supported`: Get the count of bills supported by a specific legislator.
*   `GET /legislator/id/<int:legislator_id>/bills-opposed`: Get the count of bills opposed by a specific legislator.
*   `GET /vote_results/`: Get all vote results, including legislator and bill names.
*   `GET /vote_results/bill/<int:bill_id>`: Get vote results for a specific bill ID. 
