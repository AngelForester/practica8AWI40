import mysql.connector
import os

db_config = {
    "host": os.getenv("82.197.82.90"),
    "user": os.getenv("u861594054_Misael2009"),
    "password": os.getenv("NZqhQyiNZ3Tg8JJ"),
    "database": os.getenv("u861594054_app9"),
    "port": 3306
}

try:
    conn = mysql.connector.connect(**db_config)
    print("✅ Conexión exitosa a MySQL")
    conn.close()
except Exception as e:
    print(f"❌ Error al conectar: {e}")
