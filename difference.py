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





def write_output_difference(output_file,record):
    output_record = str(record[0])+"\t"+str(record[1])+"\n"
    output_file.write(output_record)





def set_difference(file_1,file_2):
    output_file = open("RdifferenceS.tsv", "w")
    #read the first line of the files as string and remove new line char
    str_f1 = file_1.readline().rstrip('\n')
    line_f1 = convert_string_to_array(str_f1)
    str_f2 = file_2.readline().rstrip('\n')
    line_f2 = convert_string_to_array(str_f2)
    #the joined line
    flag_2 = False
    flag_1 = False
    counter = 1
    last_record = []
    while not(flag_1) or not(flag_2):
        if(flag_1):
            line_f1 = ['zzzzz']
        if flag_2:
            line_f2 = ['zzzzz']
        if(line_f1[0]==line_f2[0]):
            if(line_f1[1]==line_f2[1]):
                #print(line_f1)
                #str_f2 = file_2.readline().rstrip('\n')
                str_f1 = file_1.readline().rstrip('\n')
                #last_record = line_f1
                #counter+=1
            elif(line_f1[1]<line_f2[1]):
                if (line_f1!=last_record):
                    write_output_difference(output_file,line_f1)
                    last_record = line_f1
                str_f1 = file_1.readline().rstrip('\n')
            elif(line_f1[1]>line_f2[1]):
                str_f2 = file_2.readline().rstrip('\n')
        elif(line_f1[0]<line_f2[0]):
            if (line_f1!=last_record):
                write_output_difference(output_file,line_f1)
                last_record = line_f1
            str_f1 = file_1.readline().rstrip('\n')
        elif(line_f1[0]>line_f2[0]):
            str_f2 = file_2.readline().rstrip('\n')
        counter += 1
        if str_f1 == "":
            flag_1=True
        else:
            line_f1 = convert_string_to_array(str_f1)
        if str_f2 == "":
            flag_2=True
        else:
            line_f2 = convert_string_to_array(str_f2)
    print("Total Lines Read: "+str(counter))
