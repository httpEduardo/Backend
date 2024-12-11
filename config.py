class Config:
    DATABASE = "database.db"
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = "development_database.db"

class ProductionConfig(Config):
    DEBUG = False
    DATABASE = "production_database.db"
