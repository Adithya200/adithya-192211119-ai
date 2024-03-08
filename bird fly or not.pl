bird(penguin, false).
bird(sparrow, true).
bird(ostrich, false).
bird(eagle, true).

can_fly(Bird) :-
    bird(Bird, CanFly),
    CanFly.

cannot_fly(Bird) :-
    bird(Bird, CanFly),
    \+ CanFly.
