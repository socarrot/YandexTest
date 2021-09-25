import sys
from input import Input
from validation import ValidationError
from gender import Gender
from income_source import IncomeSource
from purpose import Purpose

try:
    request = Input(
        int(input("enter age: ")),
        Gender[input("enter gender F or M: ")],
        IncomeSource[input("enter gender PASSIVE, HIRED, OWNER or UNEMPLOYED: ")],
        int(input("enter year income: ")),
        int(input("enter credit score -2..2: ")),
        int(input("enter requested amount: ")),
        int(input("enter maturity: ")),
        Purpose[input("enter purpose MORTGAGE, BUSINESS, CAR or CONSUMER: ")])
    request.validation()
    requested_amount = request.annual_payment()
    print('requested amount', requested_amount)
except ValidationError as err:
    print('validation', err)
    sys.exit(0)
except Exception as err:
    print(err)
    sys.exit(1)