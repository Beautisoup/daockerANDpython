from Serve import db_session
from Main.tablr import PlanModel


class PlanDao:
    def get(self, plan_id) -> PlanModel:
        return db_session.query(PlanModel).filter(id = plan_id).first()
    def get_by_name(self, plan_name) -> PlanModel:
        return db_session.query(PlanModel).filter(PlanModel == plan_name).first()

    def list(self):
        # 返回所有数据
        return db_session.query(PlanModel).all()

    def create(self, plan_do: PlanModel):
        # 新增数据
        db_session.add(plan_do)
        db_session.commit()
        return plan_do.id

    def delete(self, plan_id):
        # 删除操作
        db_session.query(PlanModel).filter_by(id=plan_id).delete()
        db_session.commit()
        return plan_id