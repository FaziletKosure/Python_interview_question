# Given the names and grades for each student in a Physics class of  students
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.


def execute(s):
    d = {i[0]: i[1] for i in s}
    v = d.values()
    second = sorted(list(set(v)))[1]
    lowest2 = [key for key, value in d.items() if value == second]
    lowest2.sort()
    return [print(n) for n in lowest2]


students = [['Betty', 34], ['Berry', 45.5], ['Furki', 33], [
    'Tina', 33], ['Akriti', 56], ['Harsh', 45.5], ['Fazi', 34]]
execute(students)  # Betty Fazi
