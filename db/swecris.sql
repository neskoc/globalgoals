BEGIN TRANSACTION;
DROP TABLE IF EXISTS "swecris";
CREATE TABLE IF NOT EXISTS "swecris" (
	"index"	BIGINT,
	"diarienr"	TEXT,
	"title"	TEXT,
	"abstract"	TEXT,
	"organization"	TEXT,
	"Formas1"	INTEGER,
	"Self1"	INTEGER
);
DROP INDEX IF EXISTS "ix_swecris_index";
CREATE INDEX IF NOT EXISTS "ix_swecris_index" ON "swecris" (
	"index"
);
COMMIT;
