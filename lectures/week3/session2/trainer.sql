SELECT * FROM trainingSchool.trainer;
SELECT * FROM trainer LEFT JOIN cohort ON trainer.id = cohort.trainer_id;
SELECT * FROM trainer LEFT JOIN cohort ON trainer.id = cohort.trainer_id WHERE trainer.id = 4;
INSERT INTO trainer (firstName, lastName, bio) VALUES ("Jane", "Doe", "The best trainer in the biz");
SELECT * FROM trainer JOIN cohort ON trainer.id = cohort.trainer_id;