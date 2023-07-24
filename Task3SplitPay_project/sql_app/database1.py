from sqlalchemy import create_engine
from urllib.parse import quote  
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:%s@localhost:3306/task3splitpay1'  #'mysql+mysqlconnector://user_name:password@localhost:3306/database' 

engine = create_engine(SQLALCHEMY_DATABASE_URL % quote('yypa4146'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()