Create table Game (
    GameName varchar unique not null,
    Region varchar,
    Generation unsigned int,
    ReleaseYear unsigned smallint,
    Platform varchar,
    primary key (GameName)
);

Create Table Rating (
    GameName varchar unique not null,
    RatingNumber decimal(2,1),
    Reviewer varchar,
    ReviewDate date,
    foreign key (GameName) references Game(GameName)
);

Create Table Sales (
    GameName varchar unique not null,
    InitialSales int unsigned,
    AllTimeSales int unsigned,
    foreign key (GameName) references Game(GameName)
);
