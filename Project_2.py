import string
from random import randint, choice, choices, sample, shuffle

def password_specs(length = 14, min_spec = 0, min_num = 0, min_upper = 0):
    spec = randint(min_spec,length - min_num - min_upper)
    num = randint(min_num,length-spec-min_upper)
    upper = randint(min_upper,length - spec - num)
    lower = length - (upper + spec+ num)
    return[spec,num,upper,lower]

def password_specs_test(length = 14, min_spec = 0, min_num = 0, min_upper = 0):
    return [1,3,3,7]

def password_gen(length = 14, spec_char = '@!&', repeat = True, min_spec = 0, min_num = 0, min_upper = 0):
    required = [min_upper, min_num, min_spec]
    if sum(required) <= length and repeat or len(spec_char) >= min_spec:
        specs = password_specs(length, min_spec, min_num, min_upper)
        if repeat:
            password = choices(string.ascii_lowercase, k=specs[3]) + choices(string.ascii_uppercase, k=specs[2]) + choices(string.digits, k=specs[1]) + choices(spec_char, k=specs[0])
        else:
            ok = True
            while ok:
                specs = password_specs(length, min_spec, min_num, min_upper)
                if(specs[0] <= len(spec_char) and specs[1] <= len(string.digits) and specs[2] <= len(string.ascii_uppercase) and specs[3] <= len(string.ascii_lowercase)):
                    ok = False
            password = sample(string.ascii_lowercase, specs[3]) + sample(string.ascii_uppercase, specs[2]) + sample(string.digits, specs[1]) + sample(spec_char, specs[0])
        shuffle(password)
        pass_w = ''
        for i in password:
            pass_w += i
        return(pass_w)
    else:
        print('Invalid specifications!')

def check_password(password, length, min_spec, min_num, min_upper):
    if len(password) == length:
        specs = []
        spec_char = '@$!&%*#?'
        for item_spec in password:
            if item_spec in spec_char:
                specs += [item_spec]
        if len(specs) >= min_spec:
            nums = []
            num = string.digits
            for item_num in password:
                if item_num in num:
                    nums += [item_num]
            if len(num) >= min_num:
                up= []
                upper = string.ascii_uppercase
                for item_upper in password:
                    if item_upper in upper:
                        up += [item_upper]
                if len(up) >= min_upper:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False



