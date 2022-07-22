SELECT * FROM ourpets.species;
select * from species left join pet on species.id = pet.species_id left join owner on pet.owner_id = owner.id;