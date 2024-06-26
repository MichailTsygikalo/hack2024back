from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, DECIMAL,DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String(255), nullable=False)
    pswd = Column(String(255), nullable=False)
    status = Column(Boolean, nullable=False)
    balance_money = Column(Integer, nullable=False, default=30000)
    balance_bonus = Column(Integer, nullable=False, default=1000)
    #people = relationship("People", back_populates="user")

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    surname = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    sec_name = Column(String(255))
    birthday = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='cascade'), nullable=False)
    photo = Column(String(255))
    
    #user = relationship("User", back_populates="people")
    #pasport = relationship("Pasport", back_populates="people")

class Pasport(Base):
    __tablename__ = 'pasport'

    id = Column(Integer, primary_key=True)
    series = Column(String(4), nullable=False)
    number = Column(String(6), nullable=False, unique=True)
    registration_id = Column(Integer, ForeignKey('registration.id', ondelete='cascade'), )
    people_id = Column(Integer, ForeignKey('people.id', ondelete='cascade'), )
    date_issue = Column(Date, nullable=False)
    
    #people = relationship("People", back_populates="pasport")

class Registration(Base):
    __tablename__ = 'registration'

    id = Column(Integer, primary_key=True)
    city = Column(String(255), nullable=False)
    streat = Column(String(255))
    home = Column(String)
    flat = Column(String)
    x = Column(String)
    y = Column(String)
    #pasport = relationship("Pasport", back_populates="registration")

class Doc(Base):
    __tablename__ = 'doc'

    id = Column(Integer, primary_key=True)
    polis = Column(String(16))
    snils = Column(String(14))
    people_id = Column(Integer, ForeignKey('people.id', ondelete='cascade'), nullable=False)
    pasport_id = Column(Integer, ForeignKey('pasport.id', ondelete='cascade'), nullable=False)
    #people = relationship("People", back_populates="doc")
    #pasport = relationship("Pasport", back_populates="doc")

class Benefit(Base):       
    __tablename__ = 'benefit'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    doc_id = Column(Integer, ForeignKey('doc.id', ondelete='cascade'), nullable=False)
    #doc = relationship("Doc", back_populates="benefit")

class Discount(Base):
    __tablename__ = 'discount'

    id = Column(Integer, primary_key=True)
    percent = Column(Integer, nullable=False)
    benefit_id = Column(Integer, ForeignKey('benefit.id', ondelete='cascade'), nullable=False)
    contractor_id = Column(Integer, ForeignKey('contractor.id', ondelete='cascade'), nullable=False)

class Contractor(Base):
    __tablename__ = 'contractor'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='cascade'),)
    registration_id = Column(Integer, ForeignKey('registration.id', ondelete='cascade'),)
    photo = Column(String(255))
    
class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    contractor_id = Column(Integer, ForeignKey('contractor.id', ondelete='cascade'),)
    price = Column(DECIMAL, default=0)

    
class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id', ondelete='cascade'),)
    service_id = Column(Integer, ForeignKey('service.id', ondelete='cascade'),)
    sum = Column(DECIMAL, default=0)
    count = Column(Integer, default=0)
    date = Column(DATETIME)

    
