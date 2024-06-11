"""Module for Kaprekar's Routine."""

def kaprekar_routine(numstr: str) -> str:
    """Performs Kaprekar Routine on a numeric string.

   """

    if not isinstance(numstr, str):
        raise ValueError('Argument should be a string.')

    if not numstr.isnumeric():
        raise ValueError('Argument should be a positive number.')

    if len(numstr) != 4:
        raise ValueError('Argument should be a four-digit number.')

    if len(set(numstr)) < 2:
        raise ValueError('Argument must consist of at least two different digits.')

    seq = []
    while numstr != '6174':
        seq.append(numstr)
        asc = ''.join(sorted(numstr))
        dsc = asc[::-1]
        diff = int(dsc) - int(asc)
        numstr = f'{diff:04}'

    seq.append(numstr)
    outstr = ", ".join(x for x in seq)
    return outstr

if __name__ == '__main__':
    arg = input('Enter a four-digit number with at least two different digits: ')
    print(kaprekar_routine(arg))