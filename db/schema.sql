DROP TABLE IF EXISTS results;

CREATE TABLE results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    tag TEXT NOT NULL,
    url TEXT NOT NULL,
    created timestamp DATE DEFAULT (datetime('now','localtime'))
);