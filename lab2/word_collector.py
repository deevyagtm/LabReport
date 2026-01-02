para = input("Enter a paragraph: ")

if para == "":
    print("Please enter correct input value")
else:
    para = para.lower()      # convert to lowercase
    words = []
    
    # break input into letters and words
    for ch in para:
        if ch != " ":
            words.append(ch)

    unique_words = []

    for w in words:
        if w not in unique_words:
            unique_words.append(w)

    unique_words.sort()

    print("Unique elements are:")
    for w in unique_words:
        print(w)

    print("Total unique elements:", len(unique_words))
