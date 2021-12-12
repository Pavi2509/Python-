# Basic School administration System
import csv
#writing the contents into csv file
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","E-mail ID"])

        writer.writerow(info_list)

if __name__=='__main__':
    condition = True
    student_num=1

    #getting input from the user
    while(condition):
        student_info=input("Enter the student information for student no. #{} in the following format (Name, Age, Contact_Number, E-Mail_ID): ".format(student_num))

        student_info_list=student_info.split(', ')

        print("\nThe entered information is: \nName: {}\nAge: {}\nContact Number: {}\nE-mail ID: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check=input("Is the entered information correct? (y/n): ")
        if choice_check=="y":
            write_into_csv(student_info_list)

            condition_check=input("Enter (y/n) if you want to enter another student's information : ")
            if(condition_check=="y"):
                condition=True
                student_num=student_num+1
            else:
                condition=False
        else:
            print("\nPlease re-enter the information")
