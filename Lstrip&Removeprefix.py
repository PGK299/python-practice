url = [
    "https://www.w3schools.com",
    "https://www.youtube.com",
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org"
]

#Lstrip
for i in url:
    print(i.lstrip("https://www."))
    # The wikipedia.org will missing the 'w'

print("----------------------------")

#Removeprefix
for j in url:
    print(j.removeprefix("https://www."))