import duckdb
from flask import current_app


class BillRepository:
    _bills = None

    def _get_db_connection(self):
        return duckdb.connect(database=current_app.config['DATABASE_PATH'])
    
    def find_bills(self):
        sql = """
        SELECT b.id, b.title, l.name as sponsor_name , b.sponsor_id FROM bill b 
        LEFT JOIN legislator l ON b.sponsor_id = l.id
        """
        try:    
            with self._get_db_connection() as conn:
                df = conn.execute(sql).fetchdf()
                return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching bills: {e}")
            return []
    
    def find_bill_by_id(self, bill_id: int):
        sql = """
        SELECT b.title, l.name as sponsor_name , b.sponsor_id FROM bill b 
        LEFT JOIN legislator l ON b.sponsor_id = l.id
        WHERE b.id = ?
        """
        try:
            with self._get_db_connection() as conn:
                df = conn.execute(sql, (bill_id,)).fetchdf()
                return df.to_dict(orient='records') 
        except Exception as e:
            print(f"Error fetching bill by id: {e}")
            return []
    
    def find_every_bill_vote_summary(self):
        """
        Retrieves a summary for each bill including sponsor,
        support count, and opposition count.

        I Decided to go in this direction because it is more performative 
        even though it is not as clean as it could be (we could have 3 queries instead of 1
        and have a structured output/json) the trade-off was performance x readability
        """
        sql = """
        SELECT
            b.id AS bill_id,
            b.title AS bill_title,
            COALESCE(l.name, 'No sponsor') AS sponsor_name,
            COUNT(CASE WHEN vr.vote_type = 1 THEN vr.vote_id ELSE NULL END) AS supporters_count,
            COUNT(CASE WHEN vr.vote_type = 2 THEN vr.vote_id ELSE NULL END) AS opponents_count
        FROM
            bill b
        LEFT JOIN vote v ON b.id = v.bill_id
        LEFT JOIN vote_result vr ON v.id = vr.vote_id
        LEFT JOIN legislator l ON b.sponsor_id = l.id
        GROUP BY
            b.id, b.title, sponsor_name
        ORDER BY
            b.title DESC;
        """
        try:
            with self._get_db_connection() as conn:
                df = conn.execute(sql).fetchdf()
                return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching bill vote summary: {e}")
            return []
                

