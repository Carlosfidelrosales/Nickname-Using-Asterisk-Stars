# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)
# Your program should be uploaded to github before 1:30 pm

for row in range(7):
    for col in range(30):
        if(row!=0 and row!= 6 and (col==0 )) or ((row==0 or row==6) and (col > 0 and col< 5)) or \
          ((col==6 or col == 10) and row!=0) or ((row==0 or row ==3) and (col > 6 and col < 10)) or \
          (col== 12 or (row == 6 and col > 12 )) and (col < 17) or \
          ((row == 0 or row == 6) and (col > 18 and col < 22 )) or ((col== 18 or col== 22) and (row > 0 and row < 6)):
          
            
            print("*",end=" ")
        else:
            print(end="  ")
    print( )

 #   



