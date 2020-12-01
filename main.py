"""This program will use your Zodiac sign and another person's zodiac sign to
tell you several different things about you and the other person, like your
compatibility, your zodiac elements, your lucky numbers, etc.
Received help from Anthony Horvath and my professor Scott Vanselow.
This line asks for user input of someone else's Zodiac sign."""

__author__ = "Juliana Horvath"

import random


def main():
    """All of the code below runs the program described above. It will take your
    Zodiac sign and another person's Zodiac sign and tell you different things
    about both of you."""
    your_zodiac = 0
    your_comp = 0

    not_match = True
    while not_match:
        your_zodiac = input("Enter your Zodiac(all lowercase): ")
        # The following lines assign a number to each of the signs in order to
        # find the percentage of compatibility in the end.
        if your_zodiac == "aquarius":
            your_comp = 87
            not_match = False
        elif your_zodiac == "pisces":
            your_comp = 64
            not_match = False
        elif your_zodiac == "aries":
            your_comp = 93
            not_match = False
        elif your_zodiac == "taurus":
            your_comp = 56
            not_match = False
        elif your_zodiac == "gemini":
            your_comp = 98
            not_match = False
        elif your_zodiac == "cancer":
            your_comp = 82
            not_match = False
        elif your_zodiac == "leo":
            your_comp = 48
            not_match = False
        elif your_zodiac == "virgo":
            your_comp = 67
            not_match = False
        elif your_zodiac == "libra":
            your_comp = 86
            not_match = False
        elif your_zodiac == "scorpio":
            your_comp = 91
            not_match = False
        elif your_zodiac == "sagittarius":
            your_comp = 41
            not_match = False
        elif your_zodiac == "capricorn":
            your_comp = 75
            not_match = False
        else:
            print("Invalid Zodiac sign. Please type a valid zodiac sign.")

    their_zodiac = 0
    their_comp = 0

    not_match = True
    while not_match:
        their_zodiac = input("Enter their Zodiac(all lowercase): ")
        # The following lines assign a number to each of the signs in order to
        # find the percentage of compatibility in the end.
        if their_zodiac == "aquarius":
            their_comp = 87
            not_match = False
        elif their_zodiac == "pisces":
            their_comp = 64
            not_match = False
        elif their_zodiac == "aries":
            their_comp = 93
            not_match = False
        elif their_zodiac == "taurus":
            their_comp = 56
            not_match = False
        elif their_zodiac == "gemini":
            their_comp = 98
            not_match = False
        elif their_zodiac == "cancer":
            their_comp = 82
            not_match = False
        elif their_zodiac == "leo":
            their_comp = 48
            not_match = False
        elif their_zodiac == "virgo":
            their_comp = 67
            not_match = False
        elif their_zodiac == "libra":
            their_comp = 86
            not_match = False
        elif their_zodiac == "scorpio":
            their_comp = 91
            not_match = False
        elif their_zodiac == "sagittarius":
            their_comp = 41
            not_match = False
        elif their_zodiac == "capricorn":
            their_comp = 75
            not_match = False
        else:
            print("Invalid Zodiac sign. Please type a valid zodiac sign.")

    # The following code defines each of the variables that are going to be
    # calculated using certain equations.
    emo_comp = ((your_comp + their_comp) / 2) - 5
    # emo_comp is the emotional compatibility and this will tell you how easy
    # it is for you talk to this person and have a deep, meaningful relationship
    # with them.
    social_comp = ((your_comp * their_comp) ** 0.5) // 2
    # social_comp is the social compatibility and this will tell you how
    # comfortable you are around this person in a social environment and
    # in social situations.
    phy_comp = (your_comp % their_comp) * 1.2
    # phy_comp is the physical compatibility and this will tell you how close and
    # attracted you are physically to this person.
    emo_comp *= 1.05
    social_comp *= 1.15
    phy_comp *= 1.10
    # The following lines of code do the computations, based on the signs you
    # chose, in order to find the different compatibilities.
    # I used the "if- elif- else" statements in order to keep the numbers in the
    # 0.0% - 100.0% range because some numbers were coming out greater than
    # 100.0% and some less than 0.0%.
    if emo_comp > 100:
        print("Emotional " + "Compatibility: ", 100.0, '%')
    elif emo_comp < 0:
        print("Emotional " + "Compatibility: ", 0.0, '%')
    else:  # emo_comp >= 0 and emo_comp <= 100:
        print("Emotional " + "Compatibility: ", format(emo_comp, '.1f'), '%')
    if social_comp > 100:
        print("Social " + "Compatibility: ", 100.0, '%')
    elif social_comp < 0:
        print("Social " + "Compatibility: ", 0.0, '%')
    else:  # social_comp >= 0 and social_comp <= 100:
        print("Social " + "Compatibility: ", format(social_comp, '.1f'), '%')
    if phy_comp > 100:
        print("Physical " + "Compatibility: ", 100.0, '%')
    elif phy_comp < 0:
        print("Physical " + "Compatibility: ", 0.0, '%')
    else:  # phy_comp >= 0 and phy_comp <= 100:
        print("Physical " + "Compatibility: ", format(phy_comp, '.1f'), '%')
    # The following lines of code take the percent calculated from the previous
    # lines of code and based on that value, your given a message regarding the
    # compatibility.
    if emo_comp >= 65:
        print("Love!" * 3)
    else:
        print("No love.")
    if social_comp >= 30:
        print("Friends!" * 3)
    else:
        print("Enemies.")
    if phy_comp >= 45:
        print("Kiss!" * 3)
    else:
        print("No kiss.")

    if emo_comp != range(65, 100) or social_comp != range(30, 100) or phy_comp != range(45, 100):
        print("You do not have good compatibility with this person in at least one of the compatibility categories.")
    print("Your " + get_your_element(your_zodiac))
    print("Their " + get_their_element(their_zodiac))
    # This portion of code compares your element to the other person's element
    # and will tell you whether your element matches the other person's element.
    if get_your_element(your_zodiac) == get_their_element(their_zodiac):
        print("Your element does match the other person's element!")
    if not (get_your_element(your_zodiac) == get_their_element(their_zodiac)):
        print("Your element does not match the other person's element.")

    # This portion of code will take your zodiac sign and calculate the amount of
    # true friends you should have in life.
    num_friends = 0
    number = your_comp
    num_friends += number * 0.1
    print("The amount of true friends you'll have is", int(num_friends), '.')

    # This portion of code will tell you what your lucky numbers are.
    print("Your lucky numbers are:")
    y = 0
    for x in range(6):
        if emo_comp <= 60 or social_comp <= 60 or phy_comp <= 60:
            print(random.randint(1, 30), end=" ")
        else:
            print(random.randint(30, 60), end=" ")
        y += 1


def get_your_element(your_zodiac):
    """This portion of code will take your zodiac sign and tell you what your
    element is."""
    if your_zodiac == "cancer" or your_zodiac == "scorpio" or your_zodiac == "pisces":
        return "zodiac element is water."
    elif your_zodiac == "virgo" or your_zodiac == "taurus" or your_zodiac == "capricorn":
        return "zodiac element is earth."
    elif your_zodiac == "leo" or your_zodiac == "aries" or your_zodiac == "sagittarius":
        return "zodiac element is fire."
    elif your_zodiac == "gemini" or your_zodiac == "libra" or your_zodiac == "aquarius":
        return "zodiac element is air."
    else:
        return "zodiac sign is invalid. Please type a valid zodiac sign."


def get_their_element(their_zodiac):
    """This portion of code will take the other person's zodiac sign and tell you
    what their element is."""
    if their_zodiac == "cancer" or their_zodiac == "scorpio" or their_zodiac == "pisces":
        return "zodiac element is water."
    elif their_zodiac == "virgo" or their_zodiac == "taurus" or their_zodiac == "capricorn":
        return "zodiac element is earth."
    elif their_zodiac == "leo" or their_zodiac == "aries" or their_zodiac == "sagittarius":
        return "zodiac element is fire."
    elif their_zodiac == "gemini" or their_zodiac == "libra" or their_zodiac == "aquarius":
        return "zodiac element is air."
    else:
        return "zodiac sign is invalid. Please type a valid zodiac sign."


main()
