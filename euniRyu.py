# function exampleOne(a){
#   if(typeof a === 'number'){
#     if(a - math.floor(a) !== 0){
#         throw new Error('정수를 입력해야 합니다.');
#     }
#   }
#   else{
#     throw new Error('정수를 입력해야 합니다.');
#   }

#   return a;
# }


import math

def example_one(a):
    if isinstance(a, int): #typeof a === 'number'
        if a - math.floor(a) != 0:
            raise ValueError('정수를 입력해야 합니다.') #throw new Error()
    else:
        raise ValueError('정수를 입력해야 합니다.')
    
    return a

try:
    print(example_one(10))
except ValueError as err:
    print(str(err))
