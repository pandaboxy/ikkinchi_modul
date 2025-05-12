"2"
import time
start_time = time.time()  # boshlanadi vaqti time funksiyasi import time dan olindi

def chain_checks(*conditions): #<- bu yerda shartlar beriladi "*conditions" 
    def decorator(func): #<- bu yerda funksiya beriladi
        def wrapper(): #<- bu yerda funksiya run qilinadi
            for cond in conditions: #<- bu yerda shartlar beriladi
                if not cond: #<- agar shart bajarilmasa
                    print(f'Vaqt: {time.time() - start_time:.4f} sekund')
                    return
            func() #<- agar shart bajarilsa funksiya chaqiriladi a u bosa qaytadan boshlidi
            print(f'Vaqt: {time.time() - start_time:.4f} sekund') # <- bu yerda vaqtni milisecundalari masalan 3.1234
        return wrapper #<- bu yerda wrapper funksiya call qilinadi
    return decorator #<- bu yerda decorator funksiya call qilinadi

@chain_checks( #<- bu dekorator  
    1 + 2 == 3, 
    2 + 3 == 5,
    3 + 4 == 7,
    4 + 5 == 9,  # *shartla*
    5 + 6 == 11,
    6 + 7 == 13,
    7 + 8 == 15,
    8 + 9 == 17,
    9 + 10 == 19
)

def programa():
    print("boldi")   #run qismi

programa()