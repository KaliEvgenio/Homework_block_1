grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=list(students)
students_list.sort()
students_dict=dict(zip(students_list,grades))

for i in students_dict:
    s=0
    for j in students_dict[i]:
        s+=j
    students_dict[i]=s/len(students_dict[i])
print(students_dict)