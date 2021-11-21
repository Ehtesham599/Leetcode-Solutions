class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        PhoneDigitDict = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        Input = list(str(digits))
        Output = []
        if len(Input) == 0:
            Output = [] 
        else:
            Output = PhoneDigitDict[Input[0]]
            for a in range(1,len(Input)):
                EmptyList = []
                iterate = list(itertools.product(Output,PhoneDigitDict[Input[a]]))
                for i in iterate:
                    b = ""
                    for k in i:
                        b = b + str(k)
                    EmptyList.append(b)
                Output = EmptyList
        return Output