#ML Basics: Creating a house value estimator

def get_estimate_val(size_sqft, number_bedrooms):
    #Assume that all houses are worth at least $50,000 
    value = 50_000

    #Adjust estimate based on size of house
    value +=  size_sqft*100 #Assume that each sqft is worth $100

    #Adjust estimate based on number of bedrooms
    value += number_bedrooms*10_000 #Assume that each bedroom is worth $10,000
    
    return value

value = get_estimate_val(3800, 3)

print("The estimated value of the house is: " + str(value) + " dollars")