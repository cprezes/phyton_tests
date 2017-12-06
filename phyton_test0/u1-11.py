print( "charlotte hippopotamus turner".title())
full_name = "charlotte hippopotamus turner"
print(full_name.islower())


print("One fish, two fish, fish red fish, blue fish.".count('fish'))



prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"

vowel_count = 0

# TODO: set the value of vowel_count to be the number of vowels in prophecy
lower_prophecy = prophecy.lower()
vowel_count += lower_prophecy.count('a')
vowel_count += lower_prophecy.count('e')
vowel_count += lower_prophecy.count('i')
vowel_count += lower_prophecy.count('o')
vowel_count += lower_prophecy.count('u')

# Print the final count
print(vowel_count)
