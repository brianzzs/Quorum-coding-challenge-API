import os 
import duckdb
from flask import current_app


class LegislatorRepository:
    _legislators = None
    
    def _get_db_connection(self):
        db_path = str(current_app.config['DATABASE_PATH'])
        return duckdb.connect(database=db_path)
    
    def find_legislators(self):
        sql = "SELECT * FROM legislator;"
        try:
            with self._get_db_connection() as conn:
                df = conn.execute(sql).fetchdf()
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching legislators: {e}")
            return []
            
    
    def find_legislator_by_id(self, legislator_id: int):
        sql = "SELECT * FROM legislator WHERE id = ?"
        try:
            with self._get_db_connection() as conn:
                df = conn.execute(sql, (legislator_id,)).fetchdf()
                print(df)
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching legislator by id: {e}")
            return []
        
    def count_bills_supported_by_legislator(self, legislator_id: int):
        sql = """
        SELECT COUNT(*) as amount, b.title as bill_title FROM vote_result vr 
        INNER JOIN vote v ON v.id = vr.vote_id
        INNER JOIN bill b ON b.id = v.bill_id
        WHERE vr.legislator_id = ? AND vr.vote_type = 1
        GROUP BY b.title
        """
        try:
            with self._get_db_connection() as conn:
                df = conn.execute(sql, (legislator_id,)).fetchdf()
                return df.to_dict(orient='records') 
        except Exception as e:
            print(f"Error fetching how many bills legislator supported: {e}")
            return []
        
    def count_bills_opposed_by_legislator(self, legislator_id: int):
        sql = """
        SELECT COUNT(*) as amount, b.title as bill_title FROM vote_result vr 
        INNER JOIN vote v ON v.id = vr.vote_id
        INNER JOIN bill b ON b.id = v.bill_id
        WHERE vr.legislator_id = ? AND vr.vote_type = 2
        GROUP BY b.title
        """
        try:
            with self._get_db_connection() as conn:
                df = conn.execute(sql, (legislator_id,)).fetchdf()
                return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching how many bills legislator opposed: {e}")
            return []
    
    


