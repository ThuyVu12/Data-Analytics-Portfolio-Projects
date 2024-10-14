import csv

def program(filename):
    book_data = {}
    book_titles = set()
    # reading csv file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            name = row[0].strip()
            book = row[1].strip()
            rating = int(row[2].strip())
            book_titles.add(book)
            if name not in book_data:
                book_data[name] = {}
            book_data[name][book] = rating

    # Create list of book titles
    book_titles_list = list(book_titles)

    # Create dictionary with  names and ratings
    name_rating = {}
    for name, rating in book_data.items():
        name_rating[name] = [rating.get(book, 0) for book in book_titles_list]

    # print("List of book titles:", book_titles_list)

    for rating in name_rating.values():
        while len(rating) < len(book_titles_list):
            rating.append(0)

    #testing name_rating       
    # print("testing name_rating", name_rating)

    book_average = {}
    rating_values = list(name_rating.values())
    # testing rating values
    # print("rating values", rating_values)

    # calculating the averages for each book
    average_list = []
    for j in range(len(rating_values[0])):
        total = 0
        count = 0
        for i in range(0, len(rating_values)):
            if rating_values[i][j] != 0:
                total += rating_values[i][j]
                count += 1
        average_rating = float(total / count) if count > 0 else 0
        average_list.append(average_rating)

    # testing average_list
    # print("testing average_list", average_list)

    book_average = {book_titles_list[i]: average_list[i] for i in range(len(book_titles_list))}

    sorted_tuples_for_average = sorted(book_average.items(), key=lambda item: item[1], reverse=True)
    sorted_book_average = {k: v for k, v in sorted_tuples_for_average}

    # testing sorted book average
    # print("testing sorted book average", sorted_book_average)
    lines = [f'{key} {value}' for key, value in sorted_book_average.items()]


    print("Welcome to the CS 124 Book Recommender. Type the word in the/n left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("averages  : output the average ratings of all books in the system")
    print("quit      : exit the program")
    user_input = input("next task? " )
    while user_input != "quit":
        if user_input == "averages":
            print('\n'.join(lines))
        elif user_input == "recommend":
            name_of_user = input("user? ")
            if name_of_user not in name_rating.keys():
                print('\n'.join(lines))
            else:
                #calculating and loop through similarity_list to make recommendations
                similarity_list = []
                user_ratings = name_rating[name_of_user]
                for name, ratings in name_rating.items():
                    if name != name_of_user:
                        similarity = sum(u * v for u, v in zip(user_ratings, ratings))
                        similarity_list.append((similarity, name))
                similarity_list.sort(reverse=True)
                # print(similarity_list)

                recommendation = [0] * len(book_titles_list)
                total_ratings = [0] * len(book_titles_list)
                    
                for sim, name in similarity_list[:3]:
                    ratings = name_rating[name]
                    for i, rating in enumerate(ratings):
                        if rating != 0:
                            recommendation[i] += rating
                            total_ratings[i] += 1

                avg_ratings = [(rec / total) if total != 0 else 0 for rec, total in zip(recommendation, total_ratings)]
                avg_books = [(avg_ratings[i], book_titles_list[i]) for i in range(len(book_titles_list)) if total_ratings[i] != 0]
                avg_books.sort(reverse=True)
                #testing avg books
                # print(avg_books)
                for j in range(-1, 0):
                    for i in range(len(avg_books)):
                        print(avg_books[i][j], avg_books[i][0])        
        user_input = input("next task? ")

def main():
    program("/Users/thuyvu/Desktop/Edmonds/Data Analytics Certificate/Github/Recommender's System/ratings.csv")

main()

