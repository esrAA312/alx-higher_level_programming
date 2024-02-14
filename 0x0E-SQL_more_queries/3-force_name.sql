-- Create or update the force_name table if it does not exist
USE hbtn_0d_2;

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
