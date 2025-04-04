import duckdb
from flask import current_app


class VoteResultRepository:
    _vote_results = None

    def _get_db_connection(self):
        db_path = str(current_app.config['DATABASE_PATH'])
        return duckdb.connect(database=db_path, read_only=False)

    def get_vote_results(self):
        sql = """
        SELECT b.title as bill_title, l.name as legislator_name, 
        case when vr.vote_type = 1 then 'Yea' 
        when vr.vote_type = 2 then 'Nay' 
        end as vote_type, v.id as vote_id
        FROM vote_result vr
        INNER JOIN vote v ON v.id = vr.vote_id
        INNER JOIN bill b ON b.id = v.bill_id
        INNER JOIN legislator l ON l.id = vr.legislator_id
        ;"""
        try:
            with self._get_db_connection() as conn:
                df = conn.execute(sql).fetchdf()
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching vote results: {e}")
            return [] 

    def get_vote_result_by_bill_id(self, bill_id):
        sql = """
        SELECT b.title as bill_title, l.name as legislator_name, 
        case when vr.vote_type = 1 then 'Yea' 
        when vr.vote_type = 2 then 'Nay' 
        end as vote_type, v.id as vote_id
        FROM vote_result vr
        INNER JOIN vote v ON v.id = vr.vote_id
        INNER JOIN bill b ON b.id = v.bill_id
        INNER JOIN legislator l ON l.id = vr.legislator_id
        WHERE v.bill_id = ?;"""
        try:
            with self._get_db_connection() as conn:
                df = conn.execute(sql, [int(bill_id)]).fetchdf()
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching vote results by bill_id: {e}")
            return []