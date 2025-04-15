import psycopg2
from config import load_config


def update_vendor(vendor_id, vendor_name):
    """ Update vendor name based on the vendor id """

    updated_row_count = 0

    sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                # execute the UPDATE statement
                cur.execute(sql, (vendor_name, vendor_id))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

def update_parts(part_id, part_name):
    """ Update vendor name based on the vendor id """

    updated_row_count = 0

    sql = """ UPDATE parts
                SET part_id = %s
                WHERE part_name = %s"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                # execute the UPDATE statement
                cur.execute(sql, (part_id, part_name))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

if __name__ == '__main__':
    update_vendor(1, "3M Corp")
    ls_part_name = ["SIM Tray", "Speaker", "Vibrator", "Antenna", "Home Button", "LTE Modem", "OLED"]
    for i in range(1, 8):
        update_parts(i, ls_part_name[i - 1])

