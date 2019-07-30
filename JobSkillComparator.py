from Skill_Info import Skill
import xlrd
import os
import numpy as np

#'Knowledge.xlsx', 'Skills.xlsx', 'Abilities.xlsx'
for ExcelFileName in ['Skills.xlsx']:

    filename = ExcelFileName[:-5] + "Data.csv"
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, "w+")

    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name(ExcelFileName[:-5])

    firstJob = "Agricultural Engineers" #raw_input("Enter first job:")
    secondJob = "Marine Engineers" #raw_input("Enter second job:")
    jobList = ["Marine Engineers", "Agricultural Engineers", "Electrical Engineers", "Civil Engineers", "Mechanical Engineers",
               "Anthropologists", "Archeologists", "Software Developers, Applications", "Lawyers", "Mathematicians",
               "Nuclear Engineers", "Computer Hardware Engineers", "Geographers", "Economists", "Historians",
               "Computer Programmers", "Chemical Technicians", "Geoscientists, Except Hydrologists and Geographers", "Librarians", "Dental Hygienists",
               "Pharmacy Aides", "Computer Operators", "Sailors and Marine Oilers", "Microbiologists", "Mental Health Counselors",
               "Registered Nurses", "Pharmacists", "Aerospace Engineers", "Materials Scientists", "Database Administrators",
               "Locomotive Engineers", "Interviewers, Except Eligibility and Loan", "Accountants", "Financial Analysts", "Graphic Designers"]

    computerizationProbability = np.array([0.01, 0.49, 0.1, 0.019, 0.011,
                                  0.0077, 0.0077, 0.042, 0.035, 0.047,
                                  0.07, 0.22, 0.25, 0.43, 0.44,
                                  0.48, 0.57, 0.63, 0.65, 0.68,
                                  0.72, 0.78, 0.83, 0.012, 0.0048,
                                  0.009, 0.012, 0.017, 0.021, 0.03,
                                  0.96, 0.94, 0.94, 0.23, 0.082])

    skills = []

    a = np.empty((0,35), int)

    skilldata = []
    test = [2, 2, 3]


    for j in range(0, len(jobList)):

        skilldata = []

        for i in range(0, worksheet.nrows):
            if worksheet.cell_value(i, 1) == jobList[j]:
                skillToAdd = worksheet.cell_value(i, 3)
                added = False

                if worksheet.cell_value(i, 4) == 'IM':
                    skilldata.append(worksheet.cell_value(i, 6))

        #print skilldata
        #print len(skilldata)
        a = np.append(a, [skilldata], axis = 0)

    x = np.linalg.solve(a, computerizationProbability)
    print x
    exit()

    #skills.sort()
    #print ExcelFileName[:-5] + " Level:"
    #print ""
    skills.sort()
    f.write("Skill Name,Naval,Agricultural,Civil,Electrical,Mechanical\n")
    for s in skills:
        f.write(s.makeCSV() + '\n')
        #s.get()
    skills = []
    #print ""


    f.close()