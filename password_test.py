def test_pwd(p):
    passtest = 0
    numtest = False
    if len(p) >= 7:
        passtest += 1
    if p.replace(" ", "a") == p:
        passtest += 1
    if p.replace("\t", "a") == p:
        passtest += 1
    if p.lower() != p:
        passtest += 1
    if p.upper() != p:
        passtest += 1
    for i in range(10):
        if str(i) in p:
            numtest = True
    if numtest == True:
        passtest += 1

    if passtest == 6:
        trueFalse = True
    else:
        trueFalse = False
    return trueFalse
    #ADD YOUR CODE HERE (see description in exam)


def main():
    valid = True
    score = 0
    tries = 0
    print("""Pasword must have:
        - at least 7 characters
        - no spaces or tabs
        - at least 1 upper-case letter
        - at least 1 lower-case letter
        - at least 1 digit
        - at least 1 special character (not letter, digit, space, or tab)
        """)
    while valid:
        password = input("Enter password: ")
        test = test_pwd(password)
        if test == True:
            print("Password OK.")
            score += 1
        else:
            print("Sorry, that is not a valid password.")
        tries += 1
        yon = True
        while yon:
            another = input("Want to try another password? (y or n): ")
            if another == "n":
                yon = False
                valid = False
                print(f'Your score: {score} valid passwords in {tries} attempts.')
            elif another == "y":      #   elif ord(another) == ord("y"):
                yon = False
            else:
                print("Please enter y or n.")

    #ADD YOUR CODE HERE (see description in exam)

main()