INSERT INTO user_types (name) VALUES ("Student");
INSERT INTO user_types (name) VALUES ("Teacher");

INSERT INTO users (first_name, last_name, active, profile) VALUES ("Dmitrii", "Beliakov", 1, (SELECT id FROM user_types WHERE name = "Teacher"));
INSERT INTO users (first_name, last_name, active, profile) VALUES ("Kamil", "Talipov", 1, (SELECT id FROM user_types WHERE name = "Teacher"));
INSERT INTO users (first_name, last_name, active, profile) VALUES ("Ivan", "Ivanov", 0, (SELECT id FROM user_types WHERE name = "Student"));
INSERT INTO users (first_name, last_name, active, profile) VALUES ("Petr", "Petrov", 0, (SELECT id FROM user_types WHERE name = "Student"));
INSERT INTO users (first_name, last_name, active, profile) VALUES ("Petr", "Sidorov", 0, (SELECT id FROM user_types WHERE name = "Student"));
