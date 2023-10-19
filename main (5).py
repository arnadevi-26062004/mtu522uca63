#3.2 implement a function called sort_students that takes a list of students objects as an sort the list based on their CGPA(commulative Grade Point Average) in descending order.each student object has the following attributes: name (Strings),roll_number(string),and cgpa(float).Test the functions with different input lists of students
class student:

  def __init__(self, name, roll_number, cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa= cgpa


def sort_student(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                        key=lambda student: student.cgpa, 
                         reverse=True)
  #syntax _ lambda arg:exp
  return sorted_students


#Example usage:
students = [
     student("Stephen", "A123", 7.8),
     student("Karthik", "A124", 8.9),
     student("Santhosh", "A125", 9.1),
     student("Komban", "A126", 9.9),
 ]

sorted_students = sort_student(students)

 # Print the sorted list of students
for students in sorted_students:
  print("Name: {}, Roll Number: {}. CGPA  {}".format(students.name,
                                           students.roll_number,
                           students.cgpa))
