import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Khem0055",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    
    # Fetch all users
    cur.execute("SELECT * FROM wild_mage_db.users;")
    users = cur.fetchall()
    print("Users in wild_mage_db:", users)

    cur.close()
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")