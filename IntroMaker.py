#Python Intro Maker using personal details

name= input("Enter your name: ")
father_name= input("Enter your Father name: ")
date_of_birth= input("Enter your Date of Birth: ")
place_of_birth= input("Enter your place of birth: ")
age= input("Enter yout age: ")
email_address= input("Enter your email address: ")
qualifications= input("Enter your recent qualifications: ")
institute_name= input("Enter the name of your College/University: ")
skills= input("Enter your skills: ")
experience= input("Enter relevant job experience: ")
time_period= input("Enter the time duration of job: ")
def create_biodata():
    biodata= {
        "header" : "User Description:      ",
        "name" : f"My Name is {name}.",
        "father name" : f"My father Name is {father_name}.",
        "birth" : f"I was born on {date_of_birth} in {place_of_birth} and I am {age} years old.",
        "contact" : f"My email address is {email_address}.",
        "qualifications" : f"I recently completed my {qualifications} from {institute_name}.",
        "skills" : f"Along with my qualifications, i also possess a decent level of knowledge in {skills}.",
        "experience" : f"I also have relevant job experience as a {experience} for {time_period}."
    }
    return biodata
result= create_biodata()
print(*result.values(), sep=" ")