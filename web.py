from flask import Flask, jsonify, render_template, request
from flask.helpers import url_for

from index import getCorpora
from zoneIndex import simpleADD, weightADD
from booleanTfidf import tfidfSearch, wfidfSearch1, wfidfSearch2
from vectortfidf import vectortfidfSearch, vectorwfidfSearch1, vectorwfidfSearch2, tfidfsims, wfidf1sims, wfidf2sims
from languageModel import cal_pro, sim1, sim2, sim3

app=Flask(__name__)

corpora=getCorpora()

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
    if res[0][1]!=0:
        print(corpora[res[0][0]])
    return jsonify(res)

@app.route('/vectorwfidf1', methods=['POST'])
def vectorwfidf1():
    query=request.form['query']
    print(query)
    res=vectorwfidfSearch1(query)
    res=sorted(res, key=lambda k: k[1], reverse=True)
    if res[0][1]!=0:
        print(corpora[res[0][0]])
    return jsonify(res)

@app.route('/vectorwfidf2', methods=['POST'])
def vectorwfidf2():
    query=request.form['query']
    print(query)
    res=vectorwfidfSearch2(query)
    res=sorted(res, key=lambda k: k[1], reverse=True)
    if res[0][1]!=0:
        print(corpora[res[0][0]])
    return jsonify(res)

@app.route('/fastertfidf', methods=['POST'])
def fastertfidf():
    query=request.form['query']
    print(query)
    res=tfidfsims(query)
    sim=[]
    for i in range(len(res)):
        sim.append([i, res[i]])
    sim=sorted(sim, key=lambda k: k[1], reverse=True)
    content=''
    if sim[0][1]!=0:
        content=corpora[sim[0][0]]
    return jsonify({'sims':sim[:5], 'content':content})

@app.route('/fasterwfidf1', methods=['POST'])
def fasterwfidf1():
    query=request.form['query']
    print(query)
    res=wfidf1sims(query)
    sim=[]
    for i in range(len(res)):
        sim.append([i, res[i]])
    sim=sorted(sim, key=lambda k: k[1], reverse=True)
    content=''
    if sim[0][1]!=0:
        content=corpora[sim[0][0]]
    return jsonify({'sims':sim[:5], 'content':content})

@app.route('/fasterwfidf2', methods=['POST'])
def fasterwfidf2():
    query=request.form['query']
    print(query)
    res=wfidf2sims(query)
    sim=[]
    for i in range(len(res)):
        sim.append([i, res[i]])
    sim=sorted(sim, key=lambda k: k[1], reverse=True)
    content=''
    if sim[0][1]!=0:
        content=corpora[sim[0][0]]
    return jsonify({'sims':sim[:5], 'content':content})

@app.route('/languagemodel', methods=['POST'])
def languagemodel():
    query=request.form['query']
    print(query)
    res=sorted(cal_pro(query), key=lambda k: k[1], reverse=True)
    content=corpora[res[0][0]]
    return jsonify({'sims':res[:5], 'content':content})

@app.route('/prior1', methods=['POST'])
def prior1():
    query=request.form['query']
    print(query)
    res=sorted(sim1(query), key=lambda k: k[1], reverse=True)
    content=corpora[res[0][0]]
    return jsonify({'sims':res[:5], 'content':content})

@app.route('/prior2', methods=['POST'])
def prior2():
    query=request.form['query']
    print(query)
    res=sorted(sim2(query), key=lambda k: k[1], reverse=True)
    content=corpora[res[0][0]]
    return jsonify({'sims':res[:5], 'content':content})

@app.route('/prior3', methods=['POST'])
def prior3():
    query=request.form['query']
    print(query)
    res=sorted(sim3(query), key=lambda k: k[1], reverse=True)
    content=corpora[res[0][0]]
    return jsonify({'sims':res[:5], 'content':content})

if __name__=='__main__':
    app.run(debug=True)