from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.okgwdyz.mongodb.net/?retryWrites=true&w=majority')
db = client.junggo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question', methods=['POST'])
def save_comment():
    comment_receive = request.form['comment_give']

    comment_list = {
        'comment': comment_receive,
        'comment_date': '2022-09-20'
    }

    db.comment.insert_one(comment_list)

    return jsonify({'msg': '문의 완료!'})


@app.route('/question', methods=['GET'])
def comment_get():
    reply_list = list(db.comment.find({}, {'_id':False}))
    return jsonify({'replys': reply_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
