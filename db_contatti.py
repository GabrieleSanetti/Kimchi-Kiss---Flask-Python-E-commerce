from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Contatto(Base):
    __tablename__ = 'contatti'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)

    def send_message(message, session):
        session.add(message)

    def save(session):
        session.commit()

    def select_all(session):
        return session.query(Contatto).all()

    def delete_message(session, id):
        message = session.query(Contatto).filter(Contatto.id == id).first()
        if message:
            session.delete(message)
            session.commit()

    def get_contatto(session, name):
        return session.query(Contatto).filter(Contatto.name == name).first()