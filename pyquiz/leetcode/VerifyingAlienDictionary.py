from typing import List


class VeryfyingAlienDictionary:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words: return True
        maxlen = min([len(w) for w in words])
        # Create a map char->position in alphabet
        charmap = dict(zip(order, range(0, len(order))))
        # Store prev word ordinal
        prevordinal = [charmap[c] for c in words[0].rjust(maxlen, '0')]
        for w in words:
            # Compare ordinals of current and prev words
            ordinal = [charmap[c] for c in w.rjust(maxlen, '0')]
            if ordinal < prevordinal: return False  # Not ordered word found, go out.
            prevordinal = ordinal
        # Ok if everything is in order
        return True
