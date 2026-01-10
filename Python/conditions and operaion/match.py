# we can perform same logic or we can perform same operations by using "match". but match is used for big chunk of data to concise if else statement.
# we use "match" by using its keyword "match"


#showing the name of the day by its number:
day = int(input("Enter the number of day (1 - 7): "))

match day:
    case 1:
        print("It's sunday") # match use case along with the value of the term we want to compare
    case 2:
        print("It' Monday") # if it match with the input that user gave it will perform the operation based on that case
    case 3:
        print("It's Tuesday") 
    case 4:
        print("It's wednesday")
    case 5:
        print("It's Thursday")
    case 6:
        print("It's Friday")
    case 7:
        print("It's Saturday")
    case _:
        print("this is not a day number!") # if user input is wrong or invalid, we can define a default operation or statement like "else" in "if else" statement.




# we can take multiple case values in one case. as if multiple values can perform same task so if one of them is the input of user we can perform the task
# assigning multiple values in one case reduce redundancy of code and readability.


# using "match" to show which mob is hostile and which is friendly based on user's input
name = input("what is your mob's name? ").upper()

match name:
    case "ZOMBIE" | "SKELETON" | "CREEPER" | "SPIDER" | "HUSK" | "PHANTOM" | "WITCH" | "GHAST" | "BRUTE" | "PIGLIN" | "HOGLIN" | "DROWNS" | "BLAZE" | "MONSTER":
        print("HOSTILE MOB! STAY AWAY FROM IT")

    case "PIG" | "SHEEP" | "VILLAGER" | "COW" | "CHICKEN" | "FISH" | "PANDA" | "WOLF" :
        print("YOU CAN STAY WITH IT! IT IS FRIENDLY")

    case _:
        print("That mob is not in the list try another one!")

    # we can use multiple cases of different use cases and different operations but for one operation we can use just one case with multiple values saperated by pipe operator ( | )