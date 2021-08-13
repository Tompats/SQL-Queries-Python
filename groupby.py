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



def write_output_groupby(output_file,array):
    for record in array:
        output_record = str(record[0])+"\t"+str(record[1])+"\n"
        output_file.write(output_record)


def get_lines_array(file_1):
    lines_array = []
    counter = 0
    #lines = file_1.readlines()
    for i in file_1:
        str_line = i.rstrip('\n')
        line = convert_string_to_array(str_line)
        lines_array.append(line)
    return lines_array



def merge_sort(lines_array):
    if len(lines_array)<=1:
        return lines_array
    else:
        mid = (len(lines_array))//2
        left = merge_sort(lines_array[:mid])
        right = merge_sort(lines_array[mid:])
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        if len(result) > 1:
            if result[-1][0] == result[-2][0]:
                sum = result[-2][1] + result[-1][1]
                key = result[-2][0]
                del result[-1]
                result[-1][0] = key
                result[-1][1] = sum


    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result




def group_by_and_sum(file_1):
    output_file = open("Rgroupby.tsv", "w")
    lines_array = get_lines_array(file_1)
    sorted_array = []
    #print(lines_array)
    sorted_array = merge_sort(lines_array)
    write_output_groupby(output_file,sorted_array)
