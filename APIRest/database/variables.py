import os
def cargarvariables():
    os.environ['DB_HOST']='mariadb'
    os.environ['DB_PORT']=3306
    os.environ['DB_NAME']='restaurant'
    os.environ['DB_USER']='PEPS'
    os.environ['DB_PASSWORD']='secret'

