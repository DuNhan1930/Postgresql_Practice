import psycopg2
from config import load_config

def iter_row(cursor, size=5):
    """ Helper generator for batch fetching rows """
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_part_vendors():
    """ Retrieve part/vendor data using fetchmany() """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT part_name, vendor_name
                    FROM parts
                    INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
                    INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
                    ORDER BY part_name;
                """)
                for row in iter_row(cur, 5):
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_part_vendors()
