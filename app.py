from settings import *

'''
 Notícias
 -----------------------
'''
#Listar notícias
@app.route('/news', methods=['GET'])
def get_all_news():
    news = mongo.db.news

    output = []

    for q in news.find():
        output.append(
            {'_id':str(q['_id']),
             'self': request.url + '/' + str(q['_id']),
             'title': q['title'],
             'content': q['content'],
             'author': mongo.db.authors.find_one({'_id': ObjectId(q['author']['_id'])})})

    return jsonify({'results': output})


#Postar notícia
@app.route('/news', methods=['POST'])
def add_news():
    news = mongo.db.news

    content = request.json['content']
    author = request.json['author']
    title = request.json['title']

    author_id = mongo.db.authors.find_one({'name': author})

    if not author_id:
        author_id = mongo.db.authors.insert({'name': author})
        news.insert({'title': title, 'content': content, 'author': {'_id': author_id}})
    else:
        news.insert({'title': title, 'content': content, 'author': author_id})

    return Response(status=201)


# Pegar notícia pelo id
@app.route('/news/<id>', methods=['GET'])
def get_news(id):
    news = mongo.db.news

    found = news.find_one({'_id': ObjectId(id)})

    if found:
        output = {'title': found['title'],
                  'content': found['content'],
                  'author':  mongo.db.authors.find_one({'_id': ObjectId(found['author']['_id'])})}

        return jsonify({'result': output})

    return Response(status=404)



# Atualizar notícia pelo id
@app.route('/news/<id>', methods=['PUT'])
def update_news(id):
    news = mongo.db.news

    title = request.json['title']
    content = request.json['content']
    author = request.json['author']

    news.update_one({'_id': ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)},
                              {'$set':{'title': title, 'content': content, 'author': author}})

    return Response(status=200)


# Deletar notícia pelo id
@app.route('/news/<id>', methods=['DELETE'])
def delete_news(id):
    news = mongo.db.news

    news.delete_one({'_id': ObjectId(id)})
    return Response(status=200)


# Pesquisar notícia
@app.route('/search/<query>', methods=['GET'])
def search_news(query):
    news = mongo.db.news

    news.drop_indexes()
    news.create_index([('title', 'text'), ('content', 'text'), ('author.name', 'text')])

    found = news.find({ "$text": { "$search": query }})

    output = []
    if found:
        for q in found:
            output.append(
                {'title': q['title'],
                 'content': q['content'],
                 'author': q['author']})

    return jsonify({'results': output})


'''
 Autores
 -----------------------
'''
# Listar autores
@app.route('/authors', methods=['GET'])
def get_all_authors():
    authors = mongo.db.authors

    output = []
    for q in authors.find():
        output.append(
            {'_id':str(q['_id']), 'self': request.url + '/' + str(q['_id']), 'name': q['name']})

    return jsonify({'results': output})

# Cadastrar autores
@app.route('/authors', methods=['POST'])
def add_author():
    authors = mongo.db.authors
    name = request.json['name']
    authors.insert({'name': name})

    return Response(status=201)


# Pegar autor pelo id
@app.route('/authors/<id>', methods=['GET'])
def get_author(id):
    authors = mongo.db.authors

    found = authors.find_one({'_id': ObjectId(id)})
    output = {'name': found['name']}

    return jsonify({'result': output})

# Atualizar autor pelo id
@app.route('/authors/<id>', methods=['PUT'])
def update_author(id):
    authors = mongo.db.authors

    name = request.json['name']
    authors.update_one({'_id': ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)},{'$set':{'name': name}})

    return Response(status=200)

# Deletar autor pelo id
@app.route('/authors/<id>', methods=['DELETE'])
def delete_author(id):
    authors = mongo.db.authors
    authors.delete_one({'_id': ObjectId(id)})
    return Response(status=200)

if __name__ == '__main__':
    app.run(debug=True)
