DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS tags;
DROP SEQUENCE IF EXISTS tags_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date text
);

CREATE SEQUENCE IF NOT EXISTS tags_id_seq;
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name text,
  post_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);

INSERT INTO posts (name, starting_date) VALUES ('apprenticeship', '2023-10-30');
INSERT INTO posts (name, starting_date) VALUES ('main bootcamp', '2023-10-30');
INSERT INTO posts (name, starting_date) VALUES ('DfE,', '2023-10-30');

INSERT INTO tags (name, post_id) VALUES ('Dan', 1);
INSERT INTO tags (name, post_id) VALUES ('John', 1);
INSERT INTO tags (name, post_id) VALUES ('James', 1);
INSERT INTO tags (name, post_id) VALUES ('Annabel', 1);
INSERT INTO tags (name, post_id) VALUES ('Sarah', 2);
INSERT INTO tags (name, post_id) VALUES ('Holly', 2);
INSERT INTO tags (name, post_id) VALUES ('Amber', 2);
INSERT INTO tags (name, post_id) VALUES ('George', 3);
INSERT INTO tags (name, post_id) VALUES ('Jamie', 3);
INSERT INTO tags (name, post_id) VALUES ('Josh', 3);
