SELECT * FROM books_schema.books;
INSERT INTO books (title) VALUES ('C Sharp'), ('Java'), ('Python'), ('PHP'), ('Ruby');
UPDATE books SET title = 'C#' WHERE id = 1;
SELECT * FROM books
LEFT JOIN favorites ON books.id = favorites.book_id
LEFT JOIN users ON users.id = favorites.user_id;