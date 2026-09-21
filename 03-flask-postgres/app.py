from flask import Flask, request
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host="postgres",
        database="flaskdb",
        user="flaskuser",
        password="flaskpassword"
    )


def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
    """)

    connection.commit()

    cursor.close()
    connection.close()


@app.route("/")
def home():
    return "Hello from Flask + PostgreSQL!"


@app.route("/users", methods=["GET"])
def users():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return str(users)


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data["name"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (name) VALUES (%s)",
        (name,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return "User added successfully!"


create_table()

app.run(host="0.0.0.0", port=5000)