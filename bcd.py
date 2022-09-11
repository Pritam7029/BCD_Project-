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
temp  = []

#int f1,f2,f3,f4
def getinput():
      print("\nEnter 4-digit binary input: ")
      #f1, f2, f3, f4 = int(input("\nEnter 4-digit binary input: ")).split()

      f1 =  int(input("Enter number:"))
      f2 =  int(input("Enter number:"))
      f3 =  int(input("Enter number:"))
      f4 =  int(input("Enter number:"))
  
      if(f1==0 and f2==0 and f3==0 and f4==0):
        print("zero")
        temp = zero
      elif(f1==0 and f2==0 and f3==0 and f4==1):
         print("one")
         temp=one
      elif(f1==0 and f2==0 and f3==1 and f4==0):
         print("two")
         temp=two
      elif(f1==0 and f2==0 and f3==1 and f4==1):
         print("three")
         temp = three
      elif(f1==0 and f2==1 and f3==0 and f4==0):
         print("four")
         temp=four
      elif(f1==0 and f2==1 and f3==0 and f4==1):
         print("five")
         temp=five
      elif(f1==0 and f2==1 and f3==1 and f4==0):
         print("six")
         temp=six
      elif(f1==0 and f2==1 and f3==1 and f4==1):
         print("seven")
         temp=seven
      elif(f1==1 and f2==0 and f3==0 and f4==0):
         print("eight")
         temp=eight
      elif(f1==1 and f2==0 and f3==0 and f4==1):
         print("nine")
         temp=nine
      else:
        print("type next number:")

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
         
      #print(b)
      
      print("\nLCD output : ")
      print(" ",b[0],sep="")
      print(b[1],b[2],b[3],sep="")
      print(b[4],b[5],b[6],sep="")

j=1      
while(j==1):
   getinput()
   j=int(input("Enter '1' if you want to print another number :"))




