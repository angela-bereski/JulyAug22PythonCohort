SELECT * FROM friendships_schema.users;
INSERT INTO users (first_name, last_name) VALUES ('Amy', 'Giver'), ('Big', 'Bird'), ('Joe', 'Schmoe'), ('Eli', 'Byers'), ('Marky', 'Mark'), ('Kermit', 'The Frog');
SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name FROM users JOIN friendships ON users.id=friendships.user_id LEFT JOIN users as users2 ON users2.id = friendships.friend_id;
SELECT users2.first_name, users2.last_name, users.first_name AS friend FROM users JOIN friendships ON users.id=friendships.user_id LEFT JOIN users AS users2 ON users2.id = friendships.friend_id WHERE users.id = 1;
