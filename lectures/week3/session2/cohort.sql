SELECT * FROM trainingSchool.cohort;
INSERT INTO cohort (className, topicSkill, classLength, trainer_id) VALUES ("Obstacle Course Training", "Agility", "4 weeks", 4);
delete from cohort where id=5;
delete from cohort where id=6;
delete from cohort where id=7;
delete from cohort where id=8;
select * from cohort left join trainer on cohort.trainer_id = trainer.id;