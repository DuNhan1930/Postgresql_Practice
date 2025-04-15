import psycopg2
from config_tiki import load_config_tiki

def create_tables():
    """ Create tables in the PostgreSQL database """
    commands = (
        """
        CREATE TABLE products (
            product_id BIGINT PRIMARY KEY, 
            name TEXT,
            url_key TEXT UNIQUE,
            price INTEGER, 
            description TEXT
        );
        """,
        """
        CREATE TABLE product_images (
            id SERIAL PRIMARY KEY,
            product_id BIGINT REFERENCES products(product_id),
            image_url TEXT
        );
        """
    )
    try:
        config = load_config_tiki()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                print("Tables created successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)

if __name__ == '__main__':
    create_tables()
