DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date text
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('apprenticeship', '2023-10-30');
INSERT INTO cohorts (name, starting_date) VALUES ('main bootcamp', '2023-10-30');
INSERT INTO cohorts (name, starting_date) VALUES ('DfE,', '2023-10-30');

INSERT INTO students (name, cohort_id) VALUES ('Dan', 1);
INSERT INTO students (name, cohort_id) VALUES ('John', 1);
INSERT INTO students (name, cohort_id) VALUES ('James', 1);
INSERT INTO students (name, cohort_id) VALUES ('Annabel', 1);
INSERT INTO students (name, cohort_id) VALUES ('Sarah', 2);
INSERT INTO students (name, cohort_id) VALUES ('Holly', 2);
INSERT INTO students (name, cohort_id) VALUES ('Amber', 2);
INSERT INTO students (name, cohort_id) VALUES ('George', 3);
INSERT INTO students (name, cohort_id) VALUES ('Jamie', 3);
INSERT INTO students (name, cohort_id) VALUES ('Josh', 3);
