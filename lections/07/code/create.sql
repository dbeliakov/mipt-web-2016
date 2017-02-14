CREATE TABLE user_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    active BOOLEAN,
    profile INTEGER,
    FOREIGN KEY(profile) REFERENCES user_types(id)
);
     
