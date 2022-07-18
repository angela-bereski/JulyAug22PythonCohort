SELECT * FROM owner;
INSERT INTO owner (firstName, lastName) VALUES ("Arvel", "Cavitt");
INSERT INTO owner (firstName, lastName) VALUES ("Bernard", "Olaires");
select * from owner left join pet on owner.id = pet.owner_id;