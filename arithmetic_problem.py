def arithmetic_arranger(problems,val=False):
    n=len(problems)
    
    num1=[]
    num2=[]
    num3=[]
    sol=[]
    
    
    
    if n > 5:
        output=("Error: Too many problems.")
        return output

    for i in range(0,n):
        x=int
        numbers = problems[i].split()
        x =max(len(numbers[0]),len(numbers[2]))
        z=x+2
        #operator validation
      
        if numbers[1]=='/' or numbers[1]=='*':
            output="Error: Operator must be '+' or '-'."
            return output
        elif x>4:
            output="Error: Numbers cannot be more than four digits."
            return output
            #list of number 1
            
        if i==n-1:

            #first raw
            num1.append('{:>{}}'.format(numbers[0],z))
            y= x-min(len(numbers[0]),len(numbers[2]))+1
            l=' '* y
            
            #second raw
            if x == len(numbers[2]):
                num2.append('{:<} {:>}'.format(numbers[1],numbers[2]))
            else:
                num2.append('{:<}{}{:>}'.format(numbers[1],l,numbers[2]))
            
            #dash
            num3.append('{:>}'.format('-'* z))
            
            #solution
            if numbers[1]=='+':
              try:
                sol.append('{:>{}}'.format(str(int(numbers[0])+int(numbers[2])),z))
              except ValueError:
                    output="Error: Numbers must only contain digits."
                    return output
            else:
              try:
                sol.append('{:>{}}'.format(str(int(numbers[0])-int(numbers[2])),z))
              except ValueError:
                    output="Error: Numbers must only contain digits."
                    return output
        else:    
            #first raw
            num1.append('{:>{}}    '.format(numbers[0],z))
            y= x-min(len(numbers[0]),len(numbers[2]))+1
            l=' '* y
            
            #second raw
            if x == len(numbers[2]):
                num2.append('{:<} {:>}    '.format(numbers[1],numbers[2]))
            else:
                num2.append('{:<}{}{:>}    '.format(numbers[1],l,numbers[2]))
            
            #dash
            num3.append('{:>}    '.format('-'* z))
            
            #solution
            if numbers[1]=='+':
              try:
                sol.append('{:>{}}    '.format(str(int(numbers[0])+int(numbers[2])),z))
              except ValueError:
                    output="Error: Numbers must only contain digits."
                    return output
            else:
              try:
                sol.append('{:>{}}    '.format(str(int(numbers[0])-int(numbers[2])),z))
              except ValueError:
                    output="Error: Numbers must only contain digits."
                    return output
        
        
        output="" 
        out1=""
        out2=""
        dash=""
        solr=""
        
        for num in num1:
                out1 += num 
        for num in num2:
                out2 += num
        for num in num3:
                dash += num
        for s in sol:
                solr += s
        if val:    
            output= '\n'.join((out1,out2,dash,solr))
                
        else:
            output= '\n'.join((out1,out2,dash))
                            
    
                 
            
    return output



