from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = dict()
        # Criar um dicionário:
        # 'a': [1, 1, 1,...] (quantidade de 'a' em cada palavra)
        # 'b': [1, 3, 1,...] (quantidade de 'b' em cada palavra)
        for word in enumerate(words):
            for letter in word[1]:
                if letter not in letters:
                    letters[letter] = [0] * len(words)
                letters[letter][word[0]] = word[1].count(letter)

        # Encontrar a quantidade mínima de cada letra e retornar a lista
        print(letters)
        common = []
        for letter in letters:
            if all(letters[letter]):
                common += [letter] * min(letters[letter])
        return common