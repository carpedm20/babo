#-*- coding: utf-8 -*-
import hangul
import json

class WordPosition(object):

    def __init__(self):
        pass
    

class Babo(object):
    debug = False

    def __init__(self, file_name=None):
        if not file_name:
            file_name = 'words.json'

        with open('words.json','r') as f:
            self.words = json.loads(f.read())

        self.choseongs = []

        word_list = [list(word) for word in self.words]
        for word in word_list:
            choseong = []

            for char in word:
                choseong.append(hangul.split(char)[0])

            self.choseongs.append(choseong)

    def choseong_dict(self, choseong_to_find):
        """Dictionary for choesongs
        
        :param choseongs: a list of Choseong  ex) u'ㅂㅂ'
        """

        if type(choseong_to_find) != unicode:
            choseong_to_find = choseong_to_find.decode('utf-8')

        ans = []

        for idx, choseong in enumerate(self.choseongs):
            if choseong == list(choseong_to_find):
                ans.append(self.words[idx])

        if self.debug:
            print len(ans)
        return ans

    def search_choseong(self, char, position):
        ans = []

        for idx, choseong in enumerate(self.choseongs):
            try:
                if char == choseong[position]:
                    ans.append(self.words[idx])
            except:
                continue

        return ans

    def positions_at(self, positions = []):
        pass
