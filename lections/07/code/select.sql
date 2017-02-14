SELECT * FROM users, user_types;

SELECT user_types.name, users.first_name, users.last_name FROM users, user_types WHERE users.profile = user_types.id;

SELECT COUNT(*) FROM users WHERE profile = (SELECT id FROM user_types WHERE name = "Student");

SELECT COUNT(*), active FROM users GROUP BY active;

SELECT COUNT(*), active FROM users GROUP BY active HAVING COUNT(*) > 2;

SELECT COUNT(*), user_types.name FROM users, user_types WHERE users.profile = user_types.id GROUP BY user_types.name;
