from flask import Flask, jsonify, render_template, request
from flask.helpers import url_for

from zoneIndex import simpleADD, weightADD
from booleanTfidf import tfidfSearch, wfidfSearch1, wfidfSearch2
from vectortfidf import vectortfidfSearch, vectorwfidfSearch1, vectorwfidfSearch2

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

@app.route('/booleanTfidf', methods=['POST'])
def booleanTfidf():
    query=request.form['booleanquery']
    res=tfidfSearch(query)
    res=sorted(res, key=lambda k: k[1], reverse=True)
    print(res)
    return jsonify(res)

@app.route('/booleanwfidf1', methods=['POST'])
def booleanwfidf1():
    query=request.form['booleanquery']
    print(query)
    res=wfidfSearch1(query)
    res=sorted(res, key=lambda k: k[1], reverse=True)
    print(res)
    return jsonify(res)

@app.route('/booleanwfidf2', methods=['POST'])
def booleanwfidf2():
    query=request.form['booleanquery']
    print(query)
    res=wfidfSearch2(query)
    res=sorted(res, key=lambda k: k[1], reverse=True)
    print(res)
    return jsonify(res)

@app.route('/vectortfidf', methods=['POST'])
def vectortfidf():
    query=request.form['query']
    print(query)
    res=vectortfidfSearch(query)
    res=sorted(res, key=lambda k: k[1], reverse=True)
    print(res)
    return jsonify(res)

@app.route('/vectorwfidf1', methods=['POST'])
def vectorwfidf1():
    query=request.form['query']
    print(query)
    res=vectorwfidfSearch1(query)
    res=sorted(res, key=lambda k: k[1], reverse=True)
    print(res)
    return jsonify(res)

@app.route('/vectorwfidf2', methods=['POST'])
def vectorwfidf2():
    query=request.form['query']
    print(query)
    res=vectorwfidfSearch2(query)
    res=sorted(res, key=lambda k: k[1], reverse=True)
    print(res)
    return jsonify(res)

if __name__=='__main__':
    app.run(debug=True)