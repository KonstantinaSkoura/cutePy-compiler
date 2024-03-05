#Konstantina Skoura 4168 cs04168
#Konstantinos Retsas 4163 cs04163
import sys


input_file = open(sys.argv[1], 'r')
my_file = open('endiamesos.int','w')
my_file2 = open('symbol_table.txt','w')
final_file = open('final_file.asm','w')
#In dictionary we have assigned integer values for every state,every symbol,every token,every keyword and every error.
my_dict = {
    # katastaseis
    "start": 0,
    "expected_number": 1,
    "expected_letter": 2,
    "katastasi_ison": 3,
    "katastasi_bigger": 4,
    "katastasi_smaller": 5,
    "katastasi_slash": 6,
    "katastasi_#": 7,
    "katastasi_comments": 8,
    "expected_$": 9,
    "expected_katwpaula": 10,
    "expected_ison": 11,
    # chars
    "white_char": 0,
    "letter": 1,
    "number": 2,
    "(": 3,
    ")": 4,
    "[": 5,
    "]": 6,
    "#": 7,
    "{": 8,
    "}": 9,
    "+": 10,
    "-": 11,
    "*": 12,
    "/": 13,
    '': 14,
    "akuros_xaraktiras": 15,
    ",": 16,
    ":": 17,
    ";": 18,
    "=": 19,
    "<": 20,
    ">": 21,
    '"': 22,
    "$": 23,
    "_": 24,
    "\n": 25,
    "!": 26,
    # tokens
    "arithmitiki_stathera_tk": 50,
    "identifier_tk": 51,
    "plus_tk": 52,
    "minus_tk": 53,
    "erwtimatiko_tk": 54,
    "komma_tk": 55,
    "anw_katw_teleia_tk": 56,
    "slash_tk": 57,
    "multiply_tk": 58,
    "bigger_tk": 59,
    "bigger or equal_tk": 60,
    "ison_tk": 61,
    "smaller_tk": 62,
    "smaller or equal_tk": 63,
    "diaforo_tk": 64,
    "anathesi_tk": 65,
    "quotes_tk": 66,
    "EOF_tk": 67,
    "kleisimo_agguli_tk": 68,
    "anoigma_agguli_tk": 69,
    "kleisimo_parenthesi_tk": 70,
    "anoigma_parenthesi_tk": 71,
    "anoigma_block_tk": 72,
    "kleisimo_block_tk": 73,
    # desmeymenes lexeis
    "def": 100,
    "__main__": 101,
    "#declare": 102,
    "if": 103,
    "else": 104,
    "and": 105,
    "or": 106,
    "not": 107,
    "return": 108,
    "while": 109,
    "__name__": 110,
    "input": 111,
    "int": 112,
    "print": 113,
    # errors
    "error_unknown_symbol": -1,
    "error_digit_before_letter": -2,
    "error_slash": -3,
    "error_hashtag": -4,
    "error_comments_not_closed": -5,
    "error_starts_with_katwpaula": -6,
    "error_dolario": -7,
    "error_panw_apo_30_xarakthres": -8,
    "error_arithmos_ektos_diasthmatos": -9,
    "error_anoigma_agkistrou_xwris_#": -10,
    "error_kleisimo_agkistrou_xwris_#": -11,
    "error_starts_with_!": -12,
}
#For our array we have the states that come from finite automato
my_array = [
    # start
    [my_dict["start"], my_dict["expected_letter"], my_dict["expected_number"], my_dict["anoigma_parenthesi_tk"],
     my_dict["kleisimo_parenthesi_tk"], my_dict["anoigma_agguli_tk"], my_dict["kleisimo_agguli_tk"], my_dict["katastasi_#"],
     my_dict["error_anoigma_agkistrou_xwris_#"], my_dict["error_kleisimo_agkistrou_xwris_#"], my_dict["plus_tk"], my_dict["minus_tk"],
     my_dict["multiply_tk"], my_dict["katastasi_slash"], my_dict["EOF_tk"], my_dict["error_unknown_symbol"],
     my_dict["komma_tk"], my_dict["anw_katw_teleia_tk"], my_dict["erwtimatiko_tk"], my_dict["katastasi_ison"],
     my_dict["katastasi_smaller"], my_dict["katastasi_bigger"], my_dict["quotes_tk"], my_dict["error_dolario"],
     my_dict["expected_katwpaula"], my_dict["start"], my_dict["expected_ison"]],

    # expected_number
    [my_dict["arithmitiki_stathera_tk"], my_dict["error_digit_before_letter"], my_dict["expected_number"], my_dict["arithmitiki_stathera_tk"],
     my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"],
     my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"],
     my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["error_unknown_symbol"],
     my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"],
     my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"],
     my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"], my_dict["arithmitiki_stathera_tk"]],

    # expected_letter
    [my_dict["identifier_tk"], my_dict["expected_letter"], my_dict["expected_letter"], my_dict["identifier_tk"],
     my_dict["identifier_tk"], my_dict["identifier_tk"], my_dict["identifier_tk"], my_dict["identifier_tk"],
     my_dict["error_anoigma_agkistrou_xwris_#"], my_dict["error_kleisimo_agkistrou_xwris_#"], my_dict["identifier_tk"], my_dict["identifier_tk"],
     my_dict["identifier_tk"], my_dict["identifier_tk"], my_dict["identifier_tk"], my_dict["error_unknown_symbol"],
     my_dict["identifier_tk"], my_dict["identifier_tk"], my_dict["identifier_tk"], my_dict["identifier_tk"],
     my_dict["identifier_tk"], my_dict["identifier_tk"], my_dict["identifier_tk"], my_dict["identifier_tk"],
     my_dict["expected_letter"], my_dict["identifier_tk"], my_dict["identifier_tk"]],

    # katastasi_ison
    [my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"],
     my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"],
     my_dict["error_anoigma_agkistrou_xwris_#"], my_dict["error_kleisimo_agkistrou_xwris_#"], my_dict["anathesi_tk"], my_dict["anathesi_tk"],
     my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["error_unknown_symbol"],
     my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["ison_tk"],
     my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"],
     my_dict["anathesi_tk"], my_dict["anathesi_tk"], my_dict["anathesi_tk"]],

    # katastasi_bigger
    [my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"],
     my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"],
     my_dict["error_anoigma_agkistrou_xwris_#"], my_dict["error_kleisimo_agkistrou_xwris_#"], my_dict["bigger_tk"], my_dict["bigger_tk"],
     my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["error_unknown_symbol"],
     my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger or equal_tk"],
     my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"],
     my_dict["bigger_tk"], my_dict["bigger_tk"], my_dict["bigger_tk"]],

    # katastasi_smaller
    [my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"],
     my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"],
     my_dict["error_anoigma_agkistrou_xwris_#"], my_dict["error_kleisimo_agkistrou_xwris_#"], my_dict["smaller_tk"], my_dict["smaller_tk"],
     my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["error_unknown_symbol"],
     my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller or equal_tk"],
     my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"],
     my_dict["smaller_tk"], my_dict["smaller_tk"], my_dict["smaller_tk"]],

    # katastash slash
    [my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"],
     my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"],
     my_dict["error_anoigma_agkistrou_xwris_#"], my_dict["error_kleisimo_agkistrou_xwris_#"], my_dict["error_slash"], my_dict["error_slash"],
     my_dict["error_slash"], my_dict["slash_tk"], my_dict["error_slash"], my_dict["error_unknown_symbol"],
     my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"],
     my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"],
     my_dict["error_slash"], my_dict["error_slash"], my_dict["error_slash"]],

    # katastash_hashtag
    [my_dict["error_hashtag"], my_dict["expected_letter"], my_dict["error_hashtag"], my_dict["error_hashtag"],
     my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["error_hashtag"],
     my_dict["anoigma_block_tk"], my_dict["kleisimo_block_tk"], my_dict["error_hashtag"], my_dict["error_hashtag"],
     my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["error_unknown_symbol"],
     my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["error_hashtag"],
     my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["katastasi_comments"],
     my_dict["error_hashtag"], my_dict["error_hashtag"], my_dict["error_hashtag"]],

    # katastasi_comment#
    [my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["expected_$"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["error_comments_not_closed"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"]],

    # expected_$
    [my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["error_comments_not_closed"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["start"],
     my_dict["katastasi_comments"], my_dict["katastasi_comments"], my_dict["katastasi_comments"]],

    # expected katw_paula
    [my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"],
     my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"],
     my_dict["error_anoigma_agkistrou_xwris_#"], my_dict["error_kleisimo_agkistrou_xwris_#"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"],
     my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_unknown_symbol"],
     my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"],
     my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"],
     my_dict["expected_letter"], my_dict["error_starts_with_katwpaula"], my_dict["error_starts_with_katwpaula"]],

    # expected ison
    [my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"],
     my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"],
     my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"],
     my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_unknown_symbol"],
     my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["diaforo_tk"],
     my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"],
     my_dict["error_starts_with_!"], my_dict["error_starts_with_!"], my_dict["error_starts_with_!"]],
]

# lektikos analytis

line = 1


def lex():
    state = my_dict["start"]
    num1 = 0
    string = ""
    global line
    array = [] #we store the token
    array1 = [] #we store the value of the token,the token and the line

    while state >= 0 and state <= 11:
        char = input_file.read(1) #we read one byte from our file
        # print(char)
        if char == '\t' or char == ' ':
            num1 = my_dict["white_char"]
            string += char

        elif char.isalpha():
            num1 = my_dict["letter"]
            string += char

        elif char.isdigit():
            num1 = my_dict["number"]
            string += char

        elif char == '(':
            num1 = my_dict["("]
            string += char

        elif char == ')':
            num1 = my_dict[")"]
            string += char

        elif char == '[':
            num1 = my_dict["["]
            string += char

        elif char == ']':
            num1 = my_dict["]"]
            string += char

        elif char == '#':
            num1 = my_dict["#"]
            string += char

        elif char == '{':
            num1 = my_dict["{"]
            string += char

        elif char == '}':
            num1 = my_dict["}"]
            string += char

        elif char == '+':
            num1 = my_dict["+"]
            string += char

        elif char == '-':
            num1 = my_dict["-"]
            string += char

        elif char == '*':
            num1 = my_dict["*"]
            string += char

        elif char == '/':
            num1 = my_dict["/"]
            string += char

        elif char == '':
            num1 = my_dict[""]
            string += char

        elif char == ',':
            num1 = my_dict[","]
            string += char

        elif char == ':':
            num1 = my_dict[":"]
            string += char

        elif char == ';':
            num1 = my_dict[";"]
            string += char

        elif char == '=':
            num1 = my_dict["="]
            string += char

        elif char == '<':
            num1 = my_dict["<"]
            string += char

        elif char == '>':
            num1 = my_dict[">"]
            string += char

        elif char == '"':
            num1 = my_dict['"']
            string += char

        elif char == '$':
            num1 = my_dict["$"]
            string += char

        elif char == '_':
            num1 = my_dict["_"]
            string += char

        elif char == '\n':
            num1 = my_dict["\n"]
            line += 1
            string += char
            
        elif char == '!':
            num1 = my_dict["!"]
            string += char

        else:
            num1 = my_dict["akuros_xaraktiras"]
            string += char

        state = my_array[state][num1]
        #When we have comments or we are at the start of our finite automato we empty the string
        if state == my_dict["katastasi_comments"] or state == my_dict["start"]:
            string = ""
        #when we have found these tokens we add them at the array and we check the last char and then we go back a byte at the file so the aytomato can read it from the start
    if state == my_dict["identifier_tk"] or state == my_dict["arithmitiki_stathera_tk"] or state == my_dict["anathesi_tk"] or state == my_dict["bigger_tk"] or state == my_dict["smaller_tk"]:
        char1 = string[-1]
        if char1 == '\n':
            line -= 1
        array.append(string[:-1])
        if string[:-1] in my_dict.keys() and state != my_dict["anathesi_tk"] and state != my_dict["bigger_tk"] and state != my_dict["smaller_tk"]:
            state = my_dict[string[:-1]]
            if string[:-1] == "number" or string[:-1] == "letter":
                state = my_dict["identifier_tk"]
        input_file.seek(input_file.tell() - 1, 0) #we go back one byte from the pos we already are
    else:
        array.append(string)
#we check the length of id_tk and the range at numerical constant
    if state == my_dict["identifier_tk"]:
        if len(array[0]) > 30:
            state = my_dict["error_panw_apo_30_xarakthres"]
    if state == my_dict["arithmitiki_stathera_tk"]:
        if (int(array[0])) < -(2 ** 32 - 1) or (int(array[0])) > (2 ** 32 - 1):
            state = my_dict["error_arithmos_ektos_diasthmatos"]
    if state == my_dict["error_unknown_symbol"]:
        print("Error unknown symbol")
    elif state == my_dict["error_digit_before_letter"]:
        print("Error there is a digit before letter")
    elif state == my_dict["error_slash"]:
        print("Error there is a / alone")
    elif state == my_dict["error_hashtag"]:
        print("Error there is a # alone")
    elif state == my_dict["error_comments_not_closed"]:
        print("Error comments not closed")
    elif state == my_dict["error_starts_with_katwpaula"]:
        print("Error starts with _ ")
    elif state == my_dict["error_dolario"]:
        print("Error there is $ alone")
    elif state == my_dict["error_anoigma_agkistrou_xwris_#"]:
        print("Error there is { without #")
    elif state == my_dict["error_kleisimo_agkistrou_xwris_#"]:
        print("Error there is } without #")
    elif state == my_dict["error_panw_apo_30_xarakthres"]:
        print("Error word over 30 chars")
    elif state == my_dict["error_arithmos_ektos_diasthmatos"]:
        print("Error number out of range")
    elif state == my_dict["error_starts_with_!"]:
        print("Error starts with !")
    array1.append(state)
    array1.append(array[0])
    array1.append(line)
    return array1



fullist = []
fullist2 = []
quadlabel = 1
counter = -1
isArgument = True

def nextQuad():
    global fullist
    global quadlabel
    return quadlabel

def genQuad(op,x,y,z):
    global fullist
    global fullist2
    global quadlabel
    my_list = []
    my_list = [nextQuad()]
    my_list.insert(1,str(op))
    my_list.insert(2,str(x))
    my_list.insert(3,str(y))
    my_list.insert(4,str(z))
    fullist += [my_list]
    fullist2 += [my_list]
    quadlabel = quadlabel + 1
    return my_list

def new_temp():
    global fullist
    global counter
    counter += 1
    entity = Entity()
    entity_assign(entity,"%" + str(counter),"TEMPORARYVARIABLE",calculate_offset())
    add_entity(entity)

    return "%" + str(counter)

def empty_list():
    return []

def makeList(label):
    return [label]

def merge(list1,list2):
    return list1 +list2


def backPatch(list,z):
    global fullist
    list.sort()
    y = 0
    count = 0
    for i in list:
        for j in fullist[y:]:
            if j[0] == i:
                j[4] = str(z)
                count += 1
                y = count
                break
            else:
                count += 1
        count = 0


def print_listOfAllQuads():
    global fullist
    for i in fullist:
        print(str(i )+ "\n")

def write_Quads(x):
    global fullist
    for i in range(len(fullist)):
        z = fullist[i]
        for y in z:
            if y == z[0]:
                x.write(str(y) + ": ")
            else:
                x.write(str(y) + " ")
        x.write('\n')

#pinakas symbolwn ---------------------------------------------------------------------------------------
list_of_scopes = []
class Scope():
    def __init__(self):
        self.name = ''						#we initialize our class Scope with name,list of entities and nestinglevel
        self.entityList = []
        self.nestingLevel = 0

class Entity():
    def __init__(self):
        self.name = ''			#we initialize our class entity with the name and datatype(variable,function,parameter,temporaryvariable)
        self.datatype = ''
        self.variable = self.Variable() #we create 4 objects from the classes who inherit the name and datatype from entity
        self.function = self.Function()
        self.parameter = self.Parameter()
        self.temporaryVariable = self.TemporaryVariable()


    class Variable:
        def __init__(self):
            self.offset = 0  # the distance from the start of the stack


    class Function:
        def __init__(self):
            self.startingQuad = 0  # first quad since the function begins
            self.frameLength = 0 #length activation record
            self.argumentList = []  # the arguments of the function
            self.nestingLevel = 0


    class Parameter:
        def __init__(self):
            self.offset = 0  # distance from the start of the stack


    class TemporaryVariable:
        def __init__(self):
            self.offset = 0  # distance from the start of the stack



class Argument():
    def __init__(self):
        self.name = ''		#we initialize the name of the argument
        self.datatype = 'INT'#the datatype of the arguments is int


def add_entity(entity):  # we add a new entity at the entityList of the last scope in the list_of_scopes
    global list_of_scopes
    list_of_scopes[-1].entityList = list_of_scopes[-1].entityList + [entity]

count = 0 #global variable  that we increment when we add a new scope in the list_of_scopes
def nestingLevel_assign(scope): #we assign the global var count at the nestinglevel of a scope
    global count
    scope.nestingLevel = count

def add_argument(argument):  # we add a new argument at the argumentlist  of the last entity
    global list_of_scopes
    list_of_scopes[-1].entityList[-1].function.argumentList = list_of_scopes[-1].entityList[-1].function.argumentList + [argument]

def add_scope(name):  # we add a new scope at the list_of scopes
    global list_of_scopes
    global count

    nextScope = Scope()
    nextScope.name = name
    if len(list_of_scopes) >= 1:
        count += 1
        nestingLevel_assign(nextScope)

    list_of_scopes.append(nextScope)


def delete_scope():
    global list_of_scopes
    global count
    count = 0
    for i in range(len(list_of_scopes[-1].entityList)): #we delete from the list each entity of the last scope in the list_of_scopes
        list_of_scopes[-1].entityList.pop()
    del list_of_scopes[-1] #we delete the last scope


def calculate_offset():
    global list_of_scopes
    offset = 12 #the first entity  is 12 bytes

    if len(list_of_scopes[-1].entityList) >= 1:  #for each entity except the entity (Function) we increment the offset by 4 bytes
        for i in range( len(list_of_scopes[-1].entityList)):
            if list_of_scopes[-1].entityList[i].datatype == 'VARIABLE' or list_of_scopes[-1].entityList[i].datatype == 'TEMPORARYVARIABLE' \
                    or list_of_scopes[-1].entityList[i].datatype == 'PARAMETER':
                offset += 4
    return offset


def calculate_framelength():   #we calculate the framelength of the last entity of the scope that is before the last scope
    global list_of_scopes
    list_of_scopes[-2].entityList[-1].function.frameLength = calculate_offset()


def calculate_startingQuad():   #we find the first quad of the last entity of the scope that is before the last scope
    global list_of_scopes
    list_of_scopes[-2].entityList[-1].function.startingQuad = nextQuad()

def find_entity(x): #we search for the entity by the name
    global list_of_scopes
    if len(list_of_scopes) > 0:
        for j in range(len(list_of_scopes)-1,-1,-1):
            for i in list_of_scopes[j].entityList:
                if i.name == x:
                    return(list_of_scopes[j],i)
        print("There is not entity with  name : " + str(x))
        exit()



def entity_assign(en,name1,type1,offset1): #we assign the name,type and offset at the object entity that we give
    en.name = name1
    en.datatype = type1
    if en.datatype == "PARAMETER":
        en.parameter.offset = offset1
    elif en.datatype == "VARIABLE":
        en.variable.offset = offset1
    elif en.datatype == "TEMPORARYVARIABLE":
        en.temporaryVariable.offset = offset1


def add_parameters():  # we add a new entity for each argument in the scope before the last scope
    global list_of_scopes

    for i in list_of_scopes[-2].entityList[-1].function.argumentList:
        entity = Entity()
        entity_assign(entity,i.name,"PARAMETER",calculate_offset())
        add_entity(entity)
def show_symbols(file): #we print our symbol table at the file
    global list_of_scopes
    file.write("-------------------------------------------------------------------------------------------------")
    file.write("\n")
    for i in list_of_scopes:
        file.write("\n")
        file.write("Scope: " + str(i.name) + " " + "nestingLevel: " + str(i.nestingLevel))
        for j in i.entityList:
            file.write("\n")
            file.write("     Entity: " + str(j.name) + " " + str(j.datatype))
            file.write("\n")
            if j.datatype == "VARIABLE":
                file.write("     Offset is :" + str(j.variable.offset))
                file.write("\n")
            elif j.datatype == "PARAMETER":
                file.write("     Offset is :" + str(j.parameter.offset))
                file.write("\n")
            elif j.datatype == "TEMPORARYVARIABLE":
                file.write("     Offset is :" + str(j.temporaryVariable.offset))
                file.write("\n")
            elif j.datatype == "FUNCTION":
                file.write("     Framelength of " + str(j.name) + " is : " + str(j.function.frameLength))
                file.write("\n")
                file.write("     StartingQuad of " + str(j.name) + " is : " + str(j.function.startingQuad))
                file.write("\n")
                for k in j.function.argumentList:
                    file.write("         Argument: " + str(k.name) + " " + str(k.datatype))
                    file.write("\n")

################################ telikos kwdikas ###########################################################

def gnlvcode(y):
    global list_of_scopes
    (my_scope, my_entity) = find_entity(y)
    n = list_of_scopes[-1].nestingLevel - my_scope.nestingLevel - 1
    final_file.write('lw t0,-4(sp)\n')
    while n > 0:
        final_file.write('lw t0,-4(t0)\n')
        n = n - 1
    if my_entity.datatype == 'VARIABLE':
        my_offset = my_entity.variable.offset
        final_file.write('addi t0,t0,-%d\n' % my_offset)
    elif my_entity.datatype == 'PARAMETER':
        my_offset = my_entity.parameter.offset
        final_file.write('addi t0,t0,-%d\n' % my_offset)



def loadvr(v,r):
    if v.isdigit():
        final_file.write('li t%s,%s\n' % (r,v))
    else:
        (my_scope,my_entity) = find_entity(v)
        if my_scope.nestingLevel == 0:
            if my_entity.datatype == "VARIABLE":
                final_file.write('lw t%s,-%d(gp)\n' % (r, my_entity.variable.offset))
            elif my_entity.datatype == "TEMPORARYVARIABLE":
                final_file.write('lw t%s,-%d(gp)\n' % (r, my_entity.temporaryVariable.offset))

        elif my_scope.nestingLevel == list_of_scopes[-1].nestingLevel:
            if my_entity.datatype == "VARIABLE":
                final_file.write('lw t%s,-%d(sp)\n' % (r, my_entity.variable.offset))
            elif my_entity.datatype == "TEMPORARYVARIABLE":
                final_file.write('lw t%s,-%d(sp)\n' % (r, my_entity.temporaryVariable.offset))
            elif my_entity.datatype == "PARAMETER":
                final_file.write('lw t%s,-%d(sp)\n' % (r, my_entity.parameter.offset))

        elif my_scope.nestingLevel < list_of_scopes[-1].nestingLevel:
            if my_entity.datatype == "VARIABLE":
                gnlvcode(v)
                final_file.write('lw t%s,(t0)\n' % r)
            elif my_entity.datatype == "PARAMETER":
                gnlvcode(v)
                final_file.write('lw t%s,(t0)\n' % r)

def storerv(r,v):
    (my_scope, my_entity) = find_entity(v)
    if my_scope.nestingLevel == 0:
        if my_entity.datatype == "VARIABLE":
            final_file.write('sw t%d,-%d(gp)\n' % (r,my_entity.variable.offset))
        elif my_entity.datatype == "TEMPORARYVARIABLE":
            final_file.write('sw t%d,-%d(gp)\n' % (r, my_entity.temporaryVariable.offset))

    elif my_scope.nestingLevel == list_of_scopes[-1].nestingLevel:
        if my_entity.datatype == "VARIABLE":
            final_file.write('sw t%d,-%d(sp)\n' % (r, my_entity.variable.offset))
        elif my_entity.datatype == "TEMPORARYVARIABLE":
            final_file.write('sw t%d,-%d(sp)\n' % (r, my_entity.temporaryVariable.offset))
        elif my_entity.datatype == "PARAMETER":
            final_file.write('sw t%d,-%d(sp)\n' % (r, my_entity.parameter.offset))

    elif my_scope.nestingLevel < list_of_scopes[-1].nestingLevel:
        if my_entity.datatype == "VARIABLE":
            gnlvcode(v)
            final_file.write('sw t%d,(t0)\n' % r)
        elif my_entity.datatype == "PARAMETER":
            gnlvcode(v)
            final_file.write('sw t%d,(t0)\n' % r)


final_file.write('       \n')
my_count = 0
def generate_final():
    global fullist
    global fullist2
    global my_count
    relop_operators = ['==', '!=', '<', '<=', '>', '>=']
    assembly_operators = ['beq', 'bne', 'blt', 'ble', 'bgt', 'bge']
    numerical_op = ['+', '-', '*', '//']
    assembly_op = ['add', 'sub', 'mul', 'div']
    final_flag = 0
    for i in fullist2:
        final_file.write('L' + str(i[0]) + ': \n')
        if i[1] == "jump":
            final_file.write('j L'+str(i[4])+'\n')
        elif i[1] in relop_operators:
            x = assembly_operators[relop_operators.index(i[1])]
            loadvr(i[2], 1)
            loadvr(i[3], 2)
            final_file.write(x + ' ,t1, t2, L' + i[4] + '\n')
        elif i[1] in numerical_op:
            x = assembly_op[numerical_op.index(i[1])]
            loadvr(i[2], 1)
            loadvr(i[3], 2)
            final_file.write(x + ' ,t1, t1,t2 \n')
            storerv(1, i[4])
        elif i[1] == '=':
            loadvr(i[2], 1)
            storerv(1, i[4])
        elif i[1] == 'retv':
            loadvr(i[2], '1')
            final_file.write('lw t0, -8(sp)\n')
            final_file.write('sw t1, 0(t0)\n')
            final_file.write('lw ra, 0(sp)\n')
            final_file.write('jr ra\n')
        elif i[1] == 'inp':
            final_file.write('li a7,5' + '\n')
            final_file.write('ecall' + '\n')
            final_file.write('mv t1,a0' + '\n')
            storerv(1, i[2])
        elif i[1] == 'out':
            loadvr(i[2], 1)
            final_file.write('mv a0,t1' + '\n')
            final_file.write('li a7,1' + '\n')
            final_file.write('ecall' + '\n')
        elif i[1] == 'halt':
            final_file.write('li a0,0\n')
            final_file.write('li a7,93\n')
            final_file.write('ecall\n')
        elif i[1] == 'begin_block' and list_of_scopes[-1].nestingLevel != 0:
            final_file.write('sw ra,(sp)\n')
        elif i[1] == 'end_block' and list_of_scopes[-1].nestingLevel != 0:
            final_file.write('lw ra,(sp)\n')
            final_file.write('jr ra\n')
        elif i[1] == 'begin_block' and list_of_scopes[-1].nestingLevel == 0:
            final_file.seek(0,0)
            final_file.write('j L%d\n' % i[0])
            final_file.seek(0,2)
            final_file.write('addi sp,sp,%d\n' % calculate_offset())
            final_file.write('mv gp,sp\n')
        elif i[1] == 'par':
            j = fullist.index(i)
            for k in fullist[j:]:
                if k[1] == 'call' and final_flag == 0:
                    (my_scope,my_entity) = find_entity(k[2])
                    final_file.write('addi fp,sp,%d\n' % my_entity.function.frameLength)
                    final_flag = 1
                    break
            if i[3] == 'CV':
                loadvr(i[2],0)
                final_file.write('sw t0, -%d(fp)\n' % (12 + 4 * my_count))
                my_count = my_count + 1
            elif i[3] == 'RET':
                (my_scope, my_entity) = find_entity(i[2])
                final_file.write('addi t0,sp,-%d\n' % my_entity.temporaryVariable.offset)
                final_file.write('sw t0, -8(fp)\n')
        elif i[1] == 'call':
            final_flag = 0
            my_count = 0
            (my_scope,my_entity) = find_entity(i[2])
            if list_of_scopes[-1].nestingLevel < my_entity.function.nestingLevel:
                final_file.write('sw sp,-4(fp)\n')
            elif list_of_scopes[-1].nestingLevel == my_entity.function.nestingLevel:
                final_file.write('lw t0,-4(sp)\n')
                final_file.write('sw t0,-4(fp)\n')
            final_file.write('addi sp,sp,%d\n' % my_entity.function.frameLength)
            final_file.write('jal L%d\n' % my_entity.function.startingQuad)
            final_file.write('addi sp,sp,-%d\n' % my_entity.function.frameLength)


        fullist2 = []


# syntaktikos analytis
def syn():
    global fullist
    global line
    global tokens
    tokens = lex()
    line = tokens[2]
    add_scope('main')
    def startRule():

        def_main_part()
        call_main_part()

    def def_main_part():
        global tokens
        global line
        
        def_main_function()
        while tokens[0] == my_dict["def"]:
            def_main_function()

    def def_main_function():
        global line
        global tokens
        global  list_of_scopes
        if tokens[0] == my_dict["def"]:
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["identifier_tk"]:
                ID = tokens[1]
                tokens = lex()
                line = tokens[2]
                if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                        tokens = lex()
                        line = tokens[2]
                        entity = Entity()
                        entity.datatype = 'FUNCTION'  
                        entity.name = ID
                        entity.function.nestingLevel = list_of_scopes[-1].nestingLevel + 1
                        add_entity(entity)
                        if tokens[0] == my_dict["anw_katw_teleia_tk"]:
                            tokens = lex()
                            line = tokens[2]
                            add_scope(ID)
                            if tokens[0] == my_dict["anoigma_block_tk"]:
                                tokens = lex()
                                line = tokens[2]
                                declarations()
                                while tokens[0] == my_dict["def"]:
                                    def_function()
                                calculate_startingQuad()
                                genQuad('begin_block',ID, '_', '_')
                                statements()
                                if tokens[0] == my_dict["kleisimo_block_tk"]:
                                    calculate_framelength()
                                    genQuad('end_block', ID, '_', '_')
                                    show_symbols(my_file2)

                                    tokens = lex()
                                    line = tokens[2]
                                    generate_final()
                                    delete_scope()
                                else:
                                    print("Error,the program does not have #} after #{ at main function in line",line)
                                    exit(-1)
                            else:
                                print("Error,the program does not have #{ after main function in line",line)
                                exit(-1)
                        else:
                            print("Error,the program does not have : after main function in line",line)
                            exit(-1)
                    else:
                        print("Error,the program does not have a ) after ( at main function in line",line)
                        exit(-1)
                else:
                    print("Error,the program does not have ( after main function in line",line)
                    exit(-1)
            else:
                print("Error,the program does not have a name for main function in line",line)
                exit(-1)
        else:
            print("Error,the program doesnt start with def  at main function in line", line)
            exit(-1)

    def def_function():
        global line
        global tokens
        global list_of_scopes
        global isArgument



        if tokens[0] == my_dict["def"]:
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["identifier_tk"]:
                ID = tokens[1]
                tokens = lex()
                line = tokens[2]
                entity = Entity()
                entity.datatype = 'FUNCTION'
                entity.name = ID
                entity.function.nestingLevel = list_of_scopes[-1].nestingLevel + 1
                add_entity(entity)
                if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    isArgument = True
                    id_list()
                    if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                        tokens = lex()
                        line = tokens[2]
                        add_scope(ID)
                        if tokens[0] == my_dict["anw_katw_teleia_tk"]:
                            tokens = lex()
                            line = tokens[2]
                            if tokens[0] == my_dict["anoigma_block_tk"]:
                                tokens = lex()
                                line = tokens[2]
                                add_parameters()
                                declarations()
                                while tokens[0] == my_dict["def"]:
                                    def_function()
                                calculate_startingQuad()
                                genQuad('begin_block', ID, '_', '_')
                                statements()
                                calculate_framelength()
                                if tokens[0] == my_dict["kleisimo_block_tk"]:
                                    genQuad('end_block', ID, '_', '_')
                                    show_symbols(my_file2)

                                    tokens = lex()
                                    line = tokens[2]
                                    generate_final()
                                    delete_scope()
                                else:
                                    print("Error,the program does not have #} after #{ at function in line", line)
                                    exit(-1)
                            else:
                                print("Error,the program does not have #{ after function in line", line)
                                exit(-1)
                        else:
                            print("Error,the program does not have : after function in line", line)
                            exit(-1)
                    else:
                        print("Error,the program does not have a ) after ( at function in line", line)
                        exit(-1)
                else:
                    print("Error,the program does not have ( after function in line", line)
                    exit(-1)
            else:
                print("Error,the program does not have a name for  function in line", line)
                exit(-1)
        else:
            print("Error,the program doesnt start with def in line", line)
            exit(-1)

    def declarations():
        global tokens
        global line

        while tokens[0] == my_dict["#declare"]:
            declaration_line()

    def declaration_line():
        global tokens
        global line
        global isArgument


        if tokens[0] == my_dict["#declare"]:
            tokens = lex()
            line = tokens[2]
            isArgument = False
            id_list()

    def statement():
        global tokens
        global line

        if tokens[0] == my_dict["identifier_tk"] or tokens[0] == my_dict["print"] or tokens[0] == my_dict["return"]:
            simple_statement()
        elif tokens[0] == my_dict["if"] or tokens[0] == my_dict["while"]:
            structured_statement()
        else:
            print("Error,something is wrong with your statement in line", line)
            exit(-1)

    def statements():
        global tokens
        global line
        
        statement()
        while tokens[0] == my_dict["identifier_tk"] or tokens[0] == my_dict["print"] or tokens[0] == my_dict["return"] or tokens[0] == my_dict["if"]  or tokens[0] == my_dict["while"]:
            statement()

    def simple_statement():
        global tokens
        global line
        
        if tokens[0] == my_dict["identifier_tk"]:
            assignment_stat()
        elif tokens[0] == my_dict["print"]:
            print_stat()
        elif tokens[0] == my_dict["return"]:
            return_stat()

    def structured_statement():
        global tokens
        global line
        
        if tokens[0] == my_dict["if"]:
            if_stat()
        elif tokens[0] == my_dict["while"]:
            while_stat()

    def assignment_stat():
        global tokens
        global line

        if tokens[0] == my_dict["identifier_tk"]:
            idplace = tokens[1]
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["anathesi_tk"]:
                tokens = lex()
                line = tokens[2]
                if tokens[0] == my_dict["int"]:
                    tokens = lex()
                    line = tokens[2]
                    genQuad('inp', idplace, '_', '_')
                    if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                        tokens = lex()
                        line = tokens[2]
                        if tokens[0] == my_dict["input"]:
                            tokens = lex()
                            line = tokens[2]
                            if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                                tokens = lex()
                                line = tokens[2]
                                if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                                    tokens = lex()
                                    line = tokens[2]
                                    if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                                        tokens = lex()
                                        line = tokens[2]
                                        if tokens[0] == my_dict["erwtimatiko_tk"]:
                                            tokens = lex()
                                            line = tokens[2]
                                        else:
                                            print("Error,there is not ; after assigmnent in line",line)
                                            exit(-1)
                                    else:
                                        print("Error,there is not ) after int( in line", line)
                                        exit(-1)
                                else:
                                    print("Error,there is not ) after input( in line", line)
                                    exit(-1)
                            else:
                                print("Error,there is not ( after input in line",line)
                                exit(-1)
                        else:
                            print("Error,there is not input after ( in line",line)
                            exit(-1)
                    else:
                        print("Error,there is not ( after int in line",line)
                        exit(-1)
                else:
                    Eplace = expression()
                    genQuad('=', Eplace, '_', idplace)
                    if tokens[0] == my_dict["erwtimatiko_tk"]:
                        tokens = lex()
                        line = tokens[2]
                    else:
                        print("Error ,there is not ; after assignment in line", line)
                        exit(-1)
            else:
                print("Error, there is not = for assignment statement in line",line)
                exit(-1)
        else:
            print("Error,there is not an identifier for assignment in line",line)
            exit(-1)

    def print_stat():
        global tokens
        global line
        
        if tokens[0] == my_dict["print"]:
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                tokens = lex()
                line = tokens[2]
                Eplace = expression()
                genQuad('out', Eplace, '_', '_')
                if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    if tokens[0] == my_dict["erwtimatiko_tk"]:
                        tokens = lex()
                        line = tokens[2]
                    else:
                        print("Error,there is not ; after print in line",line)
                        exit(-1)
                else:
                    print("Error,there is not ) after print( in line",line)
                    exit(-1)
            else:
                print("Error,there is not ( after print in line",line)
                exit(-1)
        else:
            print("Error,there is not print in line",line)
            exit(-1)

    def return_stat():
        global tokens
        global line
        
        if (tokens[0] == my_dict["return"]):
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                tokens = lex()
                line = tokens[2]
                Eplace = expression()
                genQuad('retv', Eplace, '_', '_')
                if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    if tokens[0] == my_dict["erwtimatiko_tk"]:
                        tokens = lex()
                        line = tokens[2]
                    else:
                        print("Error,there is not ; after return in line",line)
                        exit(-1)
                else:
                    print("Error,there is not ) after return( in line",line)
                    exit(-1)
            else:
                print("Error,there is not ( after return in line",line)
                exit(-1)
        else:
            print("Error,there is not return in line",line)
            exit(-1)

    def if_stat():
        global tokens
        global line
        global ifList
        Btrue = []
        Bfalse = []
        ifList = []

        if tokens[0] == my_dict["if"]:
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                tokens = lex()
                line = tokens[2]
                B = condition()
                Btrue = B[0]
                Bfalse = B[1]
                backPatch(Btrue, nextQuad())
                if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    if tokens[0] == my_dict["anw_katw_teleia_tk"]:
                        tokens = lex()
                        line = tokens[2]
                        if tokens[0] == my_dict["anoigma_block_tk"]:
                            tokens = lex()
                            line = tokens[2]

                            statements()
                            ifList = makeList(nextQuad())
                            genQuad("jump", "_", "_", "_")
                            backPatch(Bfalse, nextQuad())
                            if tokens[0] == my_dict["kleisimo_block_tk"]:
                                tokens = lex()
                                line = tokens[2]
                            else:
                                print("Error there is not #} after if #{ in line", line)
                                exit(-1)
                        else:
                            statement()
                            ifList = makeList(nextQuad())
                            genQuad('jump', '_', '_', '_')
                            backPatch(Bfalse, nextQuad())
                        if tokens[0] == my_dict["else"]:
                            tokens = lex()
                            line = tokens[2]
                            if tokens[0] == my_dict["anw_katw_teleia_tk"]:
                                tokens = lex()
                                line = tokens[2]
                                if tokens[0] == my_dict["anoigma_block_tk"]:
                                    tokens = lex()
                                    line = tokens[2]
                                    statements()
                                    backPatch(ifList, nextQuad())
                                    if tokens[0] == my_dict["kleisimo_block_tk"]:
                                        tokens = lex()
                                        line = tokens[2]
                                    else:
                                        print("Error there is not #} after else: #{ in line", line)
                                        exit(-1)
                                else:
                                    statement()
                                    backPatch(ifList, nextQuad())
                            else:
                                print("Error,there is not : after else in line",line)
                                exit(-1)
                        else:
                            backPatch(ifList,nextQuad())
                    else:
                        print("Error,there is not : after if in line",line)
                        exit(-1)
                else:
                    print("Error,there is not ) after if( in line",line)
                    exit(-1)
            else:
                print("Error,there is not ( after if in line",line)
                exit(-1)
        else:
            print("Error,there is not if in line",line)
            exit(-1)

    def while_stat():
        global tokens
        global line
        Btrue = []
        Bfalse = []

        if tokens[0] == my_dict["while"]:
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                tokens = lex()
                line = tokens[2]
                Bquad = nextQuad()
                B = condition()
                Btrue = B[0]
                Bfalse = B[1]
                backPatch(Btrue, nextQuad())
                if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    if tokens[0] == my_dict["anw_katw_teleia_tk"]:
                        tokens = lex()
                        line = tokens[2]
                        if tokens[0] == my_dict["anoigma_block_tk"]:
                            tokens = lex()
                            line = tokens[2]
                            statements()
                            genQuad("jump","_","_",Bquad)
                            backPatch(Bfalse,nextQuad())
                            if tokens[0] == my_dict["kleisimo_block_tk"]:
                                tokens = lex()
                                line = tokens[2]
                            else:
                                print("Error there is not #} after while #{ in line", line)
                                exit(-1)
                        else:
                            statement()
                            genQuad("jump", "_", "_", Bquad)
                            backPatch(Bfalse, nextQuad())
                    else:
                        print("Error,there is not : after while in line", line)
                        exit(-1)
                else:
                    print("Error,there is not ) after while( in line", line)
                    exit(-1)
            else:
                print("Error,there is not ( after while in line", line)
                exit(-1)
        else:
            print("Error,there is not while in line", line)
            exit(-1)

    def id_list():
        global tokens
        global line
        global  isArgument


        if tokens[0] == my_dict["identifier_tk"]:
            ID = tokens[1]
            tokens = lex()
            line = tokens[2]

            if isArgument == True:  #if it is argument and it was called from the def_function
                argument = Argument()
                argument.name = ID
                add_argument(argument) # we add a new argument at the argumentList
            else:  #if it is a variable  and it was called from the declaration_line
                entity = Entity()
                entity_assign(entity,ID,"VARIABLE",calculate_offset()) #we assign values at the fields of the object entity
                add_entity(entity)  #we add the entity at the EntityList

            while tokens[0] == my_dict["komma_tk"]:
                tokens = lex()
                line = tokens[2]
                ID = tokens[1]
                if tokens[0] == my_dict["identifier_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    if isArgument == True:  #if it is an argument and it was called from the def_function
                        argument = Argument()
                        argument.name = ID
                        add_argument(argument)  #we add the argument at the argumentList
                    else:
                        entity = Entity()  #if it is a variable and it was called from the declaration_line
                        entity_assign(entity, ID, "VARIABLE", calculate_offset())
                        add_entity(entity)  #we add the entity at the entityList
                else:
                    print("Error,there is not identifier after , in line", line)
                    exit(-1)

    def expression():
        global tokens
        global line
        optional_sign()
        T1place = term()
        while tokens[0] == my_dict["plus_tk"] or tokens[0] == my_dict["minus_tk"]:
            add_operator = ADD_OP()
            T2place = term()
            w = new_temp()
            genQuad(add_operator,T1place,T2place,w)
            T1place = w
        Eplace = T1place
        return Eplace

    def term():
        global tokens
        global line

        F1place = factor()
        while tokens[0] == my_dict["multiply_tk"] or tokens[0] == my_dict["slash_tk"]:
            mul_operator = MUL_OP()
            F2place = factor()
            w = new_temp()
            genQuad(mul_operator,F1place,F2place,w)
            F1place = w
        Tplace = F1place
        return Tplace

    def factor():
        global tokens
        global line

        if tokens[0] == my_dict["arithmitiki_stathera_tk"]:
            Fplace = tokens[1]
            tokens = lex()
            line = tokens[2]

        elif tokens[0] == my_dict["anoigma_parenthesi_tk"]:
            tokens = lex()
            line = tokens[2]
            Eplace = expression()
            if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                Fplace = Eplace
                tokens = lex()
                line = tokens[2]
            else:
                print("Error,there is not ) after ( at factor in line", line)
                exit(-1)
        elif tokens[0] == my_dict["identifier_tk"]:
            function_name = tokens[1]
            tokens = lex()
            line = tokens[2]
            Fplace = idtail(function_name)
        else:
            print("Error,there is not numerical constant or expression or identifier at factor in line", line)
            exit(-1)
        return Fplace

    def idtail(function_name):
        global tokens
        global line

        if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
            tokens = lex()
            line = tokens[2]
            actual_par_list()
            w = new_temp()
            genQuad('par', w, 'RET', '_')
            genQuad('call', function_name, '_', '_')
            if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                tokens = lex()
                line = tokens[2]
                return w
            else:

                print("Error ,there is not ) after ( at idtail ",line)
                exit(-1)
        else:
            return function_name

    def actual_par_list():
        global tokens
        global line

        if tokens[0] == my_dict["arithmitiki_stathera_tk"] or tokens[0] == my_dict["anoigma_parenthesi_tk"] or tokens[0] == my_dict["identifier_tk"]:
            Eplace = expression()
            genQuad('par', Eplace, 'CV', '_')
            while tokens[0] == my_dict["komma_tk"]:
                tokens = lex()
                line = tokens[2]
                Eplace = expression()
                genQuad('par', Eplace, 'CV', '_')

    def optional_sign():
        global tokens
        global line

        if tokens[0] == my_dict["plus_tk"] or tokens[0] == my_dict["minus_tk"]:
            ADD_OP()

    def ADD_OP():
        global tokens
        global line
        add_operator = tokens[1]
        if tokens[0] == my_dict["plus_tk"]:
            tokens = lex()
            line = tokens[2]
        elif tokens[0] == my_dict["minus_tk"]:
            tokens = lex()
            line = tokens[2]
        return add_operator

    def MUL_OP():
        global tokens
        global line
        mull_operator = tokens[1]

        if tokens[0] == my_dict["multiply_tk"]:
            tokens = lex()
            line = tokens[2]
        elif tokens[0] == my_dict["slash_tk"]:
            tokens = lex()
            line = tokens[2]
        return mull_operator

    def condition():
        global tokens
        global line
        Btrue = []
        Bfalse = []
        Q1 = bool_term()
        Q1true = Q1[0]
        Q1false = Q1[1]
        Btrue = Q1true
        Bfalse = Q1false
        while tokens[0] == my_dict["or"]:
            backPatch(Q1false, nextQuad())
            tokens = lex()
            line = tokens[2]
            Q2 = bool_term()
            Q2true = Q2[0]
            Q2false = Q2[1]
            Btrue =merge(Q1true,Q2true)
            Bfalse = Q2false
        return Btrue,Bfalse

    def bool_term():
        global tokens
        global line
        Btrue = []
        Bfalse = []


        B1 = bool_factor()
        Qtrue = B1[0]
        Qfalse = B1[1]
        Btrue = Qtrue
        Bfalse = Qfalse

        while tokens[0] == my_dict["and"]:
            backPatch(Qtrue, nextQuad())
            tokens = lex()
            line = tokens[2]
            B2 = bool_factor()
            Q2true = B2[0]
            Q2false = B2[1]
            Qfalse = merge(Qfalse,Q2false)
            Qtrue = Q2true
            Btrue = Qtrue
            Bfalse = Qfalse
        return Btrue,Bfalse

    def bool_factor():
        global tokens
        global line
        Btrue = []
        Bfalse = []

        if tokens[0] == my_dict["not"]:
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["anoigma_agguli_tk"]:
                tokens = lex()
                line = tokens[2]
                R = condition()
                if tokens[0] == my_dict["kleisimo_agguli_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    Rtrue = R[0]
                    Rfalse = R[1]
                    Btrue = Rfalse
                    Bfalse = Rtrue

                else:
                    print("Error,there is not ] after not[ at boolfactor in line",line)
                    exit(-1)
            else:
                print("Error,there is not [ after not at boolfactor in line",line)
                exit(-1)
        elif tokens[0] == my_dict["anoigma_agguli_tk"]:
            tokens = lex()
            line = tokens[2]
            R = condition()
            if tokens[0] == my_dict["kleisimo_agguli_tk"]:
                tokens = lex()
                line = tokens[2]
                Rtrue = R[0]
                Rfalse = R[1]
                Btrue = Rtrue
                Bfalse = Rfalse


            else:
                print("Error,there is not ] after [ at boolfactor in line",line)
                exit(-1)
        else:
            E1place = expression()
            rel_operator = REL_OP()
            E2place = expression()
            Rtrue = makeList(nextQuad())
            genQuad(rel_operator, E1place, E2place,"_")
            Rfalse = makeList(nextQuad())
            genQuad("jump","_","_","_")
            Btrue = Rtrue
            Bfalse = Rfalse
        return Btrue,Bfalse

    def REL_OP():
        global tokens
        global line
        rel_operator = tokens[1]

        if tokens[0] == my_dict["ison_tk"]:
            tokens = lex()
            line = tokens[2]
        elif tokens[0] == my_dict["diaforo_tk"]:
            tokens = lex()
            line = tokens[2]
        elif tokens[0] == my_dict["smaller_tk"]:
            tokens = lex()
            line = tokens[2]
        elif tokens[0] == my_dict["smaller or equal_tk"]:
            tokens = lex()
            line = tokens[2]
        elif tokens[0] == my_dict["bigger_tk"]:
            tokens = lex()
            line = tokens[2]
        elif tokens[0] == my_dict["bigger or equal_tk"]:
            tokens = lex()
            line = tokens[2]
        else:
            print("Error,there is not == or != or > or >= or < or <= in line", line)
            exit(-1)
        return rel_operator

    def call_main_part():
        global tokens
        global line

        if tokens[0] == my_dict["if"]:
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["__name__"]:
                tokens = lex()
                line = tokens[2]
                if tokens[0] == my_dict["ison_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    if tokens[0] == my_dict["quotes_tk"]:
                        tokens = lex()
                        line = tokens[2]
                        if tokens[0] == my_dict["__main__"]:
                            tokens = lex()
                            line = tokens[2]
                            if tokens[0] == my_dict["quotes_tk"]:
                                tokens = lex()
                                line = tokens[2]
                                genQuad('begin_block', 'main', '_', '_')
                                if tokens[0] == my_dict["anw_katw_teleia_tk"]:
                                    tokens = lex()
                                    line = tokens[2]
                                    main_function_call()
                                    while tokens[0] == my_dict["identifier_tk"]:
                                        main_function_call()
                                    genQuad('halt', '_', '_', '_')
                                    genQuad('end_block', 'main', '_', '_')
                                    show_symbols(my_file2)
                                    generate_final()
                                    delete_scope()
                                else:
                                    print("Error,there is not : after call_main_part in line", line)
                                    exit(-1)
                            else:
                                print("Error,there is not quotes at call_main_part in line", line)
                                exit(-1)
                        else:
                            print("Error,there is not __main__ at  call_main_part in line", line)
                            exit(-1)
                    else:
                        print("Error,there is not quotes at call_main_part in line",line)
                        exit(-1)
                else:
                    print("Error,there is not == at call_main_part in line",line)
                    exit(-1)
            else:
                print("Error,there is not __name__ at call_main_part in line",line)
                exit(-1)
        else:
            print("Error,there is not if at call_main_part in line",line)
            exit(-1)

    def main_function_call():
        global tokens
        global line

        if tokens[0] == my_dict["identifier_tk"]:
            ID = tokens[1]
            tokens = lex()
            line = tokens[2]
            if tokens[0] == my_dict["anoigma_parenthesi_tk"]:
                tokens = lex()
                line = tokens[2]
                if tokens[0] == my_dict["kleisimo_parenthesi_tk"]:
                    tokens = lex()
                    line = tokens[2]
                    if tokens[0] == my_dict["erwtimatiko_tk"]:
                        genQuad('call', ID, '_', '_')
                        tokens = lex()
                        line = tokens[2]
                    else:
                        print("Error,there is not ; at main_function_call in line", line)
                        exit(-1)
                else:
                    print("Error,there is not ) at  main_function_call in line", line)
                    exit(-1)
            else:
                print("Error,there is not ( at main_function_call in line", line)
                exit(-1)
        else:
            print("Error,there is not identifier at main_function_call in line", line)
            exit(-1)

    startRule()
syn()
write_Quads(my_file)
my_file.close()
my_file2.close()
final_file.close()


