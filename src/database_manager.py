import sqlite3

DATABASE = "database/apihawk.db"


def connect():
    return sqlite3.connect(DATABASE)


def create_table():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS endpoints(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        endpoint TEXT,
        method TEXT,
        category TEXT,
        risk TEXT

    )
    """)

    conn.commit()
    conn.close()


def clear_old_scan():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM endpoints")

    conn.commit()
    conn.close()


def insert_endpoint(endpoint, method, category, risk):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO endpoints
    (endpoint,method,category,risk)

    VALUES(?,?,?,?)

    """, (endpoint, method, category, risk))

    conn.commit()
    conn.close()


def fetch_all():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT endpoint,
           method,
           category,
           risk

    FROM endpoints

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def statistics():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM endpoints")
    total = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM endpoints
    WHERE category='Sensitive Endpoint'
    """)
    sensitive = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM endpoints
    WHERE category='Shadow API'
    """)
    shadow = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM endpoints
    WHERE risk='CRITICAL'
    """)
    critical = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM endpoints
    WHERE risk='HIGH'
    """)
    high = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM endpoints
    WHERE risk='LOW'
    """)
    low = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "sensitive": sensitive,
        "shadow": shadow,
        "critical": critical,
        "high": high,
        "low": low
    }
def create_log_table():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS log_endpoints(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        method TEXT,
        endpoint TEXT

    )
    """)

    conn.commit()
    conn.close()


def insert_log_endpoint(method, endpoint):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO log_endpoints(method, endpoint)
    VALUES(?, ?)
    """, (method, endpoint))

    conn.commit()
    conn.close()


def fetch_log_endpoints():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT method, endpoint
    FROM log_endpoints
    ORDER BY endpoint
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows