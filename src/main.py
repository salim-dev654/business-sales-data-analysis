from data_insert import insert_sample_data
from analysis import total_revenue, revenue_by_category, best_selling_products

def main():
    while True:
        print("""
====================================
BUSINESS SALES DATA ANALYSIS SYSTEM
====================================
1. Insert Sample Sales Data
2. Show Total Revenue
3. Revenue by Category
4. Best Selling Products
5. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
            insert_sample_data()
        elif choice == "2":
            total_revenue()
        elif choice == "3":
            revenue_by_category()
        elif choice == "4":
            best_selling_products()
        elif choice == "5":
            print("👋 Goodbye")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
