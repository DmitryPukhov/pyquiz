class BullsAndCows:
    """
    You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend
    to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many
    digits in said guess match your secret number exactly in both digit and position (called "bulls") and how
    many digits  match the secret number but locate in the wrong position (called "cows").
    Your friend will use successive guesses and hints to eventually derive the secret number.
    Write a function to return a hint according to the secret number and friend's guess, use A to indicate the
    bulls and B to indicate the cows.
    Please note that both secret number and friend's guess may contain duplicate digits.
    Example 1:
    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
    Example 2:
    Input: secret = "1123", guess = "0111"
    Output: "1A1B"
    Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
    Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths
    are always equal.
    """

    def getHint(self, secret: str, guess: str) -> str:
        maxlen = len(secret)
        # Find bulls - compare each item
        bulls = 0
        for i in range(0, maxlen):
            if secret[i] == guess[i]:
                bulls += 1
        # Find (cows + bulls) -  move 2 pointers on sorted strings
        secret, guess = sorted(secret), sorted(guess)
        i = j = cows = 0
        while i < maxlen and j < maxlen:
            if secret[i] == guess[j]:
                cows += 1
                i += 1
                j += 1
            elif secret[i] < guess[j]:
                i += 1
            elif secret[i] > guess[j]:
                j += 1
        # Exclude bulls
        cows = max(0, cows - bulls)
        return f"{bulls}A{cows}B"


secret = "1807"
guess = "7810"
print("secret={}, guess={}, output={}".format(secret, guess, BullsAndCows().getHint(secret, guess)))

secret = "1123"
guess = "0111"
print("secret={}, guess={}, output={}".format(secret, guess, BullsAndCows().getHint(secret, guess)))

secret = "9305"
guess = "1234"
print("secret={}, guess={}, output={}".format(secret, guess, BullsAndCows().getHint(secret, guess)))
