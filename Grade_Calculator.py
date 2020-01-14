grade = int(input("What was your score: "))

if 93 <= grade <= 100:
           print ("For a score of " + str(grade) + ", your grade is a A")
      
elif 90 <= grade < 93:
           print ("For a score of " + str(grade) + ", your grade is a A-")
        
elif 87 <= grade < 90:
           print ("For a score of " + str(grade) + ", your grade is a B+")
          
elif 83 <= grade < 87:
            print ("For a score of " + str(grade) + ", your grade is a B")
            
elif 80 <= grade < 83:
            print ("For a score of " + str(grade) + ", your grade is a B-")

elif 77 <= grade < 80:
            print ("For a score of " + str(grade) + ", your grade is a C+")
            
elif 73 <= grade < 77:
            print ("For a score of " + str(grade) + ", your grade is a C")

elif 70 <= grade < 73:
            print ("For a score of " + str(grade) + ", your grade is a C-")
            
elif 67 <= grade < 70:
            print ("For a score of " + str(grade) + ", your grade is a D+")

elif 63 <= grade < 67:
            print ("For a score of " + str(grade) + ", your grade is a D")
            
elif 60 <= grade < 63:
            print ("For a score of " + str(grade) + ", your grade is a D-")
            
else:
            print ("For a score of " + str(grade) + ", your grade is a F")