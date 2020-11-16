BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Goals";
CREATE TABLE IF NOT EXISTS "Goals" (
	"Id"	INTEGER NOT NULL DEFAULT 0,
	"Name"	TEXT NOT NULL DEFAULT '',
	"Description"	TEXT,
	PRIMARY KEY("Id")
);
COMMIT;
