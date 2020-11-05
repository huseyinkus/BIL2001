sayi=int(input("Faktöriyeli alınacak sayıyı giriniz: "))
carpim=1

if sayi < 0:  
   print("Negatif sayıların faktöriyeli yoktur.")  
elif sayi == 0:  
   print("0 ! =  1")  
else:  
   for i in range(sayi):
    carpim*=i+1

print(sayi,"! = ",carpim)

