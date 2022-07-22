SELECT * FROM ourpets.owner;
select * from owner left join pet on owner.id = pet.owner_id left join species on pet.species_id = species.id;