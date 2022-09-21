from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.rblxfs7.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import os
from werkzeug.utils import secure_filename
#
# from daytime import timedelta
# timedelta(days=5, hours=17, minutes=30)
# datetime.timedelta(days=5, seconds=63000)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('index4.html')



@app.route("/products", methods=["POST"])
def list_post():
    name_receive = request.form['name_give']
    product_receive = request.form['product_give']

    desc_receive = request.form['desc_give']
    price_receive = request.form['price_give']



    # 현재시간
    # today = datetime.now()
    # my_time = today.strftime('%Y-%m-%d-%H-%M-%S')
    # 확장자

    # 확장자에 따라 올릴 수 있는 파일을 제한하여 오류 메세지를 전송합니다.
    # 프론트로 대륙 선택을 하지 않았을 경우에도 오류메세지를 전송합니다.
    # white_list = ['JPG', 'jpg', 'gif', 'png', 'PNG', 'webp']
    if request.method == "POST":
        f = request.files['file']
    extension = f.filename.split('.')[-1]
    f.save(secure_filename(f.filename))
    # save_to = f'static/img/{filename}.{extension}'
    # if extension not in white_list:
    #     return jsonify({'result': 'fail', 'msg': '올바른 파일 형식이 아닙니다!'})
    print(f)
    # print(save_to)
    print(os.getcwd())
    # f.save(save_to)

    # image_path = './new'
    # filename = secure_filename(file.filename)
    # os.makedirs(image_path, exists_ok=True)
    # file.save(os.path.join(image_path, filename))


    doc = {
        'name': name_receive,
        'product': product_receive,
        # 'img_url': f'{filename}.{extension}',
        'desc': desc_receive,
        'price': price_receive
    }
    db.products.insert_one(doc)

    return jsonify({'msg': '물건 등록 완료!'})

@app.route("/products", methods=["GET"])
def list_get():
    products_list = list(db.products.find({}, {'_id': False}))
    return jsonify({'products': products_list})





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
