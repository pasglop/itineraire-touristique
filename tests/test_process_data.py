import pytest

from source.data_processing.process_data import ProcessData


class TestProcessData:
    @pytest.fixture
    def processing(self):
        return ProcessData()

    def test_read_toc(self, processing):
        """Test that file can be opened
         and load table of contents"""
        toc = processing.read_toc()
        assert toc is True

    def test_find_object(self, processing):
        processing.read_toc()
        print(processing.data[0])
        assert True
