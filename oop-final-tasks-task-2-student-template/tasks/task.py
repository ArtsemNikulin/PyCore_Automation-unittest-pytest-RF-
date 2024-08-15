class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword
        self.latin_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__cypher_alphabet = self.keyword.upper() + ''.join(
            [i for i in self.latin_alphabet if i not in self.keyword.upper()])
        self.__encode_pairs = dict(zip(self.latin_alphabet, self.__cypher_alphabet))
        self.__decode_pairs = {value: key for key, value in self.__encode_pairs.items()}

    def encode(self, text):
        result = ''.join([self.__encode_pairs[i.upper()] if i.isalpha() else i for i in text])

        return result.capitalize()

    def decode(self, text):
        result = ''.join([self.__decode_pairs[i.upper()] if i.isalpha() else i for i in text])

        return result.capitalize()


if __name__ == '__main__':
    cipher = Cipher("crypto")
    print(cipher.encode('Hello world'))
    print(cipher.decode("Btggj vjmgp"))
