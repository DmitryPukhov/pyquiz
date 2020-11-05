from unittest import TestCase

from pyquiz.leetcode.WordLadder import WordLadder


class TestSolution(TestCase):
    def test_ladder_length__hit_cog__hot_dot_dog_lot_log_cog(self):
        """
        Example 1:

        Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

        Output: 5

        Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
        return its length 5.
        """
        beginWord:str = "hit"
        endWord:str = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        output = 5

        res = WordLadder().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(output, res)

    def test_ladder_length__hit_cog__hot_dot_dog_lot_log(self):
        """
        Example 2:

        Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]

        Output: 0
        Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
        """

        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        output = 0

        res = WordLadder().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(output, res)

    def test_ladder_length__a_b__ab(self):
        beginWord = "a"
        endWord = "b"
        wordList = ["b", "d", "e", "f"]
        output = 2
        res = WordLadder().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(output, res)

    def test_ladder_length__ab_bc__ab_bc_ac(self):
        beginWord = "ab"
        endWord = "bc"
        wordList = ["ab", "bc", "ac"]
        output = 3
        res = WordLadder().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(output, res)

    def test_ladder_length__hita_cogb__hota_dota_lota_loga_cogb(self):
        beginWord = "hita"
        endWord = "cogb"
        wordList = ["hota","dota","doga","lota","loga","coga","cogb"]
        # hita-hota-lota-loga-coga-cogb
        output = 6
        res = WordLadder().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(output, res)

    def test_ladder_length__ab_cd__cd(self):
        beginWord = "ab"
        endWord = "cd"
        wordList = ["cd"]
        output = 0
        res = WordLadder().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(output, res)

    def test_ladder_length__cet_ism(self):
        beginWord = "cet"
        endWord = "ism"
        wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
        output = 11
        res = WordLadder().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(output, res)

