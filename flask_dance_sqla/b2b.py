from sqlalchemy import create_engine

#engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

#"mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + MARIADB_PASSWORD + "@localhost:3306/" + MARIADB_DATABASE

engine_string = "mariadb+mariadbconnector://pythonuser:pythonuser@localhost:3306/world"

engine = create_engine(engine_string)

