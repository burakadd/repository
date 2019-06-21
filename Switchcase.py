sum
multiply
join
union

negated: map(lambda i: -i, _arg),
inverted: map(lambda i: i**(-1), _arg),
squared: map(lambda i: i**2, _arg),

odds filter(lambda i: i % 2 == 1, _arg),
evens filter(lambda i: i % 2 == 0, _arg),
simples
