import psycopg2
from config import load_config

def get_vendors():
    """ Retrieve data from the vendors table using fetchall() """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
                rows = cur.fetchall()
                print("The number of vendors: ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_vendors()
