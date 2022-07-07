def romanToDecimal():
    try:
        roman = ['I','V','X','L','C','D','M']
        decimal = [1,5,10,50,100,500,1000]

        x = input("\nEnter a roman numeral: ").upper()

        result = []
        result.append(decimal[roman.index(x[0])])
        itr = 0

        for i in x[1:]:
            
            if result[itr] < decimal[roman.index(i)]:
                result.append(decimal[roman.index(i)] - result[-1])
                result.remove(result[-2])
                
            else: 
                result.append(decimal[roman.index(i)])
                itr += 1

        print(f'\nDecimal equivalent: {sum(result)}')

    except ValueError:
        print('Invalid Input!')

romanToDecimal()