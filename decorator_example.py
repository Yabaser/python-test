#This code is for practising decorators

#defining first decorator function

def apply_discount_decorator(func):
    def wrapper(base_price):
        total_price = base_price * 0.9
        return func(total_price)
    return wrapper

#Defining the second decorator function

def apply_tax_decorator(func):
    def wrapper(base_price):
        final_price = base_price * 1.18
        return func(final_price)
    return wrapper

@apply_discount_decorator
@apply_tax_decorator
def calculate_flight_price(base_price):
    print("The final price is ", base_price)


#calling the function
calculate_flight_price(10000)
