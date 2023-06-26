import psycopg2
import dateutil.parser


class ProcessError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message):
        self.message = message


class TableProcessing:
    def __init__(self, table, comparison_keys, data, db_session):
        self.table = table
        self.comparisonKeys = comparison_keys
        self.data = data
        self.db_session = db_session

    def prepare_comparison(self):
        """
        This function is used to prepare the comparison between the object and the database.
        :param self:
        :return:
        """
        # first we check that the object has all the keys we need
        # then we create the comparison string
        comparison = ""
        for key, value in self.comparisonKeys.items():
            if value not in self.data.keys():
                raise ProcessError(f"Field {value} is missing from the object")
            # detecting a json date object
            try:
                test_date = dateutil.parser.parse(self.data[self.comparisonKeys[key]])
                comparison += f"{key} < '{test_date}' AND "
            except ValueError:
                comparison += f"{key} = '{self.data[self.comparisonKeys[key]]}' AND "
        comparison = comparison[:-5]
        return comparison

    def exists(self):
        """
        This function is used to check if the object already exists in the database.
        :param self:
        :return:
        """
        comparison = self.prepare_comparison()
        query = f"""
        SELECT 1 FROM {self.table} WHERE {comparison}
        """
        try:
            self.db_session.execute(query)
            result = self.db_session.fetchone()
        except psycopg2.Error as e:
            raise ProcessError(e.pgerror)

        if result is None:
            return False

        return True


def places_load(data, cursor):

    print(data['isOwnedBy'])
    query = f"""
    INSERT
    INTO
    public.places(id, name, schema_url, website, latitude, longitude, "lastUpdate", "sourceUpdated")
    VALUES
    ('{data['dc:identifier']}', '{data['label']}', '{data['@id']}',
    '{data['isOwnedBy']['foaf:homepage']}', {data['schema:geo']['schema:latitude']},
    {data['schema:geo']['schema:longitude']}, now(), '{data['lastUpdateDatatourisme']}')"
    """

    try:
        cursor.execute(query)
    except psycopg2.Error as e:
        raise ProcessError(e.pgerror)

    return True
