def recursive_factorial(sayi):  
   if sayi == 1:  
       return sayi  
   else:  
       return sayi*recursive_factorial(sayi-1)
   
alinan_sayi = int(input("Faktöriyeli alınacak sayıyı giriniz : "))  
if alinan_sayi < 0:  
   print("Negatif sayıların faktöriyeli yoktur.")  
elif alinan_sayi == 0:  
   print("0 ! =  1")  
else:  
   print(alinan_sayi,"! = ",recursive_factorial(alinan_sayi))  