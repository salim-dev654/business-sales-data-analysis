from db_connection import connect_db

def insert_sample_data():
    sales_data = [
        ("Laptop", "Electronics", 5, 3500, "2025-01-10"),
        ("Phone", "Electronics", 10, 1800, "2025-01-11"),
        ("Chair", "Furniture", 7, 600, "2025-01-12"),
        ("Desk", "Furniture", 4, 1200, "2025-01-13"),
        ("Printer", "Electronics", 3, 2500, "2025-01-14"),
        ("Tablet", "Electronics", 6, 1500, "2025-01-15")
    ]

    db = connect_db()
    cursor = db.cursor()

    cursor.executemany("""
    INSERT INTO sales (product_name, category, quantity, price, sale_date)
    VALUES (%s, %s, %s, %s, %s)
    """, sales_data)

    db.commit()
    db.close()

    print("✅ Sample sales data inserted")
