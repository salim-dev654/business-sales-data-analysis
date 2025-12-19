from db_connection import connect_db

def total_revenue():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT SUM(quantity * price) FROM sales")
    revenue = cursor.fetchone()[0]
    print(f"\n💰 TOTAL REVENUE: {revenue}")
    db.close()

def revenue_by_category():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT category, SUM(quantity * price) AS revenue
        FROM sales
        GROUP BY category
        ORDER BY revenue DESC
    """)
    print("\n📊 REVENUE BY CATEGORY")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]}")
    db.close()

def best_selling_products():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT product_name, SUM(quantity)
        FROM sales
        GROUP BY product_name
        ORDER BY SUM(quantity) DESC
    """)
    print("\n🔥 BEST SELLING PRODUCTS")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} units")
    db.close()
