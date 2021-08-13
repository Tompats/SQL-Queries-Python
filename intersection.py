#   Thomas Patsanis, A.M: 3318
#
#   1 Ergasthriakh Askhsh
#   Version: Python 3.8.5
#


#Returns a 2 element array for a string
def convert_string_to_array(str):
    line = str.split("\t")
    line[1] = int(line[1])
    return line



def write_output_intersect(output_file,record):
    output_record = str(record[0])+"\t"+str(record[1])+"\n"
    output_file.write(output_record)



def intersect(file_1,file_2):
    output_file = open("RintersectionS.tsv", "w")
    #################
    str_f1 = file_1.readline().rstrip('\n')
    line_f1 = convert_string_to_array(str_f1)
    str_f2 = file_2.readline().rstrip('\n')
    line_f2 = convert_string_to_array(str_f2)
    last_record = []
    flag_2 = False
    flag_1 = False
    counter = 1
    flag = 0
    buffer = []
    while not(flag_1) and not(flag_2):
        counter += 1
        if(line_f1[0]==line_f2[0]):
            if(line_f1[1]==line_f2[1]):
                if (line_f2!=last_record):
                    write_output_intersect(output_file,line_f2)
                    last_record = line_f2
                str_f2 = file_2.readline().rstrip('\n')
                str_f1 = file_1.readline().rstrip('\n')
                counter+=1
            elif(line_f1[1]<line_f2[1]):
                str_f1 = file_1.readline().rstrip('\n')
            elif(line_f1[1]>line_f2[1]):
                str_f2 = file_2.readline().rstrip('\n')
        elif(line_f1[0]<line_f2[0]):
            if(flag_1):
                flag_2 = True
                break
            str_f1 = file_1.readline().rstrip('\n')
        elif(line_f1[0]>line_f2[0]):
            if flag_2:
                flag_1 = True
                break
            str_f2 = file_2.readline().rstrip('\n')


        if str_f1 == "":
            flag_1=True
        else:
            line_f1 = convert_string_to_array(str_f1)
        if str_f2 == "":
            flag_2=True
        else:
            line_f2 = convert_string_to_array(str_f2)
    print("Total Lines Read: "+str(counter))
