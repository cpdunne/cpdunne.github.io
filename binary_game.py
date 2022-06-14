import random
# You might need to import something here

def generate_byte():
    sequence = ""
    randomnum = 0
    for i in range(8):
        randomnum = random.randint(0, 1)
        sequence += str(randomnum)
    return(sequence)
    # Add code to generate and return a random sequence of 0s and 1s.
    # Use any type of sequence: string, list, tuple, or dictionary.
    # But whatever type generate_byte() returns, main() must be able to 
    #    display it as shown in the instructions and use it to calculate
    #    the decimal answer.

def print_results(correct, attempts):
    print(f'You got {correct} correct, out of {attempts} attempts.')
    # Add code to print the number correct and number of attempts.
    # This function is void; it should not return anything

def main():
    again = True
    numcorrect = 0
    numattempts = 0
    while again:
        again2 = True
        ranbinary = generate_byte()
        print(f'Number in binary: {ranbinary}')
        answer = 0
        for i in range(len(ranbinary)):
            if ranbinary[i] == "1":
                    if i == 0:
                        answer += 128
                    elif i == 1:
                        answer += 64
                    elif i == 2:
                        answer += 32
                    elif i == 3:
                        answer += 16
                    elif i == 4:
                        answer += 8
                    elif i == 5:
                        answer += 4
                    elif i == 6:
                        answer += 2
                    elif i == 7:
                        answer += 1
    
        userinp = input("What is the equivalent in decimal? ")
        try:
            if int(userinp) == answer:
                print("Correct!")
                numcorrect += 1
            else:
                print(f'Wrong! In decimal that is: {answer}')
        except:
            print(f'Wrong! In decimal that is: {answer}')
        numattempts += 1
        
        while again2:
            againinp = input("Play again? ")
            if againinp.upper() == "Y" or againinp.upper() == "YES":
                again2 = False
            elif againinp.upper() == "N" or againinp.upper() == "NO":
                again = False
                again2 = False
                print_results(numcorrect, numattempts)
            else:
                print("Error! Please enter a valid input ('y' or 'n')")

    # Add code to get random byte, compute decimal equivalent,
    #    prompt user for decimal equivalent,
    #    tell user if correct or wrong, 
    #    ask user if wants to play again, and
    #    when user quits, print results.

main()