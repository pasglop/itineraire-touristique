import json
import os
from multiprocessing import Pool
import re

import psycopg2
from dotenv import load_dotenv

from source.data_loading.load_data import LoadData
import source.data_processing.table_processing as tp

load_dotenv()

load_object = LoadData()
fullDirPath = load_object.fullDirPath


def connect_db():
    """
    This function is used to connect to the postgresql database.
    :return:
    """
    conn = psycopg2.connect(
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"))
    return conn


def generate_schema_url(path_to_object):
    # example path 0/00/13-00006084-c3d9-3d90-8a22-e0a70f5c119a.json
    # example schema_url https://data.datatourisme.gouv.fr/13/00006084-c3d9-3d90-8a22-e0a70f5c119a
    regex = r"[a-f0-9]{1}/[a-f0-9]{2}/([0-9]{2})-([a-f0-9-]*)\.json"

    subst = "https://data.datatourisme.fr/\\g<1>/\\g<2>"
    return re.sub(regex, subst, path_to_object, 0)


def find_object(json_obj, cur):
    """
    This function is used to find the object in the database.
    and check if it needs to be updated.
    :param json_obj: object from json TOC
    :param cur: DB cursor
    :return: boolean
    """
    schema_url = generate_schema_url(json_obj['file'])
    query = f"SELECT 1 FROM public.places WHERE schema_url = '{schema_url}'"
    cur.execute(query)
    result = cur.fetchone()
    if result is None:
        return False

    return True


def process_file(json_object):
    # Process the file here
    # Replace this with your actual file processing logic
    db = connect_db()
    print(f"Processing Object: {json_object['label']}")
    cur = db.cursor()
    if not find_object(json_object, cur):
        # open the json file
        with open(fullDirPath + 'objects/' + json_object['file']) as json_file:
            data = json.load(json_file)
            # Combine both json objects
            data.update(json_object)
            # map the data to the a cleaner object?

            # Insert into the database
            try:
                tp.places_load(data, cur)
            except tp.ProcessError:
                print(f"Error: {tp.ProcessError}")
                return False

    cur.close()
    db.close()


class ProcessData:
    """
    This function is used to process the data contained into the raw_data folder.
    To do so, it will:
    - read the index.json file which have the table of contents
    - read each objects files
    - load the data into postgresql database
    """

    def __init__(self):
        """
        This function is used to initialize the ProcessData class.
        :param self:
        :return:
        """
        self.data = None
        self.fullDirPath = fullDirPath

    def read_toc(self):
        """
        This function is used to read the index.json file.
        :param self:
        :return:
        """
        try:
            with open(self.fullDirPath + 'index.json') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            print("File not found")
            return False
        except ValueError:
            print("File is not a valid JSON file")
            return False
        self.data = data
        return True

    def process_files_in_parallel(self):

        # Determine the number of available CPU cores
        num_processes = os.cpu_count()

        # Create a process pool with the determined number of processes
        with Pool(num_processes) as pool:
            # Map the file processing function to the file paths and execute them in parallel
            pool.map(process_file, self.data)



if __name__ == "__main__":
    processing = ProcessData()
    toc = processing.read_toc()
    processing.process_files_in_parallel()
