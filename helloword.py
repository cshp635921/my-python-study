def findstr(str1,str2):
    len_str1= len(str1) ;
    len_str2= len(str2);
    N=0;
    for i in range(len_str1-len_str2):
        if str1[i:i+len_str2] ==str2:
            N+=1;
        else:
            continue;
    return(N)
str1 = input('first one:')
str2 = input('second one:')
N = findstr(str1,str2)
print('The number is :%d'%N )

















