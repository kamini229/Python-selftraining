def exceptionhandling():
    try:
        a = 10
        b = 20
        c = 10
      #  c = 0

        d = (a + b) /c
        print(d)
    except:
        print("In the except box")
        #raise Exception("This is an Exception")
    else:
        print("Because there was no exception, else it executed")

    finally:
        print("Finally , always executed")

exceptionhandling()