
print("This python script allows you to simulate While Loop Condition")

def count_factors(given_number):
    factor = 1
    count = 1
 
    if given_number == 0:
        print("\nIs Given Number:",given_number,"= 0","(",given_number==0,")")
        return 0
    
    # The while loop will run while the "factor" is still less than
    # the "given_number" variable.
    while factor < given_number:
        # This "if" block checks if the "given_number" can be divided by
        # the "factor" variable without leaving a remainder. The modulo
        # operator % is used to test for a remainder.
        if given_number % factor == 0:
            print("\n===> Start Counting Simulation Number",count,"<===")
            print("Current factor:",factor)
            print("Current count:",count)
            print("Given Number:",given_number)

            print("\nWHILE LOOP: factor < Given Number (if TRUE Continue Loop if FALSE Print Count)")
            print("\nIs Factor", factor, "<", given_number, "(", factor < given_number, ")")

            print("\n   IF STATEMENT:","Given Number %", "Factor == 0 (if TRUE count + 1 if FALSE do WHILE LOOP)")
            print("         If",given_number,"%",factor,"=",given_number%factor,"(",given_number%factor == 0 ,")")
            count += 1

            print("\n       count:",count-1 ,"+ 1 =",count)
            
        factor += 1
        
        print("\n   IF STATEMENT:","Given Number %", "Factor == 0 (if FALSE do WHILE LOOP)")
        print("         If",given_number,"%",factor,"=",given_number%factor,"(",given_number%factor == 0 ,")")
        print("\n           factor:",factor-1 , "+ 1 = ",factor)
            
        #print("\nBefore Loop Check If TRUE, If FALSE Print Count")
        #print("Is Factor", factor, "<", given_number, "(", factor < given_number, ")")

    
        
    return count
 
#print("\nresult:",count_factors(0))
print("\nCount result:",count_factors(10)) 
#print("result:",count_factors(10)) 
#print("result:",count_factors(24)) 
