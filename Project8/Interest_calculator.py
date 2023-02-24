def interest_calculator():
    # first collect data from user
    print("This is your monthly interest calculator")
    print('')

    principle = float(input("Input loan amount: "))
    rate = float(input("Input the annual interest rate: "))
    years = int(input("Enter number of years: "))


    monthly_interest_rate = rate / 1200
    amount_of_months = years * 12
    monthly_payment = principle * monthly_interest_rate / ( 1- (1 + monthly_interest_rate)**(-amount_of_months))

    print('Your monthly payment for this loan is: %.2f' % monthly_payment)



if __name__ == '__main__':
    interest_calculator()