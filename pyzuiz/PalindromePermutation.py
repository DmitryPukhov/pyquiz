class PalindromePermutation:
    """
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
    drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    EXAMPLE
    Input: Tact Coa
    Output: True (permutations: "taco cat", "atco eta", etc.)
    Hints: #106, #121, #134, #136
    """

    @staticmethod
    def is_permutation(input_string):
        # Count each char in given string
        hash_table = {}
        for c in input_string:
            hash_table.setdefault(c, 0)
            hash_table[c] = hash_table[c] + 1

        # Check all counters should be even and only one could be odd
        even_count = 0
        for c in hash_table:
            if hash_table[c] % 2 == 1:
                even_count += 1
            if even_count > 1:
                return False

        # All letters in string have duplicates and we can build a palindrome from it.
        return True
