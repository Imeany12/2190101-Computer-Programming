filename = input()
semester = []
Course = []
dump = []
fn = open(filename, "r")
for line in fn :
    if "semester" in line :
        semester.append(line[:len(line)-1:])
    elif "COURSE-NO,COURSE-NAME,Credit,Grade" in line :
        dump.append(line)
    else : Course.append(line[:len(line)-1:])

print(semester,Course,dump)