CREATE TABLE IF NOT EXISTS photos (
                        album_id TEXT,
                        date TEXT,
                        id INTEGER PRIMARY KEY,
                        owner_id INTEGER,
                        has_tags TEXT,
                        height INTEGER,
                        photo_1280 TEXT,
                        photo_130 TEXT,
                        photo_604 TEXT,
                        photo_75 TEXT,
                        photo_807 TEXT,
                        post_id INTEGER,
                        text TEXT,
                        width INTEGER,
                        photo BLOB
)