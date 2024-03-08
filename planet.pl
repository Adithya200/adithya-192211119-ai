planet(mercury, 0.39, 57.9).
planet(venus, 0.72, 108.2).
planet(earth, 1.00, 149.6).
planet(mars, 1.52, 227.9).
planet(jupiter, 5.20, 778.3).
planet(saturn, 9.58, 1427.0).
planet(uranus, 19.18, 2871.0).
planet(neptune, 30.07, 4498.0).

name(Planet, Name) :-
    planet(Name, _, _),
    Name = Planet.

distance(Planet, Distance) :-
    planet(_, _, Distance),
    Planet = Planet.

mass(Planet, Mass) :-
    planet(Planet, Mass, _),
    Planet = Planet.
