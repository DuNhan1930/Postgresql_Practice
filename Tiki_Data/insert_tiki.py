import psycopg2
from config_tiki import load_config_tiki
import ijson

def insert_product_with_images(product):
    """
    Insert a product and its images into two related tables: products and product_images
    """
    config = load_config_tiki()

    product_sql = """
        INSERT INTO products(product_id, name, url_key, price, description)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING product_id;
    """

    image_sql = """
        INSERT INTO product_images(product_id, image_url)
        VALUES (%s, %s);
    """

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Insert into products table
                cur.execute(product_sql, (
                    product['id'],
                    product['name'],
                    product['url_key'],
                    product['price'],
                    product['description']
                ))
                product_id = cur.fetchone()[0]

                # Insert each image into product_images
                for img_url in product['images']:
                    cur.execute(image_sql, (product_id, img_url))

            conn.commit()
            print(f"Inserted product {product_id} with {len(product['images'])} images.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

if __name__ == '__main__':
    for file_index in range(0, 201):
        with open(f"/home/dunhan/PycharmProjects/Tiki_Crawling/tiki_data/tiki_products_{file_index}.json", 'r') as file:
            for item in ijson.items(file, 'item'):
                insert_product_with_images(item)
        print(f"Inserted tiki_products_{file_index}.json")