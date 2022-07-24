SELECT * FROM friendships_schema.friendships;
INSERT INTO friendships (user_id, friend_id) VALUES (1,2), (1,4), (1,6);
INSERT INTO friendships (user_id, friend_id) VALUES (2,1), (2,3), (2,5);
INSERT INTO friendships (user_id, friend_id) VALUES (3,2), (3,5);
INSERT INTO friendships (user_id, friend_id) VALUES (4,3);
INSERT INTO friendships (user_id, friend_id) VALUES (5,1), (5,6);
INSERT INTO friendships (user_id, friend_id) VALUES (6,2), (6,3);
SELECT COUNT(*) FROM friendships AS total_friendships;