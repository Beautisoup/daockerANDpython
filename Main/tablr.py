from sqlalchemy import Column, Integer, String

from Serve import Base, engine


class PlanModel(Base):
    __tablename__ = "plan"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)


    def __repr__(self):
        return '<Plan %r>' % self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

if __name__ == '__main__':
    Base.metadata.create_all(engine)