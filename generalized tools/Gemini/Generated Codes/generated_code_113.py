
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """

    output = []
    for i, string in enumerate(lst):
        odd_count = sum(int(digit) % 2 == 1 for digit in string)  # Count odd digits efficiently
        output_string = "the number of odd elements {count}n the str{count}ng {count} of the {count}nput.".format(count=odd_count)  # Format string with replacements
        output.append(output_string)

    return output

