# Assignment 2
# part 1
# define function
def read_file(file_name):
    text = open(file_name)
    print(text.read())
# define and call function
read_file('file.txt')

# part 2
# define function
def read_file1(file_name):
    with open(file_name) as file:
        list = file.readlines()
        print(list)
# call function
read_file1('file.txt')

# part 3
# define function.
def longest_word(file_name):
    with open(file_name, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
# define and call function
print(longest_word('file.txt'))

# part 4
# define function
def word_count(file_name):
    word_count = 0
    with open(file_name, 'r') as file:
        for line in file:
            word_count += len(line.split())
	# define and call function
    print("number of words : ", word_count)
# use function
word_count('sample.txt')

# part 5
# define function
def employee_salary(file_name):
    dict = {}
    file = open(file_name)
    for line in file:
        key, value = line.split()
        dict[key] = value

    values = dict.values()
    max_salary = max(values)

    for name, salary in dict.items():
        if salary == max_salary:
             print(name)
# use function
employee_salary("salary.txt")


# part 6
# define function
def login():
    print("LOGIN")
    username = input("username: ")
    password = input("password: ")
    for line in open("user.txt", "r").readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print(f"Welcome {username}")
            return True
    print("Invalid user!")
    return False
# call function.
login()


# Home work
# define function.
def student_analysis(file_name):
    words_list = []
    with open(file_name, "r") as f:
        words_list = f.read().split()
        ids = []
        names = []
        marks = []
		# use function.
        while len(words_list) != 0:
            ids.append(words_list[0])
            names.append(words_list[1])
            marks.append(int(words_list[2]))
            words_list.pop(0)
            words_list.pop(0)
            words_list.pop(0)

        average_marks = sum(marks) / len(marks)
        highest_marks = max(marks)
        lowest_marks = min(marks)
		# use values in the function.
        highest_marks_index = marks.index(highest_marks)
        lowest_marks_index = marks.index(lowest_marks)
		# use function in index
        highest_student = names[highest_marks_index]
        lowest_student = names[lowest_marks_index]

        print("Class report")
        print(f"\tThere are a total of {len(ids)} students")
        print(f"\tThe average of total marks is {average_marks}")
        print(f"\t{highest_student} scored the highest marks as {highest_marks}")
        print(f"\t{lowest_student} scored the lowest marks as {lowest_marks}")

# use function fot the txt files.
student_analysis("bill.txt")

