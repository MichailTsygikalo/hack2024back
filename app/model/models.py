from sqlalchemy import Integer, MetaData, String, Table, Column, Boolean, Date, ForeignKey, CheckConstraint, DECIMAL

metadata = MetaData()

user = Table(
    'user',
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('login', String(255), nullable=False, unique=True), 
    Column('pswd', String(255), nullable=False),
    Column('status', Boolean, nullable=False),
    Column('balance_money',Integer,CheckConstraint('balance_money >= 0'), nullable= False, default=30000, ),
    Column('balance_bonus',Integer,CheckConstraint('balance_bonus >= 0'), nullable= False, default=1000),
)

people = Table(
    'people',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('surname', String(255), nullable=False),
    Column('name', String(255), nullable=False),
    Column('sec_name', String(255)),
    Column('birthday', Date, nullable= False),
    Column('user_id',Integer, ForeignKey('user.id', ondelete='cascade'),nullable = False, unique=True),
    Column('photo', String(255),),
)

pasport = Table(
    'pasport',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('series', String(4),nullable= False),
    Column('number', String(6),nullable= False, unique=True),
    Column('registration_id',Integer, ForeignKey('registration.id', ondelete='cascade')),
    Column('people_id',Integer, ForeignKey('people.id', ondelete='cascade')),
    Column('date_issue', Date, nullable= False),
)

registration = Table(
    'registration',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('city', String(255),nullable= False),
    Column('streat', String(255)),
    Column('home',String),
    Column('flat', String),
    Column('x',String),
    Column('y', String),
)

doc = Table(
    'doc',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('polis', String(16)),
    Column('snils', String(14)),
    Column('people_id',Integer, ForeignKey('people.id', ondelete='cascade'),nullable = False),
    Column('pasport_id',Integer, ForeignKey('pasport.id', ondelete='cascade'),nullable = False),
)

benefit = Table(
    'benefit',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255),nullable= False),
    Column('doc_id',Integer, ForeignKey('doc.id', ondelete='cascade'),nullable = False),
)

discount = Table(
    'discount',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('percent',Integer,nullable= False),
    Column('benefit_id',Integer, ForeignKey('benefit.id', ondelete='cascade'),nullable = False),
    Column('contractor_id',Integer, ForeignKey('contractor.id', ondelete='cascade'),nullable = False),
)

contractor = Table(
   'contractor',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name',String(255),nullable= False, unique=True), 
    Column('user_id',Integer, ForeignKey('user.id', ondelete='cascade'),nullable = False, unique=True),
    Column('registration_id',Integer, ForeignKey('registration.id', ondelete='cascade')),
    Column('photo',String(255)), 
)

service = Table(
   'service',
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('name',String(255),nullable= False,), 
    Column('contractor_id',Integer, ForeignKey('contractor.id', ondelete='cascade'),nullable = False,),
    Column('price',DECIMAL, default=0),   
)

sales = Table(
    'sales',
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('people_id',Integer, ForeignKey('people.id', ondelete='cascade'),nullable = False,), 
    Column('service_id',Integer, ForeignKey('service.id', ondelete='cascade'),nullable = False,),
    Column('sum',DECIMAL, default=0),
    Column('count',Integer, default=0),
)
