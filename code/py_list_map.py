# get cc recipients list

EMAIL_CC = 'intlpowerministries@gmail.com,pramod.jingade@gmail.com'

def get_cc_list() -> list:
    list_string = EMAIL_CC or ''    
    list = list_string.split(',')
    result = map(lambda item: {"email": item}, list)
    print(f"result is: {result}")
    return result

print(str(get_cc_list()))
