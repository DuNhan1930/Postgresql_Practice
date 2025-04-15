import psycopg2
from config_tiki import load_config_tiki


def delete_part(part_id):
    """ Delete part by part id """

    rows_deleted  = 0
    sql = 'DELETE FROM parts WHERE part_id = %s'
    config = load_config_tiki()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (part_id,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted

if __name__ == '__main__':
    for i in range(1, 7):
        deleted_rows = delete_part(i)
        print('The number of deleted rows: ', deleted_rows)