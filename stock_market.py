# Web App to Get Stock Market Data from AlphaVantage Service
import requests

#Function that gets stock info from API
#  Returns results in list of two strings
#  DO NOT EDIT THIS FUNCTION EXCEPT TO INSERT YOUR API KEY WHERE INDICATED
def getStock(symbol):
    baseURL = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&datatype=csv"
    keyPart = "&apikey=" + "QDVGVGFN6OWMLQDR" #Add API key
    symbolPart = "&symbol=" + symbol
    stockResponse = requests.get(baseURL+keyPart+symbolPart)
    return stockResponse.text  #Return only text part of response

#Function that computes and displays results
def main():
    print("Check stock prices.")
    again = True
    while again:
        again2 = True
        symb = input("Enter stock symbol: ")
        sdata = getStock(symb)
        bingus = list(sdata.split())

        if len(bingus) == 2:
            bingus1 = bingus[0].split(",")
            bingus2 = bingus[1].split(",")
            for i in bingus1:
                if i == "symbol":
                    i_sym = bingus1.index("symbol")
                elif i == "open":
                    i_open = bingus1.index("open")
                elif i == "high":
                    i_high = bingus1.index("high")
                elif i == "low":
                    i_low = bingus1.index("low")
                elif i == "price":
                    i_price = bingus1.index("price")
                elif i == "volume":
                    i_vol = bingus1.index("volume")
                elif i == "latestDay":
                    i_latest = bingus1.index("latestDay")
                elif i == "previousClose":
                    iprevious = bingus1.index(i)
                elif i == "change":
                    i_change = bingus1.index("change")
                elif i == "changePercent":
                    i_per = bingus1.index("changePercent")
            print(f"""Stock Symbol: {symb}
Last Close: {bingus2[iprevious]}
Open: {bingus2[i_open]}
High: {bingus2[i_high]}
Low: {bingus2[i_low]}
Current: {bingus2[i_price]}
                """)
            wfile = open("stock_prices.txt", "a")
            wfile.write(f"""
Stock Symbol: {symb}
Last Close: {bingus2[iprevious]}
Open: {bingus2[i_open]}
High: {bingus2[i_high]}
Low: {bingus2[i_low]}
Current: {bingus2[i_price]}

============================ 
                """)
            wfile.close()
        else:
            print("Error! Invalid stock symbol.")

        while again2:
            tf = input("Check another stock price? (Y or N): ")
            if tf.upper() == "Y":
                again2 = False
            elif tf.upper() == "N":
                again = False
                again2 = False
            else:
                print("Error! Invalid input. Please enter Y or N.")
    # Add code that meets the program specifications (see instructions in Canvas)

#Code that starts the app
main()
