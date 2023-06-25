import psycopg2


class ProcessError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message):
        self.message = message


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
