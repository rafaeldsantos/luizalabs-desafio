from flask import Flask, jsonify, request
from flasgger import Swagger
from neo4jmanager import Neo4jManager, UserNotFound
import logging

logging.basicConfig(filename='webservice.log',level=logging.WARNING,format='%(asctime)s %(message)s')
app = Flask(__name__)
Swagger(app)
database = Neo4jManager()

@app.route('/')
def index():
    return redirect(url_for('apidocs'))

@app.route('/friends/<username>', methods=['GET'])
def get_friends(username):
    logging.info('GET {} FRIENDS'.format(username))
    try:
        data = database.get_friends(username)
    except UserNotFound:
        logging.warning('ERROR 404: {} NOT FOUND'.format(username))
        data = {'Error':'Username {} not found'.format(username)}
        return jsonify(data=data, meta={"status": "404"})

    return jsonify(data=data, meta={"status": "ok"})

logging.basicConfig(filename='webservice.log',level=logging.WARNING,format='%(asctime)s %(message)s')
app = Flask(__name__)
Swagger(app)
database = Neo4jManager()

@app.route('/friends/', methods=['GET'])
def get_friends():
    """
    API
    ---
    tags:
      - LuizaLabs Desafio
    parameters:
      - name: username
        in: query
        type: string
        required: true
        description:
    responses:
      404:
        description:
      200:
        description: """
    username = str(request.args.get('username', 1))
    logging.info('GET {} FRIENDS'.format(username))
    try:
        data = database.get_friends(username)
    except UserNotFound:
        logging.warning('ERRO 404: {} NOT FOUND'.format(username))
        data = {'Error':'Username {} not found'.format(username)}
        return jsonify(data=data, meta={"status": "404"})
    return jsonify(data=data, meta={"status": "ok"})

@app.route('/sugestions/', methods=['GET'])
def get_sugestions():
    """
    API
    ---
    tags:
      - LuizaLabs Desafio
    parameters:
      - name: username
        in: query
        type: string
        required: true
        description:
    responses:
      404:
        description:
      200:
        description: """
    username = str(request.args.get('username', 1))
    logging.info('GET {} SUGGESTIONS'.format(username))
    try:
        data = database.get_suggestion(username)
    except UserNotFound:
        logging.warning('ERROR 404: {} NOT FOUND'.format(username))
        data = {'Error':'Username {} not found'.format(username)}
        return jsonify(data=data, meta={"status": "404"})
    return jsonify(data=data, meta={"status": "ok"})


@app.route('/log', methods=['GET'])
def get_log():
    """
    API
    ---
    tags:
      - LuizaLabs Desafio
    responses:
      200:
        description: """
    username = str(request.args.get('username', 1))
    with open("webservice.log", "r") as content_log:
        log = content_log.read().split('\n')

    return jsonify(data=log, meta={"status": "ok"})

if __name__ == '__main__':
    logging.info('STARTING PREPROCESSING...')
    database.preprocessing()
    logging.info('PREPROCESSING END')
    app.run(host='0.0.0.0', port=80)
    # app.run()
