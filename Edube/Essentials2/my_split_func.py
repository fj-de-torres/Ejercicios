from os import system
system("cls || clear")
def my_split(input_string: str,custom_char=" ")->list:
    def_list = list()
    tmp_chain = str()
    for i in range(32,127):
        char_1 = chr(i)
        if not char_1.isalnum() or char_1 == "·":
            input_string = input_string.strip(char_1)
    if len(input_string) == 0:
        def_list = []
    else:
        for char_2 in input_string:
            if char_2 != custom_char:
                tmp_chain += char_2
            elif char_2 == custom_char:
                def_list.append(tmp_chain)
                tmp_chain =""
        def_list.append(tmp_chain)
    
    return def_list
# testing_string = input("Gimme a string! ")
# testing_separator=input("Spliting/separator character (space by default)? ")
# print(my_split(testing_string,testing_separator))
print(my_split("Ser o no ser, esa es la pregunta"))
print(my_split("Ser o no ser,esa es la pregunta"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))
