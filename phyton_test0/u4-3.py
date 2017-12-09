egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
print(egg_count)



def word_count(document, search_term):
    """ Count how many times search_term appears in document. """
    words = document.split()    
    answer = 0
    for word in words:
        if word == search_term:
            answer += 1
    return answer

def nearest_square(limit):
    """ Find the largest square number smaller than limit. """
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2
