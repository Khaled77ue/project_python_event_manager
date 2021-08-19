#### IMPORTS ####
import event_manager as EM



def check_id(id_int):
    stripped_id = id_int.strip()
    if len(str(stripped_id)) != 8 or not stripped_id.isdigit():
        return False
    else:
        return True


def check_name(name_string):
    stripped_name = name_string.strip()
    if all(x.isalpha() or x.isspace() for x in stripped_name):
        return True
    else:
        return False




def check_age(age_int):
    stripped_age = age_int.strip()
    if int(stripped_age) >= 16 and int(stripped_age) <= 120:
        return True
    else:
        return False



def check_year(year_of_birth,age_int):
    stripped_year = year_of_birth.strip()
    if (int(2020) - int(stripped_year))==int(age_int):
        return True
    else:
        return False

def check_semester(semester_int):
    stripped_semester = semester_int.strip();
    if int(stripped_semester) >= int(1):
        return True
    else:
        return False



#### PART 1 ####
# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    file = open(orig_file_path,'r')
    my_list = []
    id_list = []
    for line in file:
        line_split = line.split(",")
        if (check_id(line_split[0])) and (check_name(line_split[1])) and (check_age(line_split[2])) and (check_year(line_split[3],line_split[2])) and (check_semester(line_split[4])) and float(line_split[0][0]) != 0:
            id_list.append(line_split[0])

            for i in range(5):
                while '  ' in line_split[i]:
                    line_split[i] = line_split[i].replace('  ', ' ')
                if line_split[i][len(line_split[i])-1] == ' ':
                    line_split[i] = line_split[i][:-1]
                if line_split[1][0] != ' ':
                    line_split[1] = ' ' + line_split[1]
                if line_split[2][0] != ' ':
                    line_split[2] = ' ' + line_split[2]
                if line_split[3][0] != ' ':
                    line_split[3] = ' ' + line_split[3]
                if line_split[4][0] != ' ':
                    line_split[4] = ' ' + line_split[4]
                if i < 4:
                    line_split[i] += ','
                my_list.append(line_split[i])
    if len(my_list) == 0:
        with open(filtered_file_path,'w') as f:
            for item in my_list:
                f.write("%s"%item)

    id_list.sort()
    tmp_list = []
    for i in id_list:
        if i not in tmp_list:
            tmp_list.append(i)
    id_list=tmp_list
    if len(my_list) != 0:
        with open(filtered_file_path,'w') as f:
            for item in my_list:
                f.write("%s"%item)
    lst_of_lines = []
    out_file= open(filtered_file_path,'r')
    for newline in out_file:
        lst_of_lines.append(newline)

    lst_of_lines.reverse()
    sorted_list = []
    que =[]
    for i in id_list:
        z=i.replace(' ','')
        que.append(z)
    id_list=que
    id_list_str = [str(x) for x in id_list]

    for id in id_list_str:
       for line in lst_of_lines:
           id_frm_lst = line.split(',')
           if id in id_frm_lst[0]:

                sorted_list.append(line)
                break

    t= []
    t=sorted_list
    t = map(lambda s: s.strip(), t)
    sorted_list = t

    with open(filtered_file_path,'w') as f:
        for item in sorted_list:
            f.write("%s\n"%item)


    file.close()











    
# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if int(k) <= 0:
        return -1
    t=k
    file = open(in_file_path, 'r')
    my_list = []
    age_list = []
    id_list = []
    for line in file:
        line_split = line.split(",")
        if  (check_id(line_split[0])) and (check_name(line_split[1])) and (check_age(line_split[2])) and (check_year(line_split[3],line_split[2])) and (check_semester(line_split[4])) and float(line_split[0][0]) != 0:
            id_list.append(line_split[0])

            age_list.append(line_split[2])

            for i in range(5):
                while '  ' in line_split[i]:
                    line_split[i] = line_split[i].replace('  ', ' ')
                if line_split[i][len(line_split[i])-1] == ' ':
                    line_split[i] = line_split[i][:-1]
                if line_split[1][0] != ' ':
                    line_split[1] = ' ' + line_split[1]
                if line_split[2][0] != ' ':
                    line_split[2] = ' ' + line_split[2]
                if line_split[3][0] != ' ':
                    line_split[3] = ' ' + line_split[3]
                if line_split[4][0] != ' ':
                    line_split[4] = ' ' + line_split[4]
                if i < 4:
                    line_split[i] += ','
                my_list.append(line_split[i])
    if len(my_list) == 0:
        with open(out_file_path,'w') as f:
            for item in my_list:
                f.write("%s"%item)

    id_list.sort()
    tmp_list = []
    for i in id_list:
        if i not in tmp_list:
            tmp_list.append(i)
    id_list = tmp_list
    age_list_int = [int(z) for z in age_list]
    age_list_int.sort()
    age_list_str = [str(w) for w in age_list_int]
    if len(my_list) != 0:
        with open(out_file_path,'w') as f:
            for item in my_list:
                f.write("%s"%item)
    lst_of_lines = []
    out_file= open(out_file_path,'r')
    for newline in out_file:
        lst_of_lines.append(newline)
    lst_of_lines.reverse()

    k=[]
    for i in id_list:
        j=i.replace(' ','')
        k.append(j)
    id_list=k

    oldsorted_list= []
    sorted_list = []
    id_list_str = [str(x) for x in id_list]
    for id in id_list_str:
       for line in lst_of_lines:
           id_frm_lst = line.split(',')
           if id in id_frm_lst[0]:
                oldsorted_list.append(line)
                break

    for age in age_list_str:
        age = ' ' + age
        for line in oldsorted_list:
            age_frm_lst = line.split(',')
            #print(age)
            if age == age_frm_lst[2]:
                if(t > 0):
                    sorted_list.append(line)
                    oldsorted_list.remove(line)
                    t-=1
                    break

    lastitem = []
    for item in sorted_list:
        newitem=item.split(',')
        stripitem=newitem[1].strip()
        lastitem.append(stripitem)

    if len(lastitem) == 0:
        return 0
    if len(lastitem) !=0:
        with open(out_file_path, 'w') as f:
             for item in lastitem:
                f.write("%s\n"%item)

    file.close()


# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    if type(semester)!= int or semester < 1:
        return -1
    file = open(in_file_path, 'r')
    counter = 0
    sum = 0
    test_list =[]
    my_list = []
    id_list = []
    age_list = []
    for line in file:
        line_split = line.split(",")
        if (check_id(line_split[0])) and (check_name(line_split[1])) and (check_age(line_split[2])) and (
        check_year(line_split[3], line_split[2])) and (check_semester(line_split[4])) and float(line_split[0][0]) != 0:
            id_list.append(line_split[0])
            age_list.append(line_split[2])

            for i in range(5):
                while '  ' in line_split[i]:
                    line_split[i] = line_split[i].replace('  ', ' ')
                if line_split[i][len(line_split[i]) - 1] == ' ':
                    line_split[i] = line_split[i][:-1]
                if line_split[1][0] != ' ':
                    line_split[1] = ' ' + line_split[1]
                if line_split[2][0] != ' ':
                    line_split[2] = ' ' + line_split[2]
                if line_split[3][0] != ' ':
                    line_split[3] = ' ' + line_split[3]
                if line_split[4][0] != ' ':
                    line_split[4] = ' ' + line_split[4]

                my_list.append(line_split[i])
            test_list.append(line)
    if len(my_list) == 0:
        file.close()
        return 0
    test_list.reverse()

    id_list.sort()
    tmp_list = []
    for i in id_list:
        if i not in tmp_list:
            tmp_list.append(i)
    id_list = tmp_list
    sortedlist =[]
    my_list.reverse()
    id_list_str = [str(x) for x in id_list]
    for id in id_list_str:
       for line in test_list:
            linesplit=line.split(',')
            if id in linesplit[0]:
                sortedlist.append(line)
                break

    for line in sortedlist:
        line1=line.split(',')
        if int(line1[4]) == int(semester):
            counter+=1
            sum+=int(line1[2])
    if counter==0:
        return 0
    average = sum/counter

    file.close()
    return average





#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    min_date = EM.dateCopy(events[0]['date'])
    for e in events:
        datee = e['date']
        if EM.dateCompare(min_date, datee) > 0:
            EM.dateDestroy(min_date)
            min_date = e['date']
    event_manager = EM.createEventManager(min_date)
    for i in events:
        EM.emAddEventByDate(event_manager, i['name'], i['date'], i['id'])
    EM.emPrintAllEvents(event_manager, file_path)
    return event_manager



def testPrintEventsList(file_path :str):
    events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
                    {"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
                                 {"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
                                     {"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
    em = printEventsList(events_lists,file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)

#### Main #### 
# feel free to add more tests and change that section. 
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        testPrintEventsList(sys.argv[1])

