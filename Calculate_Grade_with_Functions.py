gradeMath = int(raw_input("Enter in grade for Math: "))
gradeEnglish = int(raw_input("Enter in grade for English: "))
gradePE = int(raw_input("Enter in grade for PE: "))
gradeScience = int(raw_input("Enter in grade for Science: "))
gradeArt = int(raw_input("Enter in grade for Art: ")) 

def returnLetterGrade(numGrade):

  if 93 <= numGrade <= 100:
       LetterGrade = "A"
       return LetterGrade
       
  elif 90 <= numGrade < 93:
        LetterGrade = "A-"
        return LetterGrade
        
  elif 87 <= numGrade < 90:
        LetterGrade = "B+"      
        return LetterGrade
        
  elif 83 <= numGrade < 87:
        LetterGrade = "B"    
        return LetterGrade
        
  elif 80 <= numGrade < 83:
        LetterGrade = "B-"    
        return LetterGrade
        
  elif 77 <= numGrade < 80:
        LetterGrade = "C+"    
        return LetterGrade
        
  elif 73 <= numGrade < 77:
        LetterGrade = "C"   
        return LetterGrade
        
  elif 70 <= numGrade < 73:
        LetterGrade = "C-"     
        return LetterGrade
        
  elif 67 <= numGrade < 70:
        LetterGrade = "D+"     
        return LetterGrade
        
  elif 63 <= numGrade < 67:
        LetterGrade = "D"     
        return LetterGrade
        
  elif 60 <= numGrade < 63:
        LetterGrade = "D-"
        return LetterGrade
      
  else:
       LetterGrade = "F"
        
       return LetterGrade
    
letterMath = returnLetterGrade (gradeMath)
letterEnglish = returnLetterGrade (gradeEnglish)
letterPE = returnLetterGrade (gradePE)
letterScience = returnLetterGrade (gradeScience)
letterArt = returnLetterGrade (gradeArt) 
        
print "Your Math score is %i, you got a %s" % gradeMath, letterMath
print "Your English score is %i, you got a %s" % gradeEnglish, letterEnglish
print "Your PE score is %i, you got a %s" % gradePE, letterPE
print "Your Science score is %i, you got a %s" % gradeScience, letterScience
print "Your Art score is %i, you got a %s" % gradeArt, letterArt