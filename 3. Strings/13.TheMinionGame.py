# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

def minion_game(string):
    # your code goes here
    Stuart = 0
    Kevin = 0
    String_length = len(string)
    
    for i in range (String_length):
        if string[i] in 'AEIOU' :
            Kevin += String_length - i
        else:
            Stuart+= String_length - i
    
    if Stuart > Kevin:
        print(f"Stuart {Stuart}")
    elif Kevin > Stuart:
        print(f"Kevin {Kevin}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)