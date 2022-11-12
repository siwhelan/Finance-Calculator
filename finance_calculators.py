import math

# Create a program that contains two different calculators - An investement return calc & a home repayment calc


# ==================== Divider ==================== #


# ask the user to choose which calculator they'd like to use and explain what each is for

print("Choose either 'investment' or 'bond' from the menu below to proceed:")

print("investment - to calculate the amount of interest you'll earn on your investment")

print("bond - to calculate the amount you'll have to pay on a home loan")

user_choice = str(input('Which calculator would you like to use?: '))

# make sure that any/all capitalisation variations are accepted - convert input to .lower()



# if user selects investment:

if user_choice.lower() == 'investment':


    # ask them to input -

    # the amount of money they are depositing

    amount = float(input('How much money would you like to invest? '))

    # the interest rate

    interest_rate = float(input('What is the interest rate? '))
    rate = interest_rate / 100

    # number of years they'll be investing

    num_years = float(input('How many years will you be investing for? '))

    # do they want simple or compound interest?

    interest_type = str(input('Would you like to calculate simple or compound interest? '))


    # check which interest type and calculate accordingly - use .lower() again!

    # if simple:

    if interest_type.lower() == 'simple':

        # rate = interest_rate / 100


        # A =P*(1+r*t)
        
        total_return = amount*(1 + rate * num_years)

        # print total_return

        print(round(total_return, 2))


    # elif compound:

    elif interest_type.lower() == 'compound':

        #  calculate total amount to be recieved at the end of the term

        # A = P* math.pow((1+r),t)

        total_return = amount * math.pow((1 + rate), num_years)


    # print total_return

        print(round(total_return, 2))

    else:
        print('There has been an error with your input, please try again')


# if user selects bond:

if user_choice.lower() == 'bond':


    # Ask them to input -

    # The present value of the house.

    present_value = float(input('What is the current value of the property? '))

    # The interest rate.

    monthly_interest = float(input('What is the interest rate? '))

    rate = (monthly_interest / 100) / 12

    # The number of months they plan to take to repay the bond

    num_months = float(input('How many months is the repayment plan? '))

    # Calculate how much money the user will have to repay each month

        # x = (i.P)/(1 - (1+i)^(-n))

    repayment = (rate * present_value)/(1 - (1 + monthly_interest)**(- num_months))

    # output the answer

    print(round(repayment, 2))

else:
    print('There is an error in your input, please try again')












