class GradePoint:
    def __init__(self, name, courses, scores, units,num):
        self.__name = name
        self.__num_of_courses = courses
        self.__score_list = scores
        self.__unit_list = units
        self.__check__num = num
    
    def __score_converter(self, score):
        count = 5
        for x in [70,60,50,40,30,0]:
            if score >= x:
                return count
            count -= 1

    def __cgpa(self):
        total_score = 0
        value_list = list(map(self.__score_converter,self.__score_list))
        for x in range(self.__num_of_courses):
            unit_value = value_list[x]
            total_score +=  unit_value * self.__unit_list[x]

        gpa = total_score/sum(self.__unit_list)
        return gpa

    def __grade_converter(self, score):
        grades = ['A','B','C','D','E','F']
        for idx,value in enumerate([70,60,50,40,30,0]):
            if score >= value:
                return grades[idx]
                
    def __grades(self):
        grade_list = list(map(self.__grade_converter,self.__score_list))
        grades = []
        for x in range(self.__num_of_courses):
            value = grade_list[x]
            grades.append(value)
        return grades
            
    def __str__(self):
        student_details = f"Student Name:{self.__name}\nNumber of Courses:{self.__num_of_courses}\
            \nScore in Courses:{self.__score_list}\nRespective Grades:{self.__grades()}\nGPA:{self.__cgpa()}"
        return student_details


def main():
    try:
        name = input("Name:")
        num_courses = int(input("Number of Courses:"))
    except ValueError:
        print("Input proper digits!!")
        main()
        pass
    scores = []
    units = []
    for x in range(num_courses):
        try:
            score = int(input(f"[{x+1}]Score in course:"))
            scores.append(score)
            unit = int(input(f"[{x+1}]Unit of course:"))
            units.append(unit)
        except ValueError:
            print("Input the right score in digits next time")
            main()
            pass
    student = GradePoint(name, num_courses, scores, units)
    print(student)
   

if __name__ == "__main__":
    main()
