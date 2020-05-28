CREATE TABLE IF NOT EXISTS photos (
                        album_id TEXT,
                        date TEXT,
                        id INTEGER,
                        owner_id INTEGER,
                        has_tags TEXT,
                        height INTEGER,
                        source_1280_link TEXT,
                        source_130_link TEXT,
                        source_604_link TEXT,
                        source_75_link TEXT,
                        source_807_link TEXT,
                        post_id INTEGER,
                        text TEXT,
                        width INTEGER,
                        photo BLOB
)