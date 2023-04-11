def Hello(**kwargs):
    #print("Hello " + kwargs['first']+ " " + kwargs['last']+ ".")
    print("Hello",end=" ")
    for keys,value in kwargs.items():
        print(value,end=" ")

Hello(title="Mr.",first="Joran",middle="Xavier",last="Delcroix")

