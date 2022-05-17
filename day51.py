def solution(roman):
    roman_numerals = {'I' : 1, 'IV' : 4, 'V' : 5, 'IX' : 9, 'X' : 10, 'XL': 40, 'L' : 50, 'XC': 90, 'C': 100, 'CD' : 400, 'D' : 500, 'CM' : 900, 'M' : 1000}
    i = 0
    total = 0

    if roman in roman_numerals:
        return roman_numerals[roman]
    
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in roman_numerals:
            total += roman_numerals[roman[i:i+2]]
            i += 2
        else:
            total += roman_numerals[roman[i]]
            
            i += 1 
        
    return total