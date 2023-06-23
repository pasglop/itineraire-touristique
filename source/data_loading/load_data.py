from dotenv import load_dotenv
import os
import json
import requests
import git
import time
from zipfile import ZipFile

load_dotenv()


class LoadData():
    def __init__(self):
        self.url = os.getenv("DT_API_URL")
        self.key = os.getenv("DT_API_KEY")
        self.data_folder = "raw_data"
        self.filename = f"data-{time.strftime('%Y%m%d')}"
        # write in the raw_data folder
        repo = git.Repo('', search_parent_directories=True)
        self.path = repo.working_tree_dir + f'/{self.data_folder}/'
        self.fullFilePath = f'{self.path}{self.filename}.zip'
        self.fullDirPath = f'{self.path}{self.filename}/'
        self.data = None
        self.r = None

    def check_file_exists(self):
        return os.path.isfile(self.fullFilePath)

    def clean_files(self):
        # delete all files in the raw_data folder
        files = os.listdir(self.path)
        for file in files:
            os.remove(self.path + file)

    def download_data(self):
        if self.check_file_exists():
            print(f"Data already exists in {self.path}")
            return True
        # clean the raw_data folder
        self.clean_files()
        # call the api
        full_url = self.url + self.key
        print(f"Calling {full_url}")
        self.r = requests.get(full_url, stream=True)
        if self.r.status_code == 200:
            # write data in the raw_data folder
            print(f"Writing data in {self.path} folder")
            with open(self.fullFilePath, 'wb') as file:
                file.write(self.r.content)
            return True

        return False

    def unzip_data(self):
        with ZipFile(self.fullFilePath) as zObject:
            zObject.extractall(self.fullDirPath)
        zObject.close()
        return True


if __name__ == '__main__':
    loader = LoadData()
    loader.download_data()
    loader.unzip_data()
