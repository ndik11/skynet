
class DatabaseConfig(object):
    SQLALCHEMY_DATABASE_DBDRIVER = 'postgresql'
    SQLALCHEMY_DATABASE_DATABASE = 'skynet_db'
    SQLALCHEMY_DATABASE_HOSTNAME = 'localhost'
    SQLALCHEMY_DATABASE_PORTNUMB = '5433'
    SQLALCHEMY_DATABASE_PASSWORD = 'postgres'
    SQLALCHEMY_DATABASE_USERNAME = 'postgres'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = '{db_d}://{usrn}:{pasw}@{host}:{port}/{db_n}'.format(
        db_d=SQLALCHEMY_DATABASE_DBDRIVER,
        usrn=SQLALCHEMY_DATABASE_USERNAME,
        pasw=SQLALCHEMY_DATABASE_PASSWORD,
        host=SQLALCHEMY_DATABASE_HOSTNAME,
        port=SQLALCHEMY_DATABASE_PORTNUMB,
        db_n=SQLALCHEMY_DATABASE_DATABASE)


class TestingConfig(DatabaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = True


class ProductionConfig(DatabaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_PASSWORD = 'prod_postgres'
    SQLALCHEMY_DATABASE_USERNAME = 'prod_postgres'
