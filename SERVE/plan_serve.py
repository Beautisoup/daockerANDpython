from Main.DAO.tablr_dao import PlanDao
from Main.tablr import PlanModel

plan_dao = PlanDao()
class PlanService:
    def get(self,id):
        return plan_dao.get(id)

    def get_by_name(self,name):
        return plan_dao.get_by_name(name)

    def list(self):
        return plan_dao.list()

    def create(self,plan_model:PlanModel):
        plan = self.get_by_name(plan_model.name)
        if not plan:
            return plan_dao.create(plan_model)
        else:
            return False

    def delete(self,id):
        plan_id = id
        if plan_id:
            plan_dao.delete(plan_id)
        else:
            return False
