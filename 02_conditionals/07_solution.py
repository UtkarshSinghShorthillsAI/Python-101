order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee_price = order_size + " Coffee with an extra shot"
else:
    coffee_price = order_size + " Coffee"


print("Order:", coffee_price)