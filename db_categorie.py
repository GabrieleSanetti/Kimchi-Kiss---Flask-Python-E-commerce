from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base3 = declarative_base()

class Categoria(Base3):
    __tablename__ = 'categorie'
    id = Column(Integer, primary_key=True)
    img = Column(String)
    nome = Column(String)
    slug = Column(String)

    def add_category(categoria, session):
        session.add(categoria)

    def save(session):
        session.commit()

    def select_all_categories(session):
        return session.query(Categoria).all()

    def delete_category(session, id):
        categoria = session.query(Categoria).filter(Categoria.id == id).first()
        if categoria():
            session.delete(categoria)
            session.commit()

    def get_categoria(session, nome):
        return session.query(Categoria).filter(Categoria.nome == nome).first()