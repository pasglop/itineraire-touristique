import json
import os
from multiprocessing import Pool
import re

from dotenv import load_dotenv

from source.data_loading.load_data import LoadData
from source.databases import connect_db, disconnect_db
from source.data_processing.places_processing import PlacesProcessing
from source.data_processing.table_processing import ProcessError
from source.data_processing.openings_processing import OpeningsProcessing
from source.data_processing.addresses_processing import AddressesProcessing
from source.data_processing.descriptions_processing import DescriptionsProcessing
from source.data_processing.places_to_classes import PlacesToClassesProcessing
from source.data_processing.contacts_processing import ContactsProcessing




load_dotenv()

load_object = LoadData()
fullDirPath = load_object.fullDirPath


def clean_key(obj):
    for key in list(obj):
        new_key = key.replace(":", "_")
        if new_key != key:
            obj[new_key] = obj[key]
            del obj[key]
    return obj


def process_file(json_object):
    # Process the file here
    # Replace this with your actual file processing logic
    db, cur = connect_db()
    print(f"Processing Object: {json_object['label']}")
    json_object['schema_url'] = generate_schema_url(json_object['file'])
    places = PlacesProcessing(json_object, (db, cur))
    descriptions = DescriptionsProcessing(json_object, (db, cur))
    addresses = AddressesProcessing(json_object, (db, cur))
    openings = OpeningsProcessing(json_object, (db, cur))
    places_to_classes = PlacesToClassesProcessing(json_object, (db, cur))
    contacts = ContactsProcessing(json_object, (db, cur))
    if not places.find_object():
        # Table Places
        data = load_json_object(json_object)
        try:
            places.process(data)
            descriptions.process(data)
            addresses.process(data)
            openings.process(data)
            contacts.process(data)
            places_to_classes.process(data)
        except ProcessError as e:
            # bypass this record
            print(f"Error : {e}")
            
    disconnect_db(db, cur)


def generate_schema_url(path_to_object):
    # example path 0/00/13-00006084-c3d9-3d90-8a22-e0a70f5c119a.json
    # example schema_url https://data.datatourisme.gouv.fr/13/00006084-c3d9-3d90-8a22-e0a70f5c119a
    regex = r"[a-f0-9]{1}/[a-f0-9]{2}/([0-9]{2})-([a-f0-9-]*)\.json"

    subst = "https://data.datatourisme.fr/\\g<1>/\\g<2>"
    return re.sub(regex, subst, path_to_object, 0)


def load_json_object(json_object):
    with open(fullDirPath + 'objects/' + json_object['file']) as json_file:
        data = json.load(json_file, object_hook=clean_key)
        # Combine both json objects
        data.update(json_object)
        # process specific fields
        data['schema_url'] = generate_schema_url(data['file'])
        return data


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
