CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    feature1 FLOAT,
    feature2 FLOAT,
    label INT
);

INSERT INTO data (feature1, feature2, label) VALUES
(1.0, 2.0, 0),
(2.0, 1.0, 1),
(3.0, 3.0, 1);