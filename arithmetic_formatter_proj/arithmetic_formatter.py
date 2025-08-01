** discoverd later that I could you use split() for etting operands and operator , .rjust() for spacing , to optimize the code, but I didin t know they existed before starting the problem **
** how manually iterating over strings to find operators and operands can be replaced by built-in functions like split() for cleaner and shorter code **
** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    result =''
    if len(problems) > 5:
        result = 'Error: Too many problems.'
    else:
        operators = [] 
        for problem in problems:
            print(f'problem: {problem}')
            for c in range(len(problem)):
                print(f'char of problem: {problem[c]}\n')
                if problem[c] == ' ' and problem[c+2] == ' ':
                    operators.append(problem[c+1])
                    print(f'operator: {problem[c+1]}')
                    break
        for op in operators:
            if op not in ['+','-']:
                return "Error: Operator must be '+' or '-'."
        print(f'operators: {operators}')           
        operands = []
        for problem in problems:
            for j in range(len(problem)):
                print(f'char of problem for operands n@{j}: {problem[j]}\n')
                if problem[j] == ' ':
                    operands.append(problem[0:j:]) 
                    break           
            operands.append(problem[j+3:len(problem):])    
        print(f'operands: {operands}')
        for operand in operands:
            for char in operand:
                        if char not in ['0','1','2','3','4','5','6','7','8','9']:
                            return 'Error: Numbers must only contain digits.'  
            if len(operand)>4:
                return 'Error: Numbers cannot be more than four digits.'
        line1 = ''
        line2 = ''
        line3 = ''
        line4 = ''
        for o in range(len(operators)):
            line1 += '  '
            line2 += operators[o] + ' '
            line3 += '--'
            line4 += ''
            if len(operands[o*2])>len(operands[o*2+1]):
                line2 += ' '*(len(operands[o*2])-len(operands[o*2+1]))
                line3 += '-'*len(operands[o*2])
            elif len(operands[o*2])<len(operands[o*2+1]):
                line1 += ' '*(len(operands[o*2+1])-len(operands[o*2]))
                line3 += '-'*len(operands[o*2+1])
            else:
                line3 += '-'*len(operands[o*2])
            line1 += operands[o*2]
            line2 += operands[o*2+1]
            if operators[o] == '+':
                space_number = max(len(operands[o*2+1]),len(operands[o*2])) + 2 - len(str(int(operands[o*2])+int(operands[o*2+1])))
                line4 += space_number*' ' + str(int(operands[o*2])+int(operands[o*2+1]))
            else:
                space_number = max(len(operands[o*2+1]),len(operands[o*2])) + 2 - len(str(int(operands[o*2])-int(operands[o*2+1])))
                line4 += space_number*' ' + str(int(operands[o*2])-int(operands[o*2+1]))
            if o < len(operators)-1:
                line1 += '    '
                line2 += '    '
                line3 += '    '
                line4 += '    '
        if show_answers:
            result = line1+'\n'+line2+'\n'+line3+'\n'+line4
        else:
            result = line1+'\n'+line2+'\n'+line3
    return result

def main():
    print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))

main()

** end of main.py **

