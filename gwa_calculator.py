# GWA Calculator in Python
# Note: Only works on a 5-point scale grade system
# The highest grade is a 1.00 and the lowest is a 5.00

def calculate_gwa(grades):
    total_subjects = len(grades)
    total_score = sum(grades)
    gwa = total_score / total_subjects
    return gwa

def determine_honor(gwa):
    if gwa >= 1.00 and gwa <= 1.25:
        return "You are in the first honors"
    elif gwa > 1.25 and gwa <= 1.50:
        return "You are in the second honors"
    elif gwa > 1.50 and gwa <= 1.75:
        return "You are in the third honors"
    elif gwa == 3.00:
        return "You survived the semester!"
    elif gwa == 5.00:
        return "You're a FAILURE!"
    else:
        return "You're not eligible for dean's listers"

def main():
    num_subjects = int(input("Enter the number of subjects: "))

    grades = []
    subject_names = []

    for i in range(num_subjects):
        subject_name = input(f"Enter the name of subject {i + 1}: ")
        grade = float(input(f"Enter the grade for subject {subject_name}: "))
        subject_names.append(subject_name)
        grades.append(grade)

    gwa = calculate_gwa(grades)
    print("\nYour GWA is", round(gwa, 2))

    honor = determine_honor(gwa)
    print(honor)

if __name__ == "__main__":
    main()
