def say_hello(name):
    # takes in a name and returns the string "Hi my name is " plus the name
    # use whichever form of interpolation is most appropriate
    s = f"Hi my name is {name}"
    return s

def replace_given_substring(str_to_replace, str_to_insert, string):
    # this function takes three parameters --
    # the first is the substring we would like to replace.
    # the second substring is what we would like to use inplace of the first
    # the third is the actual string which we want to operate on
    # the function should return the new string
    return string.replace(str_to_replace, str_to_insert)

def remove_duplicate_punctuation(string):
    chars = ['.', ',', '!', '?']
    for c in chars:    
        for i in range(string.count(c)):
            for index, w in enumerate(string):
                if w == c and index +1 < len(string) and string[index+1] == c :
                    string = string.replace(c, '', 1)
    return string


def validate_email_format(email):
    unwanted = ['*','~','#','$','%','&','(',')', "'",'`','"',"'",':',';','/','>','<']
    for c in unwanted:
        if c in email:
            return False
    if '@' in email and email.count('@') == 1:
        if email.endswith('.com'):
            return True
        else:
            return False
    else:
        return False


def anonymize_credit_card_number(credit_card_number):
    # should replace all characters except the last 4 with 'X'
    # return the anonymized credit card number as a string
    # the credit card may have characters that are not numbers (i.e. spaces and dashes, which we would want to keep)
    # i.e. 1234-5678-90-1234 -> XXXX-XXXX-XX-1234
    end = credit_card_number[-4:]
    new_cc =''
    for x in range(len(credit_card_number)-4):
        if credit_card_number[x].isdigit():
            new_cc += 'X'
        elif '-' == credit_card_number[x]:
            new_cc += '-'
        elif ' ' == credit_card_number[x]:
            new_cc += ' '
        else:
            return None
    return new_cc+end