import py2neo
from py2neo import Graph, Node, Relationship
import pdb

py2neo.authenticate("localhost:7474", "neo4j", "pudim")
graph = Graph("http://localhost:7474/db/data/")
arthur = Node("Person", name="Arthur")
mari = Node("Person", name="Mari")
eduardo = Node("Person", name="Eduardo")
gabriel = Node("Person", name="Gabriel")

arthur_mari = Relationship(arthur,"FRIEND",mari)
mari_arthur = Relationship(mari,"FRIEND",arthur)
arthur_eduardo = Relationship(arthur,"FRIEND",eduardo)
eduardo_arthur = Relationship(eduardo,"FRIEND",arthur)
gabriel_mari = Relationship(gabriel,"FRIEND",mari)
mari_gabriel = Relationship(mari,"FRIEND",gabriel)
eduardo_gabriel = Relationship(eduardo,"FRIEND",gabriel)
gabriel_eduardo = Relationship(gabriel,"FRIEND",eduardo)
mari_eduardo = Relationship(mari,"FRIEND",eduardo)
eduardo_mari = Relationship(eduardo,"FRIEND",mari)

graph.create(arthur_mari)
graph.create(mari_arthur)
graph.create(arthur_eduardo)
graph.create(eduardo_arthur)
graph.create(gabriel_mari)
graph.create(mari_gabriel)
graph.create(eduardo_gabriel)
graph.create(gabriel_eduardo)
graph.create(mari_eduardo)
graph.create(eduardo_mari)
