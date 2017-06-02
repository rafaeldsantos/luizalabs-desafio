import py2neo
from py2neo import Graph, Node, Relationship
import logging
import pdb
logging.basicConfig(filename='webservice.log',level=logging.INFO, format='%(asctime)s %(message)s')
class Neo4jManager:
    def __init__(self):
        py2neo.authenticate("localhost:7474", "neo4j", "pudim")
        self.graph = Graph("http://localhost:7474/db/data/")
    def get_friends(self,name):
        query = "MATCH (p:Person) WHERE  (:Person {name:'%s'} )-[:FRIEND]->(p) return p" %(name)
        results = self.graph.run(query)
        data = results.data()
        if data == []:
            raise UserNotFound
        friends ={ "Friends": [x["p"]["name"] for x in data ]}
        return friends
    def get_suggestion(self,name):
        query = "MATCH (p:Person) WHERE  (:Person {name:'%s'} )-[:SUGGESTED]->(p) return p" %(name)
        results = self.graph.run(query)
        if data == []:
            raise UserNotFound
        data = results.data()
        sugesteds ={ "Sugesteds": [x["p"]["name"] for x in data ]}
        return sugesteds
    #this function isn't efficient
    def preprocessing(self):
        from collections import defaultdict
        results = self.graph.run("START n=node(*) MATCH (n)-[:FRIEND]->(m) RETURN n,m;")
        data = results.data()
        node_neighbours = defaultdict(list)
        for node in data:
            node_neighbours[node['n']].append(node['m'])
        for actual_node, friends in node_neighbours.items():
            suggestions = set()
            for friend in friends:
                suggestions = suggestions.union(set(node_neighbours[friend]))
            suggestions = suggestions.difference(set(friends))
            for suggestion in suggestions:
                if suggestion['name'] != actual_node['name']:
                    node_suggestion = Relationship(actual_node,"SUGGESTED", suggestion)
                    suggestion_node = Relationship(actual_node,"SUGGESTED", suggestion)
                    self.graph.create(node_suggestion)
                    self.graph.create(suggestion_node)

class UserNotFound(Exception):
    pass

if __name__ == '__main__':
    n = Neo4jManager()
    print(n.get_friends("Mari"))
