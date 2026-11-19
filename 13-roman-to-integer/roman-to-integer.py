class Solution:
    def romanToInt(self, s: str) -> int:
        # Hash method 
        # Creating hash(dictionary) of roman letters with its value(key:value) 
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        #Initialize variable
        result = 0
        for i in range(len(s)): #Looping trhough each character of string 
            # adding the values of roman letters by comparing the hash map (dictionary of roman letters) and returning the the result
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]
        return result