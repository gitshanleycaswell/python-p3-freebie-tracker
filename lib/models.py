from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from freebietracker import *


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def __repr__(self):
        return f'<Company {self.name}>'
    
    freebies = relationship('Freebie', cascade = 'all, delete-orphan')
    
    devs = association_proxy('freebies', 'dev')

    def give_freebie(self, item_name, value, dev):
        new_freebie = Freebie(item_name=item_name, value = value, company_id=self.id, dev_id = dev.id)
        session.add(new_freebie)
        session.commit()

    @classmethod
    def oldest_company(cls):
        oldest_company = session.query(cls).order_by(cls.founding_year).first()
        return oldest_company
    
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'
    
    freebies = relationship('Freebie', cascade = 'all, delete-orphan')

    companies = association_proxy('freebies', 'company')

    
    def received_one(self, item_name):
        if any(freebie.item_name == item_name for freebie in self.freebies):
            return True
        else:
            return False
        
    def give_away(self, dev, check_freebie):
        if check_freebie in self.freebies:
            check_freebie.dev = dev
            session.commit()
            
            
    
class Freebie(Base):
    __tablename__= 'freebies'

    id = Column(Integer(), primary_key = True)
    item_name = Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    dev = relationship('Dev', back_populates = 'freebies')
    company = relationship('Company', back_populates = 'freebies')

    def __repr__(self):
        return f'<{self.item_name}>'

    def print_details(self):
        print(f"{self.dev.name} owns a {self.item_name} from {self.company.name}")