
def numerical_letter_grade(grades):
  """
  Converts a list of GPAs to a list of letter grades based on a specific grading scale.

  Args:
      grades: A list of numerical grades (GPAs).

  Returns:
      A list of corresponding letter grades for each GPA.
  """

  letter_grades = []
  for grade in grades:
    if grade >= 4.0:
      letter_grades.append("A+")
    elif grade > 3.7:
      letter_grades.append("A")
    elif grade > 3.3:
      letter_grades.append("A-")
    elif grade > 3.0:
      letter_grades.append("B+")
    elif grade > 2.7:
      letter_grades.append("B")
    elif grade > 2.3:
      letter_grades.append("B-")
    elif grade > 2.0:
      letter_grades.append("C+")
    elif grade > 1.7:
      letter_grades.append("C")
    elif grade > 1.3:
      letter_grades.append("C-")
    elif grade > 1.0:
      letter_grades.append("D+")
    elif grade > 0.7:
      letter_grades.append("D")
    elif grade > 0.0:
      letter_grades.append("D-")
    else:
      letter_grades.append("E")

  return letter_grades


def check(numerical_letter_grade):
    # Check some simple cases
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-'], "Test 1"
    assert numerical_letter_grade([1.2]) == ['D+'], "Test 2"
    assert numerical_letter_grade([0.5]) == ['D-'], "Test 3"
    assert numerical_letter_grade([0.0]) == ['E'], "Test 4"
    assert numerical_letter_grade([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+'], "Test 5"
    assert numerical_letter_grade([0, 0.7]) == ['E', 'D-'], "Test 6"

check(numerical_letter_grade)
