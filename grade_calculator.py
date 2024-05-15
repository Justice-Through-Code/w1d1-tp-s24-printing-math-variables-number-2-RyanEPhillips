def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Hello! Please enter your name: ")
    print("Welcome",  student_name, "lets find your average grade")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = int(input("Please enter your math score: "))
    science_score = int(input("Please enter your science score: "))
    english_score = int(input("Please enter your english score: "))

    # Calculate the average grade
    average_grade = ((math_score + science_score + english_score)/3)

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    #formating average grade to show proper decimal places 
    #consulted ChatGPT as I had some trouble implimenting this part
    round_num ="{:.2f}".format(average_grade)  

    # Print the student's name and their average grade
    print(f"Well,", student_name, round_num, "is you average score")
