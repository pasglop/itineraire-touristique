import json
import os
from multiprocessing import Pool

from source.data_loading.load_data import LoadData


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
        load_object = LoadData()
        self.fullDirPath = load_object.fullDirPath

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

    def process_file(file_path):
        # Process the file here
        # Replace this with your actual file processing logic
        print(f"Processing file: {file_path}")

    def process_files_in_parallel(file_paths):
        # Determine the number of available CPU cores
        num_processes = os.cpu_count()

        # Create a process pool with the determined number of processes
        with Pool(num_processes) as pool:
            # Map the file processing function to the file paths and execute them in parallel
            pool.map(process_file, file_paths)


if __name__ == "__main__":
    processing = ProcessData()
    toc = processing.read_toc()
    print(toc)