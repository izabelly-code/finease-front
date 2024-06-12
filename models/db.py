from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
instance = "mysql+pymysql://root:@localhost:3306/pjbl_exp_criativa"
#instance = "mysql+pymysql://[user]:[password]@localhost:3306/[db_name]"
#instance = "sqlite:///pjbl_exp_criativa"
