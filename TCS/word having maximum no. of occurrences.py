class count_word:
    def freq_word(self, s):
        d = {}
        for i in s.split():
            if  i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        return d
    def max_word(self, dict1):
        for k,v in dict1.items():
            if v == max(dict1.values()):
                return k

if __name__ == "__main__":
    sent = input()
    obj = count_word()
    d = obj.freq_word(sent)
    word = obj.max_word(d)
    print(word)