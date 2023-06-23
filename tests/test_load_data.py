import pytest
import os
from source.data_loading.load_data import LoadData


class TestLoadData:
    @pytest.fixture(autouse=True)
    def loader(self):
        return LoadData()

    def test_url_exists(self, loader):
        assert loader.url is not None

    def test_key_exists(self, loader):
        assert loader.key is not None

    def test_download_data(self, loader):
        test = loader.download_data()
        assert test is True
        assert os.path.isfile(loader.fullFilePath) is True

    def test_data_folder_exists(self, loader):
        test = loader.unzip_data()
        assert test is True
        assert os.path.isdir(loader.fullDirPath.rstrip('/')) is True
        assert os.path.isfile(loader.fullDirPath + 'index.json') is True
        assert os.path.isdir(loader.fullDirPath + 'objects') is True