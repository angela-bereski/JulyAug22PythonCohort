SELECT * FROM trainingSchool.trainer;
INSERT INTO trainer (firstName, lastName, bio) values ("Ashley", "Diaz", "Has a night job as a Phlebotomist while learning to code during the day");
INSERT INTO trainer (firstName, lastName, bio) values ("Missy", "Longenberger", "Instructor alla Python");
SELECT * FROM trainer WHERE id=2;
UPDATE trainer SET firstName="Melissa" WHERE id=2;
DELETE FROM trainer WHERE id=3;
INSERT INTO trainer (firstName, lastName, bio) values ("Justina", "Gray", "TA alla Python");