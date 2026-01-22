import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_contatti import Base
from db_prodotti import Base2, Prodotto
from db_categorie import Base3, Categoria
# from sqlalchemy.pool import NullPool
from dotenv import load_dotenv


def initialize(Base, Base2, Base3):
    # Cerca la variabile DATABASE_URL. 
    # Se non la trova (es. sei in locale senza variabili), usa il vecchio indirizzo locale.
    database_url = os.environ.get("DATABASE_URL", "postgresql://postgres:12345@db:5432/postgres")

    # Correzione per SQLAlchemy: alcune piattaforme usano "postgres://", 
    # ma SQLAlchemy vuole "postgresql://"
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    

    # url = "postgresql://postgres:12345@db:5432/"
    # db_name = "postgres"

    engine = create_engine(database_url)
    # engine = create_engine(url + db_name)

    Base.metadata.bind = engine
    Base2.metadata.bind = engine
    Base3.metadata.bind = engine

    Base.metadata.create_all(engine)
    Base2.metadata.create_all(engine)
    Base3.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

session = initialize(Base, Base2, Base3)

# Visualizza tutti i prodotti
prodotti = Prodotto.select_all_products(session)

# Visualizza tutti i prodotti meno che il prodotto con id = 2
prodotti_filtrati = Prodotto.all_products_less_one(session)

# Visualizza tutte le categorie
categorie = Categoria.select_all_categories(session)

# Aggiungi una categoria
#c1 = Categoria(img = "icon-drink.svg", nome = "bevande", slug = "bevande")
#Categoria.add_category(c1, session)
#Categoria.save(session)