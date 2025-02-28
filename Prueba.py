import mysql.connector
import os

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", ""),
    "database": os.getenv("DB_NAME", "mi_bd"),
    "port": 3306
}

try:
    conn = mysql.connector.connect(**db_config)
    print("✅ Conexión exitosa a MySQL")
    conn.close()
except Exception as e:
    print(f"❌ Error al conectar: {e}")
