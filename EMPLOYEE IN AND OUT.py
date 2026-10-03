class EMPLOYEE:
    #INITIALIZING
    def __init__(self):
        print("EMPLOYEE CREATED ")
    #CALLING DESTRUCTOR
    def __del__(self):
        print("DESTRUCTOR CALLED ")
def create_object():
    print("MAKING OBJECT..")
    obj = EMPLOYEE()
    print("function end ..")
    return obj
print("CALLING CREATE_OBJ FUNCTION..")
obj = create_object()
print("PROGRAM END..")
