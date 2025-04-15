import psycopg2
from config import load_config

def insert_vendor(vendor_name):
    """ Insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

    vendor_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name,))
                rows = cur.fetchone()
                if rows:
                    vendor_id = rows[0]
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return vendor_id

def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, vendor_list)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_part(part_name):
    """ Insert a new part into the parts table """
    sql = """INSERT INTO parts(part_name)
             VALUES(%s) RETURNING part_id;"""

    part_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (part_name,))
                row = cur.fetchone()
                if row:
                    part_id = row[0]
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return part_id

def insert_many_parts(part_list):
    """ Insert multiple parts into the parts table """
    sql = "INSERT INTO parts(part_name) VALUES(%s)"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, part_list)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    # Insert one part
    insert_vendor("3M Co.")

    # Insert multiple parts
    insert_many_vendors([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])
    print("Done.")
