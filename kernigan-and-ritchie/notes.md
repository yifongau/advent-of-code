# printf tricks

`printf` has a number of available substitution tokens, depending on the kind
of value you wish to print: %d for int, %f for float, %s for string,  %c for
character, etc. You also can set the width of the substitution, for more neatly
formatted data:

`printf("%3d %6d"), x, y)` 


For floats you can use the following notation to set the # of characters after
the decimal point:

`%6.2f`

This means that the float should be at least six characters wide, but at
maximum 2 characters after the decimal point. 


