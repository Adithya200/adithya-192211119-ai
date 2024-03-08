student(john, cs).
student(sarah, math).
student(tom, physics).

teacher(alice, cs).
teacher(bob, math).
teacher(charlie, physics).

sub_code(cs, csci101).
sub_code(math, math101).
sub_code(physics, phys101).

student(Person) :-
    student(Person, _).

teacher(Person) :-
    teacher(Person, _).

sub(Student, Subject) :-
    student(Student, Subject).

sub(Teacher, Subject) :-
    teacher(Teacher, Subject).

sub_code(Subject, Code) :-
    sub_code(Subject, Code).
