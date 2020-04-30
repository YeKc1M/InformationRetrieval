from flask import Flask, jsonify, render_template, request
from flask.helpers import url_for

from zoneIndex import simpleADD, weightADD

app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content']
        print(title+' '+content)
        print(title=='')
        res=[]
        if title=='':
            res=sorted(simpleADD(content), key=lambda k: k[1], reverse=True)
        else:
            res=sorted(weightADD(title, content), key=lambda k: k[1], reverse=True)
        print(res)
        return jsonify(res)
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)