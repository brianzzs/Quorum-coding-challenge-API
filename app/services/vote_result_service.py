from app.repositories.vote_result_repository import VoteResultRepository
from injector import inject

class VoteResultService:
    @inject
    def __init__(self, repo: VoteResultRepository):
        self.vote_result_repository = repo

    def get_vote_results(self):
        return self.vote_result_repository.get_vote_results()

    def get_vote_result_by_bill_id(self, bill_id):
        return self.vote_result_repository.get_vote_result_by_bill_id(bill_id)
    


