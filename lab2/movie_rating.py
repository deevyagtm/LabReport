data = input("Enter movies and ratings in format movie-rating: ")

# Replace spaces with commas so everything becomes comma-separated
data = data.replace(" ", ",")

# Split into parts
pairs = data.split(",")

movies = []
ratings = []

for p in pairs:
    if p != "" and "-" in p:
        parts = p.split("-", 1)
        name = parts[0]       # movie name
        rate = parts[1]       # rating as string
        movies.append(name)
        ratings.append(int(rate))

# Calculate average
avg = sum(ratings) / len(ratings)

# Highest rated movie
max_rating = max(ratings)
max_index = ratings.index(max_rating)
highest_movie = movies[max_index]

# Above and below average lists
above = []
below = []

for i in range(len(movies)):
    if ratings[i] > avg:
        above.append(movies[i])
    elif ratings[i] < avg:
        below.append(movies[i])

# Output
print("\nAverage rating:", avg)
print("Highest rated movie:", highest_movie)
print("Movies above average:", above)
print("Movies below average:", below)