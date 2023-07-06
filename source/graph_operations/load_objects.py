from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

from source.databases import connect_neo4j, disconnect_neo4j, connect_db

load_dotenv()  # take environment variables from .env.


class LoadObjects:

    def __init__(self):
        self.graphdb = connect_neo4j()
        self.db, self.cursor = connect_db()

    def close(self):
        disconnect_neo4j(self.graphdb)

    def load_data_from_db(self):
        result = self.cursor.execute("SELECT * FROM public.places LIMIT 10")
        return result.data()

    def print_greeting(self, message):
        with self.graphdb.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


if __name__ == "__main__":
    pass
