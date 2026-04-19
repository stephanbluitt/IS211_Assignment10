-- Drop tables if they already exist to prevent errors on multiple runs
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

-- Create the artists table
CREATE TABLE artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Create the albums table, linking to the artists table
CREATE TABLE albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists (id)
);

-- Create the songs table, linking to the albums table
CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    album_id INTEGER,
    track_number INTEGER,
    length_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums (id)
);
