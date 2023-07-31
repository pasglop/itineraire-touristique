from source.databases import connect_db


class CleanData:
    def __init__(self):
        self.connect, self.session = connect_db()

    def search_similarities(self):
        """
        This function is used to search for similarities in the data.
        """
        query = """
        SET pg_trgm.similarity_threshold = 0.6;
        WITH paris AS (
           SELECT places.id, places.poi_id, places.name
           FROM   places
           inner join addresses on addresses.poi_id = places.poi_id
           inner join public.places_to_classes ptc on places.poi_id = ptc.poi_id
           inner join public.classes c on c.id = ptc.classes_id
           WHERE  addresses.locality = 'Paris'
           AND c.type in ('Museum', 'RemarkableBuilding')
           order by places.id
           ),
            similarity as (
            SELECT n1.id, n2.id as others, n1.name, n2.name as othername, similarity(n1.name, n2.name) AS sim
            FROM   paris n1
            JOIN   paris n2 ON n1.poi_id <> n2.poi_id
                           AND n1.name % n2.name
            where n1.id < n2.id
            ORDER  BY sim DESC)
        select s.id, s.name, array_agg(s.others) as similar_places,
                    array_agg(s.othername) as similar_places_names
        from similarity s
        group by s.id,s.name
        order by s.id
        """
        self.session.execute(query)
        res = self.session.fetchall()

        self.clean_data(res)

        return True

    def clean_data(self, res):
        for r in res:
            print(r)
            query = f"""
            DELETE FROM public.places WHERE id = ANY(ARRAY{r[2]})
            """
            print(query)
            self.session.execute(query)
            self.connect.commit()

