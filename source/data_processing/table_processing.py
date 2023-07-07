import dpath
import psycopg2
import dateutil.parser


class ProcessError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message):
        self.value = message


class TableProcessing:
    def __init__(self, table, mapping, comparison_keys, data, db_session):
        self.table = table
        self.mapping = mapping
        self.comparisonKeys = comparison_keys
        self.data = data
        self.db_conn, self.db_session = db_session

    def prepare_comparison(self):
        """
        This function is used to prepare the comparison between the object and the database.
        :param self:
        :return:
        """
        # first we check that the object has all the keys we need
        # then we create the comparison string
        comparison = ""
        for value in self.comparisonKeys:
            json_key = self.mapping[value]
            if json_key not in self.data.keys():
                raise ProcessError(f"Field {json_key} is missing from the object")
            if value == "id":
                if self.data[json_key].isdigit() is False:
                    raise ProcessError(f"Field {json_key} is not an integer")
                comparison += f"{value} = '{self.data[json_key]}' AND "
                continue
            # detecting a json date object
            try:
                test_date = dateutil.parser.parse(self.data[json_key])
                comparison += f"{value} <= '{test_date}' AND "
            except ValueError:
                comparison += f"{value} = '{self.data[json_key]}' AND "
        comparison = comparison[:-5]
        return comparison

    def exists(self, where=None):
        """
        This function is used to check if the object already exists in the database.
        :param where:
        :param self:
        :return:
        """
        if where is None:
            try:
                where = self.prepare_comparison()
            except ProcessError:
                # bypass this record
                return True

        query = f"""
        SELECT 1 FROM {self.table} WHERE {where}
        """
        try:
            self.db_session.execute(query)
            result = self.db_session.fetchone()
        except psycopg2.Error as e:
            raise ProcessError(f"Error for record {self.data['dc_identifier']} : {e.pgerror}")

        if result is None:
            return False

        return True

    def parse_data(self, cols):
        """
        This function is used to parse the data from the object.
        :param self:
        :return:
        """
        values = {}
        for key in cols:
            json_key = self.mapping[key]
            if json_key.find("/") != -1:
                try:
                    dict_value = dpath.get(self.data, json_key)
                    values[key] = None if dict_value == '' else dict_value
                except ValueError or IndexError:
                    raise ProcessError(f"Field {json_key} is missing from the object or is not properly formatted")
                except KeyError:
                    values[key] = None
            else:
                values[key] = None if self.data[json_key] == '' else self.data[json_key]

        return {k: v for k, v in values.items() if v is not None}

    def insert(self):
        """
        This function is used to insert the object in the database.
        :param self:
        :return:
        """
        cols = self.mapping.keys()
        values = self.parse_data(cols)
        # add updated_at value
        values['updated_at'] = 'now()'

        query = f"""
        INSERT INTO {self.table} ({', '.join(values.keys())})
        VALUES ({', '.join(['%s'] * len(values))})
        """
        try:
            self.db_session.execute(query, list(values.values()))
            self.db_conn.commit()
        except (psycopg2.Error, psycopg2.DataError) as e:
            raise ProcessError(f"Error for record {self.data} : {e.pgerror}")

        return True

    def update(self):
        """
        This function is used to update the object in the database.
        """
        cols = list(self.mapping)
        values = self.parse_data(cols)
        where = self.prepare_comparison()
        # add updated_at value
        values['updated_at'] = 'now()'
        # combine cols and place holders
        sql_values = ', '.join('{} = {}'.format(key, value) for key, value in values.items())

        query = f"""
            UPDATE {self.table} SET {sql_values} WHERE {where}
        """
        try:
            self.db_session.execute(query, values)
            self.db_conn.commit()
        except psycopg2.Error as e:
            raise ProcessError(f"Error for record {self.data} : {e.pgerror}")

        return True

    def process(self, data):
        self.data = data
        # check if the object exists
        if self.exists():
            # if it exists, we update it
            self.update()
        else:
            self.insert()

        return True
