
def correct_bracketing(brackets: str) -> bool:
    """Checks if a string of "<" and ">" brackets has correct pairing."""

    stack = []  # Use a stack to track opening brackets

    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)  # Push opening brackets onto the stack
        elif bracket == ">":
            if not stack:  # Check for closing bracket without corresponding opening
                return False
            stack.pop()  # Pop the matching opening bracket from the stack

    return not stack  # True if all opening brackets have been matched


METADATA = {}

def check(correct_bracketing):
    assert correct_bracketing("<>")
    assert correct_bracketing("<<><>>")
    assert correct_bracketing("<><><<><>><>")
    assert correct_bracketing("<><><<<><><>><>><<><><<>>>")
    assert not correct_bracketing("<<<><>>>>")
    assert not correct_bracketing("><<>")
    assert not correct_bracketing("<")
    assert not correct_bracketing("<<<<")
    assert not correct_bracketing(">")
    assert not correct_bracketing("<<>")
    assert not correct_bracketing("<><><<><>><>><<>")
    assert not correct_bracketing("<><><<><>><>>><>")

check(correct_bracketing)
