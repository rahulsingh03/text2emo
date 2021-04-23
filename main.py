import text2emotion as te
from flask import Flask,request


app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    text = request.args.get('text')
    return {'text': te.get_emotion(text)}


if __name__ == '__main__':
    app.run(debug=True,port=2222)
