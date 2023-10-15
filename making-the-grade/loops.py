"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    scores_rounded =[]
    for each in student_scores:
        scores_rounded.append(round(each))
    
    return scores_rounded


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count =0
    for each in student_scores:
        if each <= 40:
            count = count+1

    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    the_best =[]
    for each in student_scores:
        if each >= threshold:
            the_best.append(each)

    return the_best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    #calculeting the range
    grade_range = (highest-40)//4
    target =[]
    
    #count = 41
    #while (count<highest):
    #    target.append(count)
    #    count = count+grade_range

    for each in range(41, highest, grade_range): #this line makes the SAME THING as de while above!
        target.append(each)
    
    return target


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    target =[]
    for index, name in enumerate(student_names):
        target.append(f"{index+1}. {name}: {student_scores[index]}")

    return target
    

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for each in student_info:
        if each[1] == 100:
            return each
            
    return[]
        
