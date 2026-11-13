class Solution:
    """
    encode:
    input: 
    strs: list of strings, which could be a variety of lengths and empty
    
    return: an encoded single string -> so combine these strings in a way that 
    goes beyond just joining them

    Question for first time view: what does encoding mean? does that mean I shouldn't
    be able to recognize the original strings by looking at the single string?

    considerations: 
    - we must be able to "decode" the single string back into the original array
    - we need to know where to separate the single string (where original strings start and end)
    - but we need to do so in a way that cannot be mistaken for false breaks

    my first idea: use a delimiter that is uncommon like # then any character between these
    is one of the original strings
    ["neet","code","love","you"] -> neet#code#love#you
    Problem what if we had ne#t -> ne#t#code#love#you -> won't decode to original

    so what if we did like a combo deliminator like len(str)#?

    this combo delimiter tells us length of string and where they separate

    then if we always rely on the pattern length, #, word...
    we don't really care what is inside word because of the strict pattern and length given

    so for 4#4#cd -> our input string element would be 4#cd even though
    first 2 characters follow the length# pattern

    ex: 4#neet4#code4#love3#you

    if strs doesn't exist then return ""
    
    """

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # move i so it is
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result

        # 4#neet4#code4#love3#you  
