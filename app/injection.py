from injector import Module, singleton
from .repositories.vote_result_repository import VoteResultRepository
from .services.vote_result_service import VoteResultService
from .repositories.legislator_repository import LegislatorRepository
from .services.legislator_service import LegislatorService
from .repositories.bill_repository import BillRepository
from .services.bill_service import BillService

class AppModule(Module):
    def configure(self, binder):
        binder.bind(VoteResultRepository, to=VoteResultRepository, scope=singleton)
        binder.bind(LegislatorRepository, to=LegislatorRepository, scope=singleton)
        binder.bind(VoteResultService, to=VoteResultService, scope=singleton)
        binder.bind(LegislatorService, to=LegislatorService, scope=singleton)
        binder.bind(BillRepository, to=BillRepository, scope=singleton)
        binder.bind(BillService, to=BillService, scope=singleton)