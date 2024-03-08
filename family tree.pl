parent(john, ann).
parent(john, bob).
parent(mary, ann).
parent(mary, bob).
parent(bob, jim).
parent(ann, pat).

male(john).
male(bob).
male(jim).

female(mary).
female(ann).
female(pat).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

uncle(X, Y) :- male(X), sibling(X, Z), parent(Z, Y).

cousin(X, Y) :- uncle(Z, X), parent(Z, Y).
