class GroupAnagrams:
    """
    10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
    each other
    """

    def group_anagrams(self, arr: []):
        """
        Idea: we need not sort the whole array.
        1. Create hash table anagram -> (original, original count, anagram count)
        We need counts because original-anagram counts may not be 1:1
        2. Go through array and fill hash table.
        3. Go through hash table and build array with anagrams next to each other
        :param arr: array of strings
        :return: array with grouped anagrams
        """
        # Build hash table
        ht = self._build_hash_table(arr)

        # Resulted array with grouped anagrams
        return self._build_grouped_arr(ht)

    @staticmethod
    def _build_grouped_arr(ht):
        """
        Create resulted array from hash table anagram -> (original, original_count, anagram_count)
        """
        grouped_arr = []
        for anagram in ht.keys():
            (original, orig_cnt, anag_cnt) = ht[anagram]

            # Add original-anagram pairs
            for i in range(0, anag_cnt):
                grouped_arr.append(original)
                grouped_arr.append(anagram)

            # Add singles
            for i in range(0, orig_cnt - anag_cnt):
                grouped_arr.append(original)

        return grouped_arr

    @staticmethod
    def _build_hash_table(arr: [str]):
        """
        Go through array and build hash table anagram -> original, original counts, anagram count
        For single element 12 without anagram in array it will be 21 -> (12, 1, 0)
        """
        ht = {}
        for cur_str in arr:

            anagram = cur_str[::-1]
            if cur_str in ht.keys():
                # This string is an anagram of some previous
                # Increase anagram count for hash table item
                (original, orig_cnt, anag_cnt) = ht[cur_str]
                ht[cur_str] = (original, orig_cnt, anag_cnt + 1)
            elif anagram in ht.keys():
                # This string equals to some prevoius
                # Increase original count for hash table item
                (original, orig_cnt, anag_cnt) = ht[anagram]
                ht[anagram] = (original, orig_cnt+1, anag_cnt)
            else:
                # This string is new
                ht[anagram] = (cur_str, 1, 0)
        return ht
