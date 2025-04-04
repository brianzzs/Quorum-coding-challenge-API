from app.repositories.bill_repository import BillRepository
from injector import inject

class BillService:
    @inject
    def __init__(self, repo: BillRepository):
        self.bill_repository = repo

    def get_bills(self):
        return self.bill_repository.find_bills()
    
    def get_every_bill_vote_summary(self):
        return self.bill_repository.find_every_bill_vote_summary()
    
    def get_bill_by_id(self, bill_id: int):
        return self.bill_repository.find_bill_by_id(bill_id)
    

    def get_count_of_supporters_by_id(self, bill_id: int):
        return self.bill_repository.find_count_of_supporters_by_id(bill_id)
    
    def get_count_of_opponents_by_id(self, bill_id: int):
        return self.bill_repository.find_count_of_opponents_by_id(bill_id)
    
    def get_primary_sponsor_by_id(self, bill_id: int):
        return self.bill_repository.find_primary_sponsor_by_id(bill_id)
    
    
