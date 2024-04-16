drop database GameSales;
create database GameSales;
use GameSales;

CREATE TABLE Game (
    GameName VARCHAR(100) UNIQUE NOT NULL,
    Generation INT UNSIGNED,
    ReleaseYear SMALLINT UNSIGNED,
    Platform VARCHAR(100),
    PRIMARY KEY (GameName)
);

CREATE TABLE Rating (
    GameName VARCHAR(100) UNIQUE NOT NULL,
    RatingNumber DECIMAL(2 , 1 ),
    ReviewDate DATE,
    FOREIGN KEY (GameName)
        REFERENCES Game (GameName)
);

CREATE TABLE Sales (
    GameName VARCHAR(100) UNIQUE NOT NULL,
    InitialSales INT UNSIGNED,
    AllTimeSales INT UNSIGNED,
    FOREIGN KEY (GameName)
        REFERENCES Game (GameName)
);
