from time import sleep
n=int(input(" ---> input number of waves :"))
string="*****"
space=" "
indent=[1,2,3,4,5]
while True:
    try : 
        for i in indent:
            print((space*i+string),string*(n-1))
            sleep(0.05)
        for i in indent[::-1]:
            print((space*i+string),string*(n-1))
            sleep(0.05)
    except KeyboardInterrupt(): print("exited with keyboard interruption")

# type: ignore #11/9/24
