from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base2 = declarative_base()

class Prodotto(Base2):
    __tablename__ = 'prodotti'
    id = Column(Integer, primary_key=True)
    img = Column(String)
    titolo = Column(String)
    codice = Column(String)
    descbreve = Column(String)
    stelle = Column(Integer)
    recensioni = Column(Integer)
    prezzo = Column(Float)
    prezzo_visibile = Column(String)
    qta = Column(Integer)
    descrizione = Column(String)
    tabnutrizione = Column(String)
    ingredienti = Column(String)
    categoria = Column(String)

    def add_product(prodotto, session):
        session.add(prodotto)

    def save(session):
        session.commit()

    def select_all_products(session):
        return session.query(Prodotto).limit(6).all()

    def delete_prodotto(session, id):
        prodotto = session.query(Prodotto).filter(Prodotto.id == id).first()
        if prodotto:
            session.delete(prodotto)
            session.commit()

    def get_prodotto(session, id):
        return session.query(Prodotto).filter(Prodotto.id == id).first()

    def categoria_filtro(session, categoria):
        return session.query(Prodotto).filter(Prodotto.categoria == categoria).all()

    def all_products_less_one(session):
        return session.query(Prodotto).filter(Prodotto.id != 2).limit(6).all()
