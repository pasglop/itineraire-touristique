from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

from source.databases import connect_neo4j, disconnect_neo4j

load_dotenv()  # take environment variables from .env.


class LoadObjects:

    def __init__(self):
        self.driver = connect_neo4j()

    def close(self):
        disconnect_neo4j(self.driver)

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "password")
    greeter.print_greeting("hello, world")
    greeter.close()
