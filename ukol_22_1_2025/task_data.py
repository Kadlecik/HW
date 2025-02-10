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