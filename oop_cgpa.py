class GradePoint:
   
    def __init__(self, name, courses, scores, units):
        self.__name = name
        self.__num_of_courses = courses
        self.__score_list = scores
        self.__unit_list = units
    
    def __score_converter(self, score):
        #getting score point
        count = 5
        for x in [70,60,50,40,30,0]:
            if score >= x:
                return count
            count -= 1

    def __cgpa(self):
        #calculating cgpa
        total_score = 0
        value_list = list(map(self.__score_converter,self.__score_list))
        for x in range(self.__num_of_courses):
            unit_value = value_list[x]
            total_score += unit_value * self.__unit_list[x]

        gpa = total_score/sum(self.__unit_list)
        return gpa

    def __grade_converter(self, score):
        #generating grades
        grades = ['A','B','C','D','E','F']
        for idx,value in enumerate([70,60,50,40,30,0]):
            if score >= value:
                return grades[idx]
                
    def __grades(self):
        #using grade to generate points
        grade_list = list(map(self.__grade_converter,self.__score_list))
        grades = []
        for x in range(self.__num_of_courses):
            value = grade_list[x]
            grades.append(value)
        return grades

            #method to get student details
    def __str__(self):
        #returning student details
        student_details = f"Student Name:{self.__name}\nNumber of Courses:{self.__num_of_courses}\
            \nScore in Courses:{self.__score_list}\nRespective Grades:{self.__grades()}\nGPA:{self.__cgpa()}"
        return student_details

#main method
def main():
    while True:
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
            #catching input error
            try:
                score = int(input(f"[{x+1}]Score in course:"))
                scores.append(score)
                unit = int(input(f"[{x+1}]Unit of course:"))
                units.append(unit)
            except ValueError:
                print("Input the right score in digits next time")
                main()
                pass
        student = GradePoint(name,num_courses, scores, units)
        print(student)

        print(
            "...........................................................................................................")
        prompt = input("Do you wish to get another student(s) GPA? 'if yes, press y, if no, press x' (y/n): ")
        if prompt == 'y' or prompt == 'Y':
            main()
            pass
        elif prompt == 'n' or prompt == 'N':
            print("Bye")
            exit()
        else:
            print("Input the right response")
            exit()
   

if __name__ == "__main__":
    main()
