-- Lab 8 assignment by Chris Reutz
-- SQLite user creation and blog post statements

CREATE TABLE IF NOT EXISTS user (
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL
);

INSERT INTO user (userId,user_name) VALUES (1,'Bob'),(2,'Alice'),(3,'Sydney'),(4,'Chris');

-- CREATE THE vw_users VIEW HERE
CREATE VIEW IF NOT EXISTS vw_users AS 
    SELECT
        userId AS Id, 
        user_name AS User
    FROM user;

CREATE TABLE IF NOT EXISTS blog_posts (
    postId INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER NOT NULL REFERENCES user(userId),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    post_message TEXT NOT NULL
);

-- CREATE INSERTS FOR THE blog_posts TABLE HERE
INSERT INTO blog_posts (userId,post_message) VALUES (2, 'Hello Class!');
INSERT INTO blog_posts (userId,post_message) VALUES (1, 'Kilroy was here!');
INSERT INTO blog_posts (userId,post_message) VALUES (3, 'Hello mate');
INSERT INTO blog_posts (userId,post_message) VALUES (2, 'Today was a sunny day');
INSERT INTO blog_posts (userId,post_message) VALUES (4, 'It''s such a fine line between stupid and clever.');
INSERT INTO blog_posts (userId,post_message) VALUES (4, 'Try not. Do or do not. There is no try.');

-- CREATE THE VIEW vw_posts HERE. THE VIEW SHOULD 
-- INCLUDE THE userId, user_name, created_at, and message

CREATE VIEW vw_posts AS
    SELECT
        u.userId AS Id,
        u.user_name AS User,
        p.created_at,
        p.post_message
    FROM
        blog_posts AS p
    JOIN
        user AS u
    ON
        p.userId = u.userId;