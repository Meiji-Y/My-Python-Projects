
def NumberToDigit(number):

    if number<10 :
            lst.append(number)
            lst.reverse()
            return lst
    else:
        
        lastdigit=number%10
        lst.append(lastdigit)
        number=number//10
        return NumberToDigit(number)


def func2(my_list,my_num):
    def insert_num(counter,length):
            
            if counter>length:
                return my_list
            else:
                my_list.insert(0,my_num)
                counter += 1
                return insert_num(counter,length)
    def replace_all(max_num,my_list,max_check):
            index = my_list.index(max_num)
            if max_num != max_check:           
                return my_list
            elif max_num == max_check:
                my_list[index]=my_num
                max_num= sorted_list.pop(len(sorted_list)-1)
                return replace_all(max_num,my_list,max_check)


    if len(my_list)%2 == 0:
        sorted_list=sorted(my_list)
        max_num= sorted_list.pop(len(my_list)-1)
        max_check=max_num
        replace_all(max_num,my_list,max_check)

    else:
        counter = 1
        length=len(my_list)
        insert_num(counter,length)
    return my_list


lst=[]
number=eval(input('Enter a number you want to convert a list:'))
my_list=NumberToDigit(number)
print(lst)
my_num=eval(input('Enter the number:'))
func2(lst,my_num)
print(lst)
