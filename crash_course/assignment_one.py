# a function to calculate

def calculate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score>=80:
        return 'B'
    elif average_score >=70:
        return 'C'
    elif average_score >=60:
        return 'D'
    elif average_score >=50:
        return 'E'
    else:
        return 'F'

def main():
    subject_names = ["CIT 3101", "CIT 3102", "CIT 3013", "CIT 3104"]
    subject_scores = []

    print("Let's record your scores for the following subjects, shall we?")

    for subject in subject_names:
        score = float(input(subject + " "))
        subject_scores.append(score)

    total = 0
    count = 0

    for sub_score in subject_scores:
        total = total + sub_score
        count +=1

    average = total/count

    grade = calculate_grade(average)

    print("Your results are as follows:")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
