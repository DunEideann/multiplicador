from math import floor

def multiplicar(numero_1, numero_2):
    """
    We multiply depending on the entered parameters in the function,
    being integers or float needed.
    """
    bothIntCondition = type(numero_1)==int and type(numero_2)==int
    bothFloatCondition = type(numero_1)==float and type(numero_2)==float
    oneFloatCondition = ((type(numero_1)==float or type(numero_1)==int) and
                      (type(numero_2)==float or type(numero_2)==int))
    result = 0
    decimalResult = 0
    

    if bothIntCondition:
        aux = True #Variable used to know in what condition did we enter
        for i in range(numero_1):
            result += numero_2    
            
    elif bothFloatCondition:
        aux = True
        #Variables for number 1
        float_numero_1 = str(numero_1)
        numbers_1 = float_numero_1.split(".")
        decimals_1 = len(numbers_1[1])
        noDec1 = int(numbers_1[0] + numbers_1[1])
        #Variables for number 2
        float_numero_2 = str(numero_2)
        numbers_2 = float_numero_2.split(".")
        decimals_2 = len(numbers_2[1])
        noDec2 = int(numbers_2[0] + numbers_2[1])
        #print(f"El numero de decimales es :{decimals_1} y {decimals_2}")

        #Now we use an if statement to do the shorter loop and save resources
        if decimals_1>decimals_2:
            #First we calculate the result of the multiplication
            #  of the second number by the floor of the first number.
            for i in range(floor(numero_1)):
                result += numero_2 
            #print(f"Entered in decimals_1>decimals_2. Resultado: {result}, numero 1 y 2: {numero_1} y {numero_2} y floor{floor(numero_1)} y {floor(numero_2)}")

            #We considerate the zeros in the decimal value
            # of the first number after the '.' and before the fist number
            #  by adding a x10 to the second number

            #We calculate the addition decimal value
            for i in range(noDec2):
                decimalResult += int(numbers_1[1])
            #print(f"DecimalResult incompleto: {decimalResult}")
            
            #We transform decimalResult to the real value we need
            decimalResultStr = str(decimalResult)
            decimalResultLen = len(str(decimalResult))
            vecesCorrerPunto = decimals_1 + decimals_2
            puntoToRight = decimalResultLen-vecesCorrerPunto
            # print(f"Correr punto: {vecesCorrerPunto} y decimalResultStr: {decimalResultStr}{type(decimalResultStr)} y decimalResultLen: {decimalResultLen}")
            
            if puntoToRight==0:
                decimalResultStr = "0." + decimalResultStr
            elif puntoToRight>0:
                decimalResultStr = decimalResultStr[0:puntoToRight]+"."+decimalResultStr[puntoToRight:]

            while(vecesCorrerPunto > len(decimalResultStr)):
                decimalResultStr = "0" + decimalResultStr
                # print(f"while decimalResultStr {decimalResultStr}")
            
            decimalResult = float(decimalResultStr)
            # print(f"DecimalResult completo en else: {decimalResult}")
            result += decimalResult
            
        else:
            #First we calculate the result of the multiplication
            #  of the second number by the floor of the first number.
            for i in range(floor(numero_2)):
                result += numero_1
            #print(f"Entered in decimals_2>decimals_1. Resultado: {result}, numero 1 y 2: {numero_1} y {numero_2} y floor{floor(numero_1)} y {floor(numero_2)}")
            
            #We considerate the zeros in the decimal value
            # of the first number after the '.' and before the fist number
            #  by adding a x10 to the second number

            #We calculate the addition decimal value
            for i in range(noDec1):
                decimalResult += int(numbers_2[1])
            #print(f"DecimalResult incompleto: {decimalResult}")
            
            #We transform decimalResult to the real value we need
            decimalResultStr = str(decimalResult)
            decimalResultLen = len(str(decimalResult))
            vecesCorrerPunto = decimals_1 + decimals_2
            puntoToRight = decimalResultLen-vecesCorrerPunto
            # print(f"Correr punto: {vecesCorrerPunto} y decimalResultStr: {decimalResultStr}{type(decimalResultStr)} y decimalResultLen: {decimalResultLen}")
            
            if puntoToRight==0:
                decimalResultStr = "0." + decimalResultStr
            elif puntoToRight>0:
                decimalResultStr = decimalResultStr[0:puntoToRight]+"."+decimalResultStr[puntoToRight:]

            while(vecesCorrerPunto > len(decimalResultStr)):
                decimalResultStr = "0" + decimalResultStr
                # print(f"while decimalResultStr {decimalResultStr}")
            
            decimalResult = float(decimalResultStr)
            # print(f"DecimalResult completo en else: {decimalResult}")
            result += decimalResult


    elif oneFloatCondition:
        aux = True
        if type(numero_1)==int:
            for i in range(numero_1):
                result += numero_2 
        else:
            for i in range(numero_2):
                result += numero_1  

    else:
        print("Please write two numbers")
        numero_1 = input("First number: ")
        numero_2 = input("Second number: ")
        a = ProblemaUno(numero_1, numero_2)
        aux = False
    if aux:
        print(f"The result for numers {numero_1} and {numero_2} is : {result}")

num_1 = 28.54
num_2 = 25.558
problema1 = multiplicar(num_1, num_2)
problema1_test = num_1*num_2
print(f"Traditional result with * : {problema1_test}")