from app.repositories.legislator_repository import LegislatorRepository
from injector import inject

class LegislatorService:
    @inject
    def __init__(self, repo: LegislatorRepository):
        self.legislator_repository = repo

    def get_legislators(self):
        return self.legislator_repository.find_legislators()

    def get_legislator_by_id(self, legislator_id: int):
        return self.legislator_repository.find_legislator_by_id(legislator_id)

    def get_count_bills_supported_by_legislator(self, legislator_id: int):
        return self.legislator_repository.count_bills_supported_by_legislator(legislator_id)
    
    def get_count_bills_opposed_by_legislator(self, legislator_id: int):
        return self.legislator_repository.count_bills_opposed_by_legislator(legislator_id)

    def get_every_legislator_supported_bills(self):
        return self.legislator_repository.find_every_legislator_supported_bills()

    def get_every_legislator_opposed_bills(self):
        return self.legislator_repository.find_every_legislator_opposed_bills()


