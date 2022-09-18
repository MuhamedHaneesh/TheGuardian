from flask import Flask, request, Response
import pymongo
from bson import json_util

app = Flask(__name__)

MONGO_URI = 'mongodb+srv://MongoDB123:MongoDB123@cluster1.12bbqt2.mongodb.net/?retryWrites=true&w=majority'
connection = pymongo.MongoClient(MONGO_URI)
db = connection.cluster1


@app.route('/articles')
def articles():
    page = int(request.args.get("page", "1"))
    num_articles = int(request.args.get("num_documents", "5"))
    skips = num_articles * (page - 1)

    result = db.articles.find().limit(num_articles).skip(skips)
    return Response(
        json_util.dumps({
            'status': 'success',
            'page': page,
            'num_documents_found': result.count(),
            'num_documents_per_page': num_articles,
            'results': result}),
        mimetype='application/json'
    )


@app.route('/search/content')
def search_content():
    content = request.args.get("content", "")

    page = int(request.args.get("page", "1"))
    num_articles = int(request.args.get("num_articles", "5"))

    result = db.articles.find({"content": content})

    return Response(
        json_util.dumps({
            'status': 'success',
            'page': page,
            'num_articles_found': result.count(),
            'num_articles_per_page': num_articles,
            'results': result}),
        mimetype='application/json'
    )


@app.route('/search/headline')
def search_headline():
    query = request.args.get("headline", "")

    page = int(request.args.get("page", "1"))
    num_articles = int(request.args.get("num_articles", "5"))

    result = db.articles.find({"headline": query})
    return Response(
        json_util.dumps({
            'status': 'success',
            'page': page,
            'num_articles_found': result.count(),
            'num_articles_per_page': num_articles,
            'results': result}),
        mimetype='application/json'
    )


@app.route('/search/author')
def search_author():
    author = request.args.get("author", "")

    page = int(request.args.get("page", "1"))
    num_articles = int(request.args.get("num_articles", "5"))

    result = db.articles.find({"author": author})
    return Response(
        json_util.dumps({
            'status': 'success',
            'page': page,
            'num_articles_found': result.count(),
            'num_articles_per_page': num_articles,
            'results': result}),
        mimetype='application/json'
    )
