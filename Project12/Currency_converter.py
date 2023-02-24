def Curreny_converter():
    print("Currency Converter programe")
    #eval()--> function/method that evaluate the specified expression-->if the epxression is legal python statement , it will be excecuted
    dollars = eval(input("Enter amount in $: "))
    pak_rupe = convert_to_pak(dollars)

    print("The amount is rupees is: ", pak_rupe)


# lambda function --> are also called anonymous function
# it take any number of arguments , but can only have one expression

# Syntax --> lambda arguments: expression
# the power of lambda function show when you use them inside another funciont
# Example --> if you function that take one arguments , that arguments will be multipy with an unknown number

convert_to_pak = lambda dollars : dollars * 260.40

if __name__ == '__main__':
    Curreny_converter()