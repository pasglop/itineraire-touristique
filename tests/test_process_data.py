import pytest
import dateutil.parser

from .context import process_data
from .context import databases
from .context import places_processing

class TestProcessData:
    @pytest.fixture
    def processing(self):
        return process_data.ProcessData()

    @pytest.fixture
    def db_session(self):
        conn, db_session = databases.connect_db()
        yield conn, db_session
        databases.disconnect_db(conn, db_session)

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
        data = process_data.load_json_object(processing.data[0])
        places = places_processing.PlacesProcessing(data, db_session)
        test = places.find_object()
        assert type(test) is bool

    def test_process_file(self, processing):
        processing.read_toc()
        test = process_data.process_file(processing.data[0])
        assert True
        
class TestPlacesProcessing(TestProcessData):

    def test_places_ops_check(self, processing, db_session):
        # get a record from TOC
        processing.read_toc()
        data = process_data.load_json_object(processing.data[0])
        # check if it exists in the database
        tp = places_processing.PlacesProcessing(data, db_session)
        test = tp.exists()

        # manually check if the record exists in the database
        db_conn, db_session = db_session
        query = f"""
            SELECT 1 FROM public.places 
            WHERE id = '{data['dc_identifier']}' AND 
            source_updated <= '{dateutil.parser.parse(data['lastUpdateDatatourisme'])}'
            """
        db_session.execute(query)
        result = True if db_session.fetchone() else False
        assert result == test

    def test_places_ops_insert(self, processing, db_session):
        # get a record from TOC
        processing.read_toc()
        data = process_data.load_json_object(processing.data[0])

        tp = places_processing.PlacesProcessing(data, db_session)
        if tp.exists():
            assert True
        else:
            test = tp.insert()
            assert test is True
            
    def test_places_ops_update(self, processing, db_session):
        # get a record from TOC
        processing.read_toc()
        data = process_data.load_json_object(processing.data[0])

        tp = places_processing.PlacesProcessing(data, db_session)
        if tp.exists():
            test = tp.update()
            assert test is True
        else:
            assert True
