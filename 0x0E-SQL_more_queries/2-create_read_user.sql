-- creates the db and the user
-- creates db
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grants SELECT privileges
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
