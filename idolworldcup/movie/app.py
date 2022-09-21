from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.rblxfs7.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import os
from werkzeug.utils import secure_filename

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('index4.html')

@app.route('/sign_up')
def sign_up():
    return render_template('index5.html')


@app.route("/products", methods=["POST"])
def list_post():
    name_receive = request.form['name_give']
    product_receive = request.form['product_give']

    desc_receive = request.form['desc_give']
    price_receive = request.form['price_give']

    doc = {
        'name': name_receive,
        'product': product_receive,

        'desc': desc_receive,
        'price': price_receive
    }
    db.products.insert_one(doc)

    return jsonify({'msg': '물건 등록 완료!'})

@app.route("/products", methods=["GET"])
def list_get():
    products_list = list(db.products.find({}, {'_id': False}))
    return jsonify({'products': products_list})


@app.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file']
    image_path = './new'
    filename = secure_filename(file.filename)
    os.makedirs(image_path, exists_ok=True)
    file.save(os.path.join(image_path, filename))

    return

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
