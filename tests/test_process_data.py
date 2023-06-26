import pytest
import dateutil.parser

from source.data_processing.process_data import ProcessData, connect_db, find_object, process_file, disconnect_db, \
    load_json_object
from source.data_processing.table_processing import TableProcessing


class TestProcessData:
    @pytest.fixture
    def processing(self):
        return ProcessData()

    @pytest.fixture
    def db_session(self):
        conn, db_session = connect_db()
        yield db_session
        disconnect_db(conn, db_session)

    def test_read_toc(self, processing):
        """Test that file can be opened
         and load table of contents"""
        toc = processing.read_toc()
        assert toc is True

    def test_find_object(self, processing):
        processing.read_toc()
        assert True

    def test_query_object_exits(self, processing, db_session):
        processing.read_toc()
        test = find_object(processing.data[0], db_session)
        assert type(test) is bool

    def test_process_file(self, processing):
        processing.read_toc()
        test = process_file(processing.data[0])
        assert True

    def test_table_ops_check(self, processing, db_session):
        # get a record from TOC
        processing.read_toc()
        data = load_json_object(processing.data[0])
        # check if it exists in the database
        # we need a dict with keys to compare / preferably primary keys
        compare_keys = {"id": "dc:identifier", "source_updated": "lastUpdateDatatourisme"}

        tp = TableProcessing('public.places', compare_keys, data, db_session)
        test = tp.exists()

        # manually check if the record exists in the database
        db_session.execute(f"SELECT 1 FROM public.places "
                                   f"WHERE id = '{data['dc:identifier']}' AND"
                                   f" source_updated = '{dateutil.parser.parse(data['lastUpdateDatatourisme'])}'")
        result = True if db_session.fetchone() else False
        assert result == test
