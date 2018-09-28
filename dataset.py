import numpy as np
import datetime
np.random.seed(0)
Designations = ['Associate','Analyst','Sr. Analyst','Associate Consultant','Consultant','Sr. Consultant']
Locations = ['Delhi','Mumbai','Bangalore','Chennai','Hyderabad','Noida','Pune','Kolkata']
Ratings = [i for i in range(6)]
Feedbacks = ['Poor','Good','Average','Excellent','Awesome']
primarySkills = ['Python','Java','DBMS','Testing','C','Perl','Machine Learning','Algorithm and Programming']
skills = ['Python','Java','DBMS','HTML/CSS/JS','Testing','C','Perl','Machine Learning','Algorithm and Programming','OpenCV','Manual Testing','Oracle','Git','Big Data']


for i in range(10):
    #------- Employee Table Detials-------------------------#
    firstName = "".join(np.random.choice(['a','b','c','d','e','f','g','h','i','j',
                                       'k','l','m','n','o','p','q','r','t',
                                       'u','v','w','x','y','z'],10))
    lastName = "".join(np.random.choice(['a','b','c','d','e','f','g','h','i','j',
                                      'k','l','m','n','o','p','q','r','t','u',
                                      'v','w','x','y','z'],10))
    currentRole = np.random.choice(['Company','External'],1)[0]
    middleName = " "
    domain = np.random.choice(["yahoo.in","gmail.com","hotmail.com"],1)[0]
    email = firstName+'.'+lastName+"@"+domain
    yearsOfExperience = np.random.choice(10,1)[0]
    isAllocated = np.random.choice(1,1,[0.9,0.1])[0]
    preferredLocation = np.random.choice(Locations,1)[0]
    currentLocation = np.random.choice(Locations,1)[0]
    resourceAvail = datetime.datetime.now()
    visaCountry = np.random.choice(1,1)[0]

    if yearsOfExperience == 0:
        des = np.random.choice(Designations[:2],1)[0]
        rating = 0
        feedback = 'NaN'
    elif yearsOfExperience >= 1 and yearsOfExperience <=3:
        des = np.random.choice(Designations[2:4],1)[0]
        rating = np.random.choice(Ratings,1)[0]
        feedback = np.random.choice(Feedbacks,1)[0]
    else:
        des = np.random.choice(Designations[4:],1)[0]
        rating = np.random.choice(Ratings,1)[0]
        feedback = np.random.choice(Feedbacks,1)[0]
    print("----- Employee Detials --------------")
    print("Emp ID: ",i)
    print("Name: ",firstName+middleName+lastName)
    print("Email: ",email)
    print("Designation: ",des)
    print("Company/External: ",currentRole)
    print("Current Location: ",currentLocation)
    print("Total Experience: ",yearsOfExperience)
    print("On Bench/Wait: ",'Yes' if isAllocated ==0 else 'No')
    print("Date of Avialablity: ",resourceAvail)
    print("Perferred Location: ",preferredLocation)
    print("Rating: ",rating)
    print("Feedback: ",feedback)
    print("Visa: ",visaCountry)
    #print(i,firstName,middleName,lastName,email,des,currentRole,currentLocation,yearsOfExperience,
    # isAllocated,resourceAvail,preferredLocation,rating,feedback,visaCountry)

    #----------------ExamScores-----------------------------#
    #print("------- Exam Scores --------------------")
    marks = np.random.choice(100,5)
    examDict = {'Python':marks[0],'Java':marks[1],'C':marks[2],'HTML/CSS/JS':marks[3],'Perl':marks[4]}
    print("Training Score: ",examDict)

    #---------- Skiils -------------------------------------#
    primarySkillsFlag = []
    empSkills = np.random.choice(skills,3)
    #empSkills = certiName
    for i in empSkills:
        if i in primarySkills:
            primarySkillsFlag.append(i)
    if yearsOfExperience == 0:
        skillExp = [0,0,0]
    elif yearsOfExperience >= 1 and yearsOfExperience <=3:
        skillExp = np.random.choice(3,3)
    else:
        skillExp = np.random.choice(10,3)
    skillData = dict(zip(primarySkillsFlag, skillExp))
    print("Skills: ",skillData)

    #------ Certification Table Detials --------------------#
    certiName = empSkills
    certiNumber = []
    for totalCertificate in range(3):
        code = int("".join(str(i) for i in np.random.choice(10,5)))
        certiNumber.append(code)
    #print("------- Certification Detials --------------")
    #print(i,certiName,certiNumber)
    certificate = dict(zip(certiName, certiNumber))
    print("Certification Name: ",certificate)
    print("-------------------------------\n")
