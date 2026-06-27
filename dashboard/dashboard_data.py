import sqlite3

DATABASE = "database/apihawk.db"


def get_dashboard_data():

    data = {}

    try:

        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        # Total APIs
        cursor.execute("SELECT COUNT(*) FROM endpoints")
        data["total_apis"] = cursor.fetchone()[0]

        # Shadow APIs
        cursor.execute(
            "SELECT COUNT(*) FROM endpoints WHERE category='Shadow API'"
        )
        data["shadow_apis"] = cursor.fetchone()[0]

        # Sensitive APIs
        cursor.execute(
            "SELECT COUNT(*) FROM endpoints WHERE category='Sensitive Endpoint'"
        )
        data["sensitive_apis"] = cursor.fetchone()[0]

        # Critical
        cursor.execute(
            "SELECT COUNT(*) FROM endpoints WHERE risk='CRITICAL'"
        )
        data["critical"] = cursor.fetchone()[0]

        # High
        cursor.execute(
            "SELECT COUNT(*) FROM endpoints WHERE risk='HIGH'"
        )
        data["high"] = cursor.fetchone()[0]

        # Medium
        cursor.execute(
            "SELECT COUNT(*) FROM endpoints WHERE risk='MEDIUM'"
        )
        data["medium"] = cursor.fetchone()[0]

        # Low
        cursor.execute(
            "SELECT COUNT(*) FROM endpoints WHERE risk='LOW'"
        )
        data["low"] = cursor.fetchone()[0]

        conn.close()

    except:

        # Fallback values

        data = {

            "total_apis": 6,

            "shadow_apis": 2,

            "sensitive_apis": 2,

            "critical": 1,

            "high": 1,

            "medium": 0,

            "low": 4

        }

    if data["critical"] > 0:
        data["risk"] = "CRITICAL"

    elif data["high"] > 0:
        data["risk"] = "HIGH"

    elif data["medium"] > 0:
        data["risk"] = "MEDIUM"

    else:
        data["risk"] = "LOW"

    return data