def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
         for line in f:
            linia=""
            for word in line.strip():
                if word == ",":
                    break
                linia = linia + word
            #print(linia)
            cast_list.append(linia)
 
    return cast_list



print(create_cast_list("C:/Users/php/Documents/phyton/phyton_test0/flyin_circus_cast.txt"))