from flask import Flask, jsonify, request
from flasgger import Swagger
from neo4jmanager import Neo4jManager, UserNotFound
import logging

logging.basicConfig(filename='webservice.log',level=logging.WARNING,format='%(asctime)s %(message)s')
app = Flask(__name__)
Swagger(app)
database = Neo4jManager()

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

@app.route('/friends/<username>', methods=['GET'])
def get_friends(username):
    # """
    # This is the language awesomeness API
    # Call this api passing a language name and get back its features
    # ---
    # tags:
    #   - Awesomeness Language API
    # parameters:
    #   - name: username
    #     in: path
    #     type: string
    #     required: true
    # responses:
    #   404:
    #     description: User not found!
    #   200:
    #     description: A language with its awesomeness
    #     schema:
    #       id: awesome
    #       properties:
    #         language:
    #           type: string
    #           description: The language name
    #           default: Lua
    #         features:
    #           type: array
    #           description: The awesomeness list
    #           items:
    #             type: string
    #           default: ["perfect", "simple", "lovely"]
    #
    # """
    logging.info('GET {} FRIENDS'.format(username))
    try:
        data = database.get_friends(username)
    except UserNotFound:
        logging.warning('ERRO 404: {} NOT FOUND'.format(username))
        data = {'Error':'Username {} not found'.format(username)}
        return jsonify(data=data, meta={"status": "404"})
    return jsonify(data=data, meta={"status": "ok"})

@app.route('/sugestions/<username>', methods=['GET'])
def get_sugestions(username):
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
    with open("webservice.log", "r") as content_log:
        log = content_log.read().split('\n')

    return jsonify(data=log, meta={"status": "ok"})

if __name__ == '__main__':
    logging.info('STARTING PREPROCESSING...')
    database.preprocessing()
    logging.info('PREPROCESSING END')
    app.run(host='0.0.0.0')
    # app.run()
