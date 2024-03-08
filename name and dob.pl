person(john, date(1990, 1, 10)).
person(jane, date(1985, 5, 15)).
person(jim, date(1995, 12, 25)).
name(Person, Name) :
    person(Name, _),
    Name = Person.
dob(Person, DOB) :-
    person(_, DOB),
    Person = Person.
