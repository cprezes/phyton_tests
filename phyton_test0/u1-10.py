house_number=10
street_name = "The Crescent"
town_name = "Belmont"
print(type(house_number))

address = str(house_number) + " " + street_name + ", " + town_name
print(address)


mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

sales = int(mon_sales)+int(thurs_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales)

print ("This week's total sales: " + str(sales))