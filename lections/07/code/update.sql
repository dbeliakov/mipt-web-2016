UPDATE users SET profile = (SELECT id FROM user_types WHERE name = "Student") WHERE first_name = "Dmitrii" AND last_name = "Beliakov";
