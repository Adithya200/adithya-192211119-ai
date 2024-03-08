fact(disease(diabetes)).
fact(disease(hypertension)).
fact(disease(obesity)).
rule(eat_low_carb, [disease(diabetes)]).
rule(eat_low_sodium, [disease(hypertension)]).
rule(eat_low_calorie, [disease(obesity)]).
backward_chain(Query) :-
    rule(Query, Body),
      loop(Body),
    write(Query),
    write(' is recommended.'),
    nl.

loop([]).
loop([Condition|Body]) :-
    fact(Condition),
    loop(Body),
    !.
loop([Condition|Body]) :-
    backward_chain(Condition),
    loop(Body),
    !.

main :-

    write('Known Facts:'),
    nl,
    display_facts,
    write('Recommendations:'),
    nl,
    display_rules,
    backward_chain(recommendation),
    !.

display_facts :-
    fact(Fact),
    write(Fact),
    nl,
    fail.
display_rules :-
    rule(Head, Body),
    write('Rule: '),
    write(Head),
    write(' :- '),
    write(Body),
    nl,
    fail.
main :-
    write('Known Facts:'),
    nl,
    display_facts,
    write('Recommendations:'),
    nl,
    display_rules,
    backward_chain(recommendation),
    !.
