"""Asks the user for their credit score, annual income, and years in current job, then determines if they are eligible for a loan."""
def main():
    credit_score = int(input("Enter your credit score: "))
    annual_income = float(input("Enter your annual income($): "))
    years_in_current_job = int(input("Enter years at current job: "))

    """Assigns the values to the loan_approval function to determine if the user is eligible for a loan."""
    loan_approval(credit_score, annual_income, years_in_current_job)

"""Defines the loan_approval function that takes in the user's credit score, annual income, and years in
   current job as parameters and determines if they are eligible for a loan based on the criteria provided."""
def loan_approval(credit_score, annual_income, years_in_current_job):
    if credit_score >= 700 and annual_income >= 30000 and years_in_current_job >= 2:
        print("Loan Approved")
    else:
        print("Loan Denied")

main()

