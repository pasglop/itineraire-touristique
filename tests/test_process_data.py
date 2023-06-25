import pytest

from source.data_processing.process_data import ProcessData, connect_db, find_object, process_file


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
        assert True

    def test_query_object_exits(self, processing):
        processing.read_toc()
        db = connect_db()
        cur = db.cursor()
        test = find_object(processing.data[0], cur)
        cur.close()
        db.close()
        assert type(test) is bool

    def test_process_file(self, processing):
        processing.read_toc()
        test = process_file(processing.data[0])
        assert True