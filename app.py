from flask import Flask, jsonify, request, render_template, redirect, make_response, flash
from main import Transaction
import json
import logging

app = Flask(__name__)

transaction = Transaction()

# Create Logger
app.logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('app.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)


@app.route('/', methods=['GET'])
def cashier():
    try:
        table, data, total_harga = transaction.check_order()
        return render_template('index.html', table=data, total_harga=total_harga)
   
    except Exception as e:
        app.logger.exception(e)

@app.route('/add_item', methods=['POST'])
def tambah_item():
    try:
        nama_item = request.form.get('nama_item')
        jumlah_item = int(request.form.get('jumlah_item'))
        harga = int(request.form.get('harga'))
        
        item = (nama_item, jumlah_item, harga)
        transaction.add_item(item)
        app.logger.info(f"Successed to add item {item[0]}")

        return redirect('/')
    
    except Exception as e:
        app.logger.exception(e)


@app.route('/delete_item/<string:name>', methods=['POST'])
def delete_item(name):
    transaction.delete_item(name)
    return redirect('/')


@app.route('/update_item', methods=['POST'])
def update_item():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = int(request.form['price'])
    transaction.update_item(name, quantity, price)
    return redirect('/')


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    response = transaction.check_out()
    if len(response) < 4:
        return render_template('checkout.html', 
                               item_data=response[0], 
                               total_harga=response[1],
                               total_harga_setelah_diskon= None,
                               persen_diskon= None
                              )
    else:
        return render_template('checkout.html', 
                               item_data=response[0], 
                               total_harga=response[1], 
                               total_harga_setelah_diskon=response[2],
                               persen_diskon=round(response[3])
                              )

@app.route('/back')
def back():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
