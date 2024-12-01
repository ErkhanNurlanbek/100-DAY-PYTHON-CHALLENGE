import pandas
nums = [1, 2, 3]
new_list = [n + 5 for n in nums]
name = 'Erkhan'
name_list = [letter for letter in name]
print(name_list)
students_scores = {

}
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)


student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [43, 23, 91]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#Loooooooooop through a data frame
for (key, value) in student_data_frame.items():
    print(value)
#Loooooooooop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.score <= 50:
        print(f'{row.student} failed')