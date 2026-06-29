DROP TABLE IF EXISTS data;

CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    age INT,
    pressure INT,
    cholesterol INT,
    target INT
);

INSERT INTO data (age, pressure, cholesterol, target) VALUES
(20, 120, 200, 0),
(30, 130, 220, 1),
(40, 140, 240, 1),
(50, 150, 260, 1),
(60, 160, 280, 0);