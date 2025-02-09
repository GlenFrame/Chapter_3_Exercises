def get_and_print_info():
    name = input("Enter your name: ").strip() # write me a function or set of functions that can take a name and an age and print it with a message saying your name is x and age is x
    try:
        age = int(input("Enter your age: ").strip())
        print(f"Your name is {name} and your age is {age}.")
    except ValueError:
        print("Invalid input for age. Please enter a valid number.")
 # the professors AI question was better because the ad-lib idea is super cool. Mine could be improved because it is too complicated for what it actually does

get_and_print_info()
def print_right(string):
    print((40 - len(string)) * " " + string)
print_right("very")
print_right("awesome")
print_right("bit of code") # my version is better because it is easier to read and simpler, but it is very possible that it also has shortcomings due to this.
# never mind the professor just pulled a flex and did four different methods of it. Mine is worse because I didn't do four different methods, and some of the professors were even cleaner looking.
# mine could be improved because it would be useful to learn multiple ways to do things, so I never get stuck.
def triangle(string, n):
    for i in range(n):
        print(string * i + string) # honestly I see no difference between our solutions. Both work. I think once again though it would be useful for me to learn multiple ways to do things so mine could be improved in that way.
triangle("I", 10)
def rectangle(string, w, h):
    for i in range(h):
        print((string * w)) # I think the professor won this one automatically because didn't exactly understand what I was doing at the time and kind of just kept messing around until it was actually a rectangle. Overall looks pretty clean and tidy though.
rectangle("I", 5, 5)
def first_verse(n):
    print(n, "bottles of beer on the wall")
def second_verse(n):
    print(n, "bottles of beer")
def third_verse():
    print("Take one down, pass it around")
def fourth_verse(n):
    print(n-1, "bottles of beer on the wall")
def bottle_verse(n):
    first_verse(n)
    second_verse(n)
    third_verse()
    fourth_verse(n)
n = 40
for n in range(n, n-n, n-n-1): # the professor cheated with his years of superiority and made an absolutely beautiful rendition of bottles of beer all contained within a single function (plus the one to repeat it, but we don't talk about that)
    bottle_verse(n) # I am amazed by how neat it is and I feel very flexed on. I definitely need some improvements to mine. But at least it works!
    print()
