import string_functions

def main():
    testString1 = "Fourscore and seven years ago our forefathers conceived of a new nation."
    testString2 = "   Now is the time for all good people to come to the aid of their country."
    testString3 = "Ask not what your country can do for you; ask what you can do for your country."
    testString4 = "     Twinkle, twinkle, little star.   "
    testString5 = "That's one small step for a man; one giant leap for mankind.   "
    testString6 = "dog"
    testString7 = "cat"
    testString8 = "cats"
    testString9 = "fish"
    testString10 = "fishing"
    score = 0

    # 1: Test CS110_upper()
    tempScore = 0
    if string_functions.cs110_upper(testString1) == testString1.upper():
        tempScore = tempScore + 1
    if string_functions.cs110_upper(testString2) == testString2.upper():
        tempScore = tempScore + 1
    if string_functions.cs110_upper(testString4) == testString4.upper():
        tempScore = tempScore + 1
    if tempScore == 3:
        print("cs110_upper passes")
        score = score + 10

    # 2: Test CS110_lstrip()
    tempScore = 0
    if string_functions.cs110_lstrip(testString2) == testString2.lstrip():
        tempScore = tempScore + 1
    if string_functions.cs110_lstrip(testString4) == testString4.lstrip():
        tempScore = tempScore + 1
    if string_functions.cs110_lstrip(testString5) == testString5.lstrip():
        tempScore = tempScore + 1
    if tempScore == 3:
        print("cs110_lstrip passes")
        score = score + 10

    # 3: Test CS110_replace()
    tempScore = 0
    if string_functions.cs110_replace(testString5,"m","x") == testString5.replace("m","x"):
        tempScore = tempScore + 1
    if string_functions.cs110_replace(testString3,"t","q") == testString3.replace("t","q"):
        tempScore = tempScore + 1
    if string_functions.cs110_replace(testString3," ","-") == testString3.replace(" ","-"):
        tempScore = tempScore + 1
    if tempScore == 3:
        print("cs110_replace passes")
        score = score + 10

    # 4: Test CS110-in()
    tempScore = 0
    if string_functions.cs110_in(testString9, testString10) == (testString9 in testString10):
        tempScore = tempScore + 1
    if string_functions.cs110_in("Fourscore ", testString1) == ("Fourscore" in testString1):
        tempScore = tempScore + 1
    if string_functions.cs110_in("twinkel", testString4) == ("twinkel" in testString4):
        tempScore = tempScore + 1
    if tempScore == 3:
        print("cs110_in passes")
        score = score + 10
 
    # 5: Test CS110_title()
    tempScore = 0
    if string_functions.cs110_title(testString3) == "Ask Not What Your Country Can Do For You; Ask What You Can Do For Your Country.":
        tempScore = tempScore + 1
    if string_functions.cs110_title(testString4) == "     Twinkle, Twinkle, Little Star.   ":
        tempScore = tempScore + 1
    if string_functions.cs110_title(testString10) == "Fishing":
        tempScore = tempScore + 1
    if tempScore == 3:
        print("cs110_title passes")
        score = score + 10
        

    # 11: EXTRA CREDIT -- Test CS110_remove_repeats()
    if score == 50 and hasattr(string_functions, "cs110_remove_repeats"):
        tempScore = 0
        if string_functions.cs110_remove_repeats(testString2) == " Now is the time for al god people to come to the aid of their country.":
            tempScore = tempScore + 1
        if string_functions.cs110_remove_repeats(testString4) == " Twinkle, twinkle, litle star. ":
            tempScore = tempScore + 1
        if string_functions.cs110_remove_repeats(testString5) == "That's one smal step for a man; one giant leap for mankind. ":
            tempScore = tempScore + 1
        if tempScore == 3:
            print("cs110_remove_repeats passes")
            score = score + 5
        else:
            print("Sorry, CS110_remove_repeats does not pass")

    # Show total score
    print("Your score: ", score)

main()

