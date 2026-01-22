import os
from flask import Flask, render_template, request
from sqlalchemy import func
from main import prodotti, categorie, session
from db_contatti import Contatto
from db_prodotti import Prodotto
from db_categorie import Categoria

app = Flask(__name__)
@app.route('/')
def index():
    prodotti = session.query(Prodotto).filter(Prodotto.id != 2).limit(6).all()
    return render_template('categoria.html', prodotti = prodotti, categorie = categorie)

@app.route('/categoria/<slug>')
def prodotti_filtrati(slug):
    prodotti = Prodotto.categoria_filtro(session, slug)
    return render_template('categoria.html', prodotti = prodotti, categorie = categorie)


@app.route('/prodotto/<id>')
def scheda_prodotto(id):
    prodotto = session.get(Prodotto, id)
    if prodotto:
        return render_template('prodotto.html', prodotto=prodotto)
    else:
        return render_template('categoria.html', prodotti=prodotti, categorie=categorie)

@app.route('/contatti', methods = ['POST', 'GET'])
def contatto():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        nuovo_contatto = Contatto(name=name, email=email, message=message)
        Contatto.send_message(nuovo_contatto, session)
        Contatto.save(session)
        return render_template('inviato.html', name = name, email = email)
    else:
        return render_template('contatti.html')

@app.route('/lucky-box', methods = ['POST', 'GET'])
def lucky_box():
    if request.method == 'GET':
        select = session.query(Prodotto).limit(6).all()
        return render_template('lucky-box.html', luckybox=select)
    else:
        select = session.query(Prodotto).order_by(func.random()).limit(6).all()
        return render_template('lucky-box.html', luckybox=select)


@app.route('/add-product', methods = ['POST', 'GET'])
def add_products():
    if request.method == 'POST':

        img = request.form['img']
        titolo = request.form['titolo']
        codice = request.form['codice']
        descbreve = request.form['descbreve']
        stelle = request.form['stelle']
        recensioni = request.form['recensioni']
        prezzo = request.form['prezzo']
        qta = request.form['qta']
        descrizione = request.form['descrizione']
        tabnutrizione = request.form['tabnutrizione']
        ingredienti = request.form['ingredienti']
        categoria = request.form['categoria']
        prezzo_visibile = request.form['prezzo_visibile']

        nuovo_prodotto = Prodotto(img=img,
                                  titolo=titolo,
                                  codice=codice,
                                  descbreve=descbreve,
                                  stelle=stelle,
                                  recensioni=recensioni,
                                  prezzo=prezzo,
                                  qta=qta,
                                  descrizione=descrizione,
                                  tabnutrizione=tabnutrizione,
                                  ingredienti=ingredienti,
                                  categoria=categoria,
                                  prezzo_visibile=prezzo_visibile)
        Prodotto.add_product(nuovo_prodotto, session)
        Prodotto.save(session)
        return render_template('add-product.html', cats = Categoria.select_all_categories(session))
    else:
        return render_template('add-product.html', cats = Categoria.select_all_categories(session))




if __name__ == '__main__':
    # Render usa la porta 10000 di default per il piano free
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)