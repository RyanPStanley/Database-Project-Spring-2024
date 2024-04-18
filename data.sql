drop database GameSales;
create database GameSales;
use GameSales;

CREATE TABLE Game (
    GameName VARCHAR(100) UNIQUE NOT NULL,
    Generation TINYINT UNSIGNED NOT NULL DEFAULT 1 CHECK (Generation >= 1 AND Generation <= 9),
    ReleaseYear SMALLINT UNSIGNED NOT NULL DEFAULT 2000 CHECK (ReleaseYear >= 1996),
    Platform VARCHAR(6) NOT NULL CHECK (Platform IN ('GB' , 'GBC', 'GBA', 'DS', '3DS', 'Switch')),
    PRIMARY KEY (GameName)
);

CREATE TABLE Rating (
    GameName VARCHAR(100) PRIMARY KEY UNIQUE NOT NULL,
    RatingNumber DECIMAL(2 , 1 ) NOT NULL DEFAULT 0.0 CHECK (RatingNumber >= 0.0
        AND RatingNumber <= 10.0),
    ReviewDate DATE DEFAULT 20000101,
    FOREIGN KEY (GameName)
        REFERENCES Game (GameName)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Sales (
    GameName VARCHAR(100) PRIMARY KEY UNIQUE NOT NULL,
    UnitSales INT UNSIGNED NOT NULL DEFAULT 0,
    AllTimeSales INT UNSIGNED NOT NULL DEFAULT 0,
    FOREIGN KEY (GameName)
        REFERENCES Game (GameName)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

INSERT INTO Game(GameName, Generation, ReleaseYear, Platform)
VALUES ('Pokemon Red & Blue', 1, 1996, 'GB'),
    ('Pokemon Yellow', 1, 1998, 'GB'),
    ()