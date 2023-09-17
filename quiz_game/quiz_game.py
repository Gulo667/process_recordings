
import lists
print(lists.created_answers)
print("welcome to my dummy quiz")
playing = input("the quiz will take approximately 10 minutes. do you want to play ? ").lower()
if playing != "yes":
    quit()
else:
    print("okay, let's start :) ")
final_point=0
def during_game(questions):
    for question in lists.questions_list:
        print(question)
        lists.created_answers.append(input("answer: ").lower())
during_game(lists.questions_list)
for i in range(0, len(lists.answers_list)):
    if lists.answers_list[i]==lists.created_answers[i]:
        print(f"you've answered correctly on the question - {lists.questions_list[i]}")
        final_point+=1
    else:
        print(f"you've answered incorrectly on the question - {lists.questions_list[i]} \n correct anaswer is {lists.answers_list[i]}")
if final_point < len(lists.answers_list)/2:
    print(f"you've finished the quiz with the result {final_point}, try better next time :) ")
else:
    print(f"you've finished the quiz with the result {final_point}, good job :) ")