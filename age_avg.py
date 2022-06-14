def compute(f):
    num = 0
    highest = 0
    lowest = 100
    average = 0
    for line in f:
        line = line.split(",")
        age = int(line[1])
        num += 1
        average += age
        if age > highest:
            highest = age
        if age < lowest:
            lowest = age
    average = average / num
    f.close()
    return{"n": num, "high": highest, "low": lowest, "avg": average}
    #ADD CODE to read the data from the file object f,
    #   count the number of people
    #   find the highest and lowest ages
    #   compute the average age
    #   return the results in a dictionary (see instructions)

def main():
    file = open("age_data.txt", "r")
    results = compute(file)
    print(f'Number of people: {results["n"]}\nHighest age: {results["high"]}\nLowest age: {results["low"]}\nAverage age: {results["avg"]}')
    wfile = open("results.txt", "w")
    wfile.write(f'Number of people: {results["n"]}\nHighest age: {results["high"]}\nLowest age: {results["low"]}\nAverage age: {results["avg"]}')
    wfile.close()
    #ADD CODE to open the data file,
    #   call compute(), save the results
    #   print the results

main()
