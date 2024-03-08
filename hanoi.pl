hanoi(0, _, _).
hanoi(N, A, C) :-
    N > 0,
    M is N - 1,
    hanoi(M, A, B),
    move_disk(A, C, N),
    hanoi(M, B, C).

move_disk(A, C, N) :-
    write('Move disk '),
    write(N),
    write(' from rod '),
    write(A),
    write(' to rod '),
    write(C),
    nl.
