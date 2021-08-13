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


#prints the final array to the output file
def write_output_join(output_file,record):
    output_record = str(record[0])+"\t"+str(record[1])+"\t"+str(record[2])+"\n"
    output_file.write(output_record)



def merge_join(file_1,file_2):
    output_file = open("RjoinS.tsv", "w")

    #read the first line of the files as string and remove the  new line char
    str_f1 = file_1.readline().rstrip('\n')
    line_f1 = convert_string_to_array(str_f1)
    str_f2 = file_2.readline().rstrip('\n')
    line_f2 = convert_string_to_array(str_f2)

    #the joined line
    record = [0,0,0]

    flag_2 = False
    flag_1 = False
    counter = 1
    flag = 0
    buffer = []
    max_buffer = [0,' ']
    while not(flag_1) and not(flag_2):
        if(line_f1[0]==line_f2[0]):
            record[0] = line_f1[0]
            record[1] = line_f1[1]
            record[2] = line_f2[1]
            buffer.append(line_f2)
            write_output_join(output_file,record)
            str_f2 = file_2.readline().rstrip('\n')
            if str_f2 == "":
                flag_2=True
            else:
                line_f2 = convert_string_to_array(str_f2)
        elif(line_f1[0]<line_f2[0]):
            if(flag_1):
                flag_2 = True
                break
            str_f1 = file_1.readline().rstrip('\n')
            if str_f1 == "":
                flag_1=True
            else:
                line_f1 = convert_string_to_array(str_f1)
                if(len(buffer)>0):
                    if(line_f1[0] == buffer[0][0]):
                        for i in buffer:
                            record[0] = line_f1[0]
                            record[1] = line_f1[1]
                            record[2] = i[1]
                            write_output_join(output_file,record)
                    else:
                        #Keep the max size of buffer
                        if len(buffer)>= max_buffer[0]:
                            max_buffer[0] = len(buffer)
                            max_buffer[1] = buffer[0][0]
                        buffer = []
        elif(line_f1[0]>line_f2[0]):
            if flag_2:
                flag_1 = True
                break
            str_f2 = file_2.readline().rstrip('\n')
            if str_f2 == "":
                flag_2=True
            else:
                line_f2 = convert_string_to_array(str_f2)
        counter += 1
    print("Max Buffer Size & Key: "+str(max_buffer))
    print("Total Lines Read: "+str(counter))
