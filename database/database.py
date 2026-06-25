import sqlite3


def initialize_database():
    conn = sqlite3.connect("database/apihawk.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scan_results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        endpoint TEXT,
        category TEXT,
        risk TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_scan(endpoint, category, risk):
    conn = sqlite3.connect("database/apihawk.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scan_results(endpoint, category, risk) VALUES (?, ?, ?)",
        (endpoint, category, risk)
    )

    conn.commit()
    conn.close()


def display_results():
    conn = sqlite3.connect("database/apihawk.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scan_results")

    rows = cursor.fetchall()

    print("=" * 60)
    print("APIHAWK DATABASE RESULTS")
    print("=" * 60)

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":

    initialize_database()

    save_scan("/login", "Sensitive Endpoint", "HIGH")
    save_scan("/admin/debug", "Shadow API", "CRITICAL")
    save_scan("/patients", "Normal API", "LOW")

    display_results()