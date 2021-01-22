
DROP TABLE IF EXISTS pr_pl;
DROP TABLE IF EXISTS pro_lang;
DROP TABLE IF EXISTS project;

CREATE TABLE "pro_lang" (
  "language_id" integer PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
  "name" text NOT NULL UNIQUE
);

CREATE TABLE "project" (
  "project_id" integer PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
  "name" text NOT NULL UNIQUE,
  "description" text, -- may be null
  "url" text NOT NULL,
  "initial_stars" integer NOT NULL,
  "current_stars" integer NOT NULL,
  "add_time" timestamptz NOT NULL DEFAULT NOW(),
  "initial_fork_count" integer NOT NULL,
  "current_fork_count" integer NOT NULL
);

CREATE TABLE "pr_pl" (
  "pl_id" integer REFERENCES pro_lang(language_id) ON UPDATE CASCADE ON DELETE CASCADE,
  "pr_id" integer REFERENCES project(project_id) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT "pr_pl_pkey" PRIMARY KEY (pl_id, pr_id)
);

-- Indexes
CREATE INDEX prolang_index on pro_lang(name);
CREATE INDEX project_index on project(name, current_stars)
