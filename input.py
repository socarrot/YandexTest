# The following data is transmitted to the input:
from gender import Gender
from income_source import IncomeSource
from purpose import Purpose
from config import Config
from validation import ValidationError
import income_source
import purpose
import credit_score
import requested_amount


def percentage(n: int, per: int):
    return n / 100 * float(per)

# Calculate annual credit payment
def annual_payment(requested_amount: int, maturity: int, annual_payment_base_rate: int):
    # (<сумма кредита> * (1 + <срок погашения> * (<базовая ставка> + <модификаторы>))) / <срок погашения>
    return (requested_amount * (1 + maturity + percentage(maturity, annual_payment_base_rate))) / maturity


class Input:
    def __init__(self,
                 age: int,
                 gender: Gender,
                 insrc: IncomeSource,
                 year_income: int,
                 crsc: int,
                 reqam: int,
                 maturity: int,
                 purp: Purpose):
        self.age = age
        self.gender = gender
        self.income_source = insrc
        self.year_income = year_income
        self.credit_score = crsc
        self.requested_amount = reqam
        self.maturity = maturity
        self.purpose = purp

    def validation(self):
        # Validate MIN age for loan request
        if self.age < Config.AGE_MIN:
            raise ValidationError("age less than", Config.AGE_MIN)

        # Validate MAX age for loan request - for male, female
        if self.gender == Gender.M and self.age > Config.AGE_MALE_MAX:
            raise ValidationError("male age more than", Config.AGE_MALE_MAX)
        if self.gender == Gender.F and self.age > Config.AGE_FEMALE_MAX:
            raise ValidationError("female age more than", Config.AGE_FEMALE_MAX)

        # Validate income source for loan request
        if self.income_source == IncomeSource.UNEMPLOYED:
            raise ValidationError("not possible to issue a loan if", Config.FORBIDDEN_INCOME_SOURCE)

        # Validate credit score for loan request
        if self.credit_score <= Config.CREDIT_SCORE_MIN:
            raise ValidationError("loan cannot be issues, credit score is less or equal", Config.CREDIT_SCORE_MIN)
        if self.credit_score > Config.CREDIT_SCORE_MAX:
            raise ValidationError("credit score more than", Config.CREDIT_SCORE_MAX)

        # Validate requested loan amount
        if self.requested_amount < Config.REQUESTED_AMOUNT_MIN:
            raise ValidationError("requested amount less than", Config.REQUESTED_AMOUNT_MIN)
        if self.requested_amount > Config.REQUESTED_AMOUNT_MAX:
            raise ValidationError("requested amount more than", Config.REQUESTED_AMOUNT_MAX)

        # Validate maturity for loan request
        if self.maturity < Config.MATURITY_MIN:
            raise ValidationError("maturity less than", Config.MATURITY_MIN)
        if self.maturity > Config.MATURITY_MAX:
            raise ValidationError("maturity more than", Config.MATURITY_MAX)

        # Validate age at the time of loan repayment
        if self.gender == Gender.M and self.final_age() > Config.AGE_MALE_MAX:
            raise ValidationError("male age at the time of loan repayment more than", Config.AGE_MALE_MAX)
        if self.gender == Gender.F and self.final_age() > Config.AGE_FEMALE_MAX:
            raise ValidationError("female age at the time of loan repayment more than", Config.AGE_FEMALE_MAX)

        # Calculate result of dividing the requested amount by the maturity in years
        # If more than a third of the annual income -> no loan is issued
        a = self.requested_amount / self.maturity
        b = self.year_income / 3
        if a > b:
            raise ValidationError("requested amount by the maturity in years is more than a third of the annual income")

        # Validate income source for loan request
        if self.income_source == Config.FORBIDDEN_INCOME_SOURCE:
            raise ValidationError("loan cannot be issues for", Config.FORBIDDEN_INCOME_SOURCE)

        # Validate that annual payment (including interest) is more than half of the year income -> no loan is issued
        if self.annual_payment() > self.year_income / 2:
            raise ValidationError("loan cannot be issues since annual payment is more than half of the year income")

    def annual_payment(self):
        anp = annual_payment(self.min_requested_amount(), self.maturity, self.calculate_modifier())
        return anp

    def min_requested_amount(self):
        csra = credit_score.max_requested_amount(self.credit_score)
        ra = self.requested_amount
        if ra > csra:
            ra = csra

        isra = income_source.max_requested_amount(self.income_source)
        if ra > isra:
            ra = isra

        return ra

    # Calculate age at the time of loan repayment
    def final_age(self):
        return self.age + self.maturity

    # Calculate sum of modifiers for annual loan payment
    def calculate_modifier(self):
        cm = Config.ANNUAL_PAYMENT_BASE_RATE + income_source.modifier(self.income_source)
        + purpose.modifier(self.purpose) + credit_score.modifier(self.credit_score)
        + requested_amount.modifier(self.requested_amount)
        return cm
