import psycopg2
from db_config import posts_db_connection_string

conn = psycopg2.connect(posts_db_connection_string)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS postUsers (
        userID SERIAL NOT NULL UNIQUE,
        firstName varchar(40) NOT NULL,
        lastName varchar(40) NOT NULL,
        isAdmin boolean NOT NULL,
        CONSTRAINT primaryKeyUserID PRIMARY KEY (userID)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS postTypes (
        postTypeID SERIAL NOT NULL UNIQUE,
        postTypeName varchar(20) NOT NULL,
        CONSTRAINT primaryKeyPostTypeID PRIMARY KEY (postTypeID)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        postID SERIAL NOT NULL UNIQUE,
        userID integer NOT NULL,
        postTypeID integer NOT NULL,
        postContent varchar(500) NOT NULL,
        creationDT timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT primaryKeyPostID PRIMARY KEY (postID),
        CONSTRAINT foreignKeyUserID FOREIGN KEY (userID) REFERENCES users,
        CONSTRAINT foreignKeyPostTypeID FOREIGN KEY (postTypeID) REFERENCES postTypes
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS socialPosts (
        socialPostID SERIAL NOT NULL UNIQUE,
        postID integer NOT NULL,
        CONSTRAINT foreignKeyPostID FOREIGN KEY (postID) REFERENCES posts
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS jobPosts (
        jobPostID SERIAL NOT NULL UNIQUE,
        postID integer NOT NULL,
        company varchar(40) NOT NULL,
        hiringDate date NOT NULL,
        CONSTRAINT foreignKeyPostID FOREIGN KEY (postID) REFERENCES posts
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS commentPosts (
        commentPostID SERIAL NOT NULL UNIQUE,
        postID integer NOT NULL,
        CONSTRAINT foreignKeyPostID FOREIGN KEY (postID) REFERENCES posts
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS eventPosts (
        eventPostID SERIAL NOT NULL UNIQUE,
        postID integer NOT NULL,
        title varchar(40) NOT NULL,
        location varchar(60) NOT NULL,
        address varchar(80) NOT NULL,
        startDT timestamp NOT NULL,
        endDT timestamp NOT NULL,
        CONSTRAINT foreignKeyPostID FOREIGN KEY (postID) REFERENCES posts
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS likes (
        likeID SERIAL NOT NULL UNIQUE,
        postID integer NOT NULL,
        userID integer NOT NULL,
        CONSTRAINT foreignKeyPostID FOREIGN KEY (postID) REFERENCES posts,
        CONSTRAINT foreignKeyUserID FOREIGN KEY (userID) REFERENCES users
    );
""")

conn.commit()
cur.close()
conn.close()