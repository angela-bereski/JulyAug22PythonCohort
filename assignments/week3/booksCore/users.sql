SELECT * FROM books_schema.users;
INSERT INTO users (first_name, last_name) VALUES ('Jane', 'Amsden'), ('Emily', 'Dixon'), ('Theodore', 'Dostoevsky'), ('William', 'Shapiro'), ('Lao', 'Xiu');
UPDATE users SET first_name = 'Bill' WHERE id = 4;
SELECT * FROM users
LEFT JOIN favorites ON users.id = favorites.user_id
LEFT JOIN books ON books.id = favorites.book_id;