# import string
#
#
# class Alphabet:
#     def __init__(self, lang, letters_str):
#         self.lang = lang
#         self.letters = letters_str
#
#     def print(self):
#         print(self.letters)
#
#     def letters_num(self):
#         len(self.letters)
#
#
# class EngAlphabet(Alphabet):
#     def __init__(self):
#         super().__init__('En', string.ascii_uppercase)
#
#     __letters_num = 26
#
#     def is_en_letter(self, letter):
#         if letter.upper() in self.letters:
#             return True
#         return False
#
#     def letters_num(self):
#         return EngAlphabet.__letters_num
#
#     @staticmethod
#     def example():
#         print("English Exampel:")
#
#
# if __name__ == '__main__':
#     en = EngAlphabet()
#     en.print()
#     print(en.letters_num())
#     print(en.is_en_letter('F'))
#     print(en.is_en_letter('Щ'))
#     en.example()
class Test:
    __test = 0
tt = Test
print(tt._Test__test)