#create a hello world function
def hello_world():
    return "Hello, World!"

#call the function with from main  
if __name__ == "__main__":
    print(hello_world()) 


#list 5 last presidens in the us as a list
def last_5_presidents():
    presidents = [
        "Joe Biden",
        "Donald Trump",
        "Barack Obama",
        "George W. Bush",
        "Bill Clinton"
    ]
    return presidents

#same for denmark
def last_5_danish_prime_ministers():
    prime_ministers = [
        "Mette Frederiksen",
        "Lars Løkke Rasmussen",
        "Helle Thorning-Schmidt",
        "Lars Løkke Rasmussen",
        "Anders Fogh Rasmussen"
    ]
    return prime_ministers

#tranlate to dict and include election year
def last_5_danish_prime_ministers_dict():
    prime_ministers = {
        "Mette Frederiksen": 2019,
        "Lars Løkke Rasmussen": 2015,
        "Helle Thorning-Schmidt": 2011,
        "Lars Løkke Rasmussen": 2009,
        "Anders Fogh Rasmussen": 2001
    }
    return prime_ministers