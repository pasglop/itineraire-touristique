import dpath
import psycopg2
import dateutil.parser


class ProcessError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message):
        self.message = message


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
            where = self.prepare_comparison()
        query = f"""
        SELECT 1 FROM {self.table} WHERE {where}
        """
        try:
            self.db_session.execute(query)
            result = self.db_session.fetchone()
        except psycopg2.Error as e:
            raise ProcessError(e.pgerror)

        if result is None:
            return False

        return True

    def parse_data(self):
        """
        This function is used to parse the data from the object.
        :param self:
        :return:
        """
        values = []
        for key in self.mapping.keys():
            json_key = self.mapping[key]
            if json_key.find("/") != -1:
                try:
                    dict_value = dpath.get(self.data, json_key)
                    values.append(dict_value)
                except ValueError or IndexError:
                    raise ProcessError(f"Field {json_key} is missing from the object or is not properly formatted")
            else:
                values.append(self.data[json_key])

        return values

    def insert(self):
        """
        This function is used to insert the object in the database.
        :param self:
        :return:
        """
        cols = self.mapping.keys()
        values = self.parse_data()

        query = f"""
        INSERT INTO {self.table} ({', '.join(cols)}, updated_at)
        VALUES ('{"','".join(values)}', NOW())
        """
        try:
            self.db_session.execute(query)
            self.db_conn.commit()
        except psycopg2.Error as e:
            raise ProcessError(e.pgerror)

        return True

    def update(self):
        """
        This function is used to update the object in the database.
        """
        cols = list(self.mapping)
        values = self.parse_data()
        where = self.prepare_comparison()
        # combine cols and values
        cols_values = [f"{cols[i]} = '{values[i]}'" for i in range(len(cols))]
        
        query = f"""
            UPDATE {self.table} SET {', '.join(cols_values)}, updated_at = NOW()
        """
        try:
            self.db_session.execute(query)
            self.db_conn.commit()
        except psycopg2.Error as e:
            raise ProcessError(e.pgerror)

        return True
