#VARIABLES
zero  = [1,1,0,1,1,1,1]
one   = [0,0,0,1,0,0,1]
two   = [1,0,1,1,1,1,0]
three = [1,0,1,1,0,1,1]
four  = [0,1,1,1,0,0,1]
five  = [1,1,1,0,0,1,1]
six   = [1,1,1,0,1,1,1]
seven = [1,0,0,1,0,0,1]
eight = [1,1,1,1,1,1,1]
nine  = [1,1,1,1,0,1,1]
list1 = [zero,one,two,three,four,five,six,seven,eight,nine]
temp  = [0,0,0,0,0,0,0]
#FUNCTIO FOR DECIMAL INPUT
def DectoBin(num,list1):
   temp=list1[num]
   printing(temp)
#FUNCTION FOR BCD INPUT
def BintoDec(binary,list1):
   decimal = 0
   for i in binary:
      decimal = decimal*2 + int(i)
   DectoBin(decimal,list1)
#FUNCTION FOR PRINTING THE 7 SEGMENT OUTPUT 
def printing(temp):
   #Putting the character in a list   
   b=[]
   for i in range(0,7):
      if (i==0 or i==2 or i==5):
         if(temp[i] ==1):
            b.append("_")
         else:
               b.append(" ")
      else:
         if(temp[i]==1):
            b.append("|")
         else:
            b.append(" ")      
   print("\nLCD output : ")
   print(" ",b[0],sep="")
   print(b[1],b[2],b[3],sep="")
   print(b[4],b[5],b[6],sep="")
j=1 
print("BCD TO 7 SEGMENGT DISPLAY DECODER ")     
while(j==1):
   ch=int(input("\n1.Decimal input\n2.BCD input\n Enter your choice :"))
   if ch==1:
      num = int(input("Enter Decimal value :"))
      DectoBin(num,list1)
   elif ch==2:
      dec = input("Enter Binary Value :")
      BintoDec(dec,list1)
   else:
      print("Wrong input !!!")
   j=int(input("Enter '1' if you want to display another number :"))
      