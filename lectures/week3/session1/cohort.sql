SELECT * FROM trainingSchool.cohort;
INSERT INTO cohort (className, topicSkill, classLength, trainer_id) VALUES ("GreenClass", "Health", "15 weeks", 1);
INSERT INTO cohort (className, topicSkill, classLength, trainer_id) VALUES ("Purple", "Planting", "16 weeks", 2);
UPDATE cohort SET trainer_id=4 WHERE id=2;
UPDATE cohort SET classLength="12 weeks" WHERE id=2;
INSERT INTO cohort (className, topicSkill, classLength, trainer_id) VALUES ("Gardening with Melissa", "Planting", "2 weeks", 2);
UPDATE cohort SET className="Nutrition with Melissa", topicSkill="Nutrition" WHERE id=3;