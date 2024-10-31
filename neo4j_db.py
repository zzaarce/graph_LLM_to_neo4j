from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

class Neo4jDatabase:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def insert_entity(self, entity_name, entity_type):
        with self.driver.session() as session:
            session.run("MERGE (e:Entity {name: $name, type: $type})", name=entity_name, type=entity_type)
