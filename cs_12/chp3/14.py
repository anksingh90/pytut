'''
 Default Argument Function
Write a function make_payment(amount, payment_method="credit_card") that processes a payment. 
The function should print the payment amount and method.
'''
def make_payment(amount, payment_method="credit_card"):
    print ( "Money to be paid :" , amount , "by using" , payment_method)
amount="Rs 100000"
payment_method="credit_card"
make_payment(amount, payment_method="credit_card")