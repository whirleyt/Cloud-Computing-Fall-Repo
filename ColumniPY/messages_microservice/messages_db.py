import psycopg2
from db_config import messages_db_connection_string


conn = psycopg2.connect(messages_db_connection_string)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS messageUsers (
        userID SERIAL NOT NULL UNIQUE,
        firstName varchar(40) NOT NULL,
        lastName varchar(40) NOT NULL,
        isAdmin boolean NOT NULL,
        CONSTRAINT primaryKeyUserID PRIMARY KEY (userID)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS messageThread (
        messageThreadID SERIAL NOT NULL UNIQUE,
        creationDT timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT primaryKeyMessageID PRIMARY KEY (messageThreadID)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS userMessages (
        userMessageID SERIAL NOT NULL UNIQUE,
        senderID integer NOT NULL,
        receiverID integer,
        messageThreadID integer NOT NULL,
        messageContents varchar(500),
        isGroupMessage boolean NOT NULL,
        creationDT timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT primaryKeyUserMessageID PRIMARY KEY (userMessageID),
        CONSTRAINT foreignKeySenderID FOREIGN KEY (senderID) REFERENCES users(userID),
        CONSTRAINT foreignKeyReceiverID FOREIGN KEY (receiverID) REFERENCES users(userID),
        CONSTRAINT foreignKeyMessageThreadID FOREIGN KEY (messageThreadID) REFERENCES messageThread(messageThreadID)
    );
""")

conn.commit()
cur.close()
conn.close()