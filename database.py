import psycopg2
import psycopg2.extras


class Connection:

    def __init__(self, database, user):
        connection = psycopg2.connect(database=database, user=user)
        self.__cursor = connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

    def query(self, query):
        self.__cursor.execute(query)
        return self

    def fetch_all(self):
        return self.__cursor.fetchall()

    def fetch_one(self):
        return self.__cursor.fetchone()


if __name__ == '__main__':
    db = Connection('dvdrental', 'rodgers')
    results = db.query("""
        SELECT name, COUNT(DISTINCT f.film_id ) FROM rental r
        JOIN inventory i ON (r.inventory_id=i.inventory_id)
        JOIN film f ON (f.film_id=i.film_id)
        JOIN film_category fc ON (fc.film_id=f.film_id)
        JOIN category c ON (c.category_id=fc.category_id)
        GROUP BY name ORDER BY COUNT  DESC""").fetch_all()
    for result in results:
        print("Category: {name}\nMovies: {count}".format(**result))
