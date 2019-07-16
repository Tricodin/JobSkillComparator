from Skill_Info import Skill
import xlrd
import os


for ExcelFileName in ['Knowledge.xlsx', 'Skills.xlsx', 'Abilities.xlsx']:

    filename = ExcelFileName[:-5] + "Data.csv"
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, "w+")

    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name(ExcelFileName[:-5])

    firstJob = "Agricultural Engineers" #raw_input("Enter first job:")
    secondJob = "Marine Engineers" #raw_input("Enter second job:")

    skills = []


    for i in range(0, worksheet.nrows):
        if worksheet.cell_value(i, 4) == 'IM':
            skillToAdd = worksheet.cell_value(i, 3)
            added = False

            if worksheet.cell_value(i, 1) == "Marine Engineers":
                for temp in skills:
                    if temp.skill == skillToAdd:
                        added = True
                        temp.setNaval(worksheet.cell_value(i, 6))
                if added == False:
                    s = Skill(skillToAdd)
                    s.setNaval(worksheet.cell_value(i, 6))
                    skills.append(s)

            elif worksheet.cell_value(i, 1) == "Agricultural Engineers":
                for temp in skills:
                    if temp.skill == skillToAdd:
                        added = True
                        temp.setAgri(worksheet.cell_value(i, 6))
                if added == False:
                    s = Skill(skillToAdd)
                    s.setAgri(worksheet.cell_value(i, 6))
                    skills.append(s)

            if worksheet.cell_value(i, 1) == "Electrical Engineers":
                for temp in skills:
                    if temp.skill == skillToAdd:
                        added = True
                        temp.setElec(worksheet.cell_value(i, 6))
                if added == False:
                    s = Skill(skillToAdd)
                    s.setElec(worksheet.cell_value(i, 6))
                    skills.append(s)

            if worksheet.cell_value(i, 1) == "Civil Engineers":
                for temp in skills:
                    if temp.skill == skillToAdd:
                        added = True
                        temp.setCivil(worksheet.cell_value(i, 6))
                if added == False:
                    s = Skill(skillToAdd)
                    s.setCivil(worksheet.cell_value(i, 6))
                    skills.append(s)

            if worksheet.cell_value(i, 1) == "Mechanical Engineers":
                for temp in skills:
                    if temp.skill == skillToAdd:
                        added = True
                        temp.setMech(worksheet.cell_value(i, 6))
                if added == False:
                    s = Skill(skillToAdd)
                    s.setMech(worksheet.cell_value(i, 6))
                    skills.append(s)


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