import sqlite3

def main():
    # Připojení k SQLite databázi (v paměti)
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # --- Vytvoření tabulek (podle task_tables.py) ---
    users_create_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """

    rooms_create_table = """
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """

    messages_create_table = """
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (room_id) REFERENCES rooms(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """

    cursor.executescript(users_create_table)
    cursor.executescript(rooms_create_table)
    cursor.executescript(messages_create_table)

    # --- Vložení dat (podle task_data.py) ---
    insert_users = """
    INSERT INTO users (username, password) VALUES
    ('user1', 'password1'),
    ('user2', 'password2'),
    ('user3', 'password3');
    """

    insert_rooms = """
    INSERT INTO rooms (name) VALUES
    ('room1'),
    ('room2'),
    ('room3');
    """

    insert_messages = """
    INSERT INTO messages (room_id, user_id, message) VALUES
    (1, 1, 'Ahoj, ako sa máte?'),
    (1, 1, 'Dobre ráno všetkým!'),
    (1, 2, 'Dobré popoludnie!'),
    (2, 3, 'Ahojte, čo sa deje?'),
    (2, 1, 'Som tu!'),
    (2, 2, 'Ahoj, ako sa máte?'),
    (3, 3, 'Tento chat je skvelý!');
    """

    cursor.executescript(insert_users)
    cursor.executescript(insert_rooms)
    cursor.executescript(insert_messages)
    connection.commit()

    # --- Úkol 1: Najít uživatele, kteří poslali zprávy do místnosti "room1" ---
    print("Task 1: Users who sent messages to room1")
    query1 = """
    SELECT DISTINCT u.username
    FROM users u
    JOIN messages m ON u.id = m.user_id
    JOIN rooms r ON m.room_id = r.id
    WHERE r.name = 'room1';
    """
    for row in cursor.execute(query1):
        print(row[0])
    print("-" * 40)

    # --- Úkol 2: Spočítat, kolik různých uživatelů poslalo zprávy do jednotlivých místností ---
    print("Task 2: Count of distinct users per room")
    query2 = """
    SELECT r.name, COUNT(DISTINCT m.user_id) AS user_count
    FROM rooms r
    JOIN messages m ON r.id = m.room_id
    GROUP BY r.name;
    """
    for row in cursor.execute(query2):
        print(f"Room: {row[0]}, Number of users: {row[1]}")
    print("-" * 40)

    # --- Úkol 3: Najít místnosti, do kterých konkrétní uživatel (user2) poslal zprávy ---
    print("Task 3: Rooms where user2 sent messages")
    query3 = """
    SELECT DISTINCT r.name
    FROM rooms r
    JOIN messages m ON r.id = m.room_id
    JOIN users u ON m.user_id = u.id
    WHERE u.username = 'user2';
    """
    for row in cursor.execute(query3):
        print(row[0])
    print("-" * 40)

    # --- Úkol 4: Zobrazit počet zpráv, které poslal každý uživatel ---
    print("Task 4: Number of messages per user")
    query4 = """
    SELECT u.username, COUNT(m.id) AS message_count
    FROM users u
    LEFT JOIN messages m ON u.id = m.user_id
    GROUP BY u.username;
    """
    for row in cursor.execute(query4):
        print(f"User: {row[0]}, Message count: {row[1]}")
    print("-" * 40)

    # --- Úkol 5: Zobrazit seznam místností spolu s počtem zpráv, které poslali jednotliví uživatelé ---
    print("Task 5: Rooms with the number of messages per user")
    query5 = """
    SELECT r.name AS room, u.username, COUNT(m.id) AS message_count
    FROM rooms r
    JOIN messages m ON r.id = m.room_id
    JOIN users u ON m.user_id = u.id
    GROUP BY r.name, u.username;
    """
    for row in cursor.execute(query5):
        print(f"Room: {row[0]}, User: {row[1]}, Message count: {row[2]}")

    connection.close()

if __name__ == "__main__":
    main()
