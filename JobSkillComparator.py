from Skill_Info import Skill
import xlrd

for ExcelFileName in ['Knowledge.xlsx', 'Skills.xlsx', 'Abilities.xlsx']:
    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name(ExcelFileName[:-5])

    firstJob = "Civil Engineers" #raw_input("Enter first job:")
    secondJob = "Marine Engineers" #raw_input("Enter second job:")

    skills = []

    count = 1
    for i in range(0, worksheet.nrows):
        if worksheet.cell_value(i, 1) == firstJob and worksheet.cell_value(i, 4) == 'IM':
            skillToAdd = worksheet.cell_value(i, 3)
            added = False
            for temp in skills:
                if temp.skill == skillToAdd:
                    added = True

            if added == False:
                s = Skill(skillToAdd)
                s.setAgri(worksheet.cell_value(i, 6))
                skills.append(s)

    for i in range(0, worksheet.nrows):
        if worksheet.cell_value(i, 1) == secondJob and worksheet.cell_value(i, 4) == 'IM':
            skillToAdd = worksheet.cell_value(i, 3)
            added = False
            for temp in skills:
                if temp.skill == skillToAdd:
                    added = True
                    temp.setNaval(worksheet.cell_value(i, 6))

            if added == False:
                s = Skill(skillToAdd)
                s.setNaval(worksheet.cell_value(i, 6))
                skills.append(s)

    skills.sort()
    print ExcelFileName[:-5] + " Level:"
    print ""
    for s in skills:
        s.get()
    skills = []
    print ""
