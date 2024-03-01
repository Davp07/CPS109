"""""Assign a letter grade given a numeric grade. A letter grade will be assigned in accordance
 with the North Shore Community College’s Grading System, which is defined on page 4 of
  the course syllabus and below:
A   93-100   C   73-76
A-  90-92    C-  70-72
B+  87-89    D+  67-69
B   83-86    D   63-66
B-  80-82    D-  60-62
C+  77-79    F   Below 60
"""


number_grade = int(input('Enter your grade in number form: '))


if 93 <= number_grade and number_grade <= 100:
  letter_grade = 'A'

elif 90 <= number_grade and number_grade <= 92:
    letter_grade = 'A-'

elif 87 <= number_grade and number_grade <= 89:
    letter_grade = 'B+'

elif 83 <= number_grade and number_grade <= 86:
    letter_grade = 'B'

elif 80 <= number_grade and number_grade <= 82:
    letter_grade = 'B-'

elif 77 <= number_grade and number_grade <= 79:
    letter_grade = 'C+'

elif 73 <= number_grade and number_grade <= 76:
    letter_grade = 'C'

elif 70 <= number_grade and number_grade <= 72:
    letter_grade = 'C-'

elif 67 <= number_grade and number_grade <= 69:
    letter_grade = 'D+'

elif 63 <= number_grade and number_grade <= 66:
    letter_grade = 'D'

elif 60 <= number_grade and number_grade <= 62:
    letter_grade = 'D-'

else:
    letter_grade = 'F'
print(f'your letter grade for {number_grade} is {letter_grade}')