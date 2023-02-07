class grade_point:
    name_list = []
    score_list = []
    grade_list = []
    details_list = []
    gpa_list = []
    sum_gotten_point = 0
    sum_point = 0
    sum_gpa = 0
    cgpa = 0
    def __init__(self):
        self.name = str(input("Enter the name of student: "))
        self.name_list.append(self.name)

    def score_cal(self):
        self.course_num = int(input("How many courses do you offer: "))
        for c in range(self.course_num):
            score = int(input("Enter the score of the courses: "))
            unit = int(input("Enter the unit of the courses: "))
            self.score_list.append(score)

            if score >= 70 and score <= 100:
                grade = "A"
                point = 5
                gpa = 5 * 5
            if score >= 60 and score <= 69:
                grade = "B"
                point = 4
                gpa = 5 * 4
            if score >= 50 and score <= 59:
                grade = "C"
                point = 3
                gpa = 5 * 3
            if score >= 40 and score <= 49:
                grade = "D"
                point = 2
                gpa = 5 * 2
            if score >= 30 and score <= 39:
                grade = "E"
                point = 1
                gpa = 5 * 1
            if score >= 0 and score <= 29:
                grade = "F"
                point = 0
                gpa = 5 * 0
            # else:
            # print("Invalid Grade")
            self.grade_list.append(grade)
            attainable_sum = unit * 5
            attained_sum = point * unit
            self.sum_gotten_point += attained_sum
            self.sum_point += attainable_sum
            self.gpa = (self.sum_gotten_point / self.sum_point) * 5
            self.gpa_list.append(gpa)

    def output(self):
        print(f"Name of Student: {self.name}")
        print(f"Number of Courses: {self.course_num}")
        print(f"Score in courses: {self.score_list}")
        print(f"Respective Grades in Courses: {self.grade_list}")
        print(f"GPA: {self.gpa:.3f}")



p1 = grade_point()
p1.score_cal()
p1.output()