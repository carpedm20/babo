#-*- coding: utf-8 -*-
"""
    babo.babo
    ~~~~~~~~~

    Definition of Babo dictionary class

    :copyright: (c) 2014 by Taehoon Kim.
    :license: BSD, see LICENSE for more details.
"""
import hangul
import json

class Babo(object):
    jungseongs = []
    jongseongs = []
    choseongs = []

    def __init__(self, file_name=None, debug=False):
        self.debug = debug

        if not file_name:
            file_name = 'words.json'

        with open('words.json','r') as f:
            self.words = json.loads(f.read())

        self.choseongs = []

        for mode in range(3):
            self._make_serach_table(mode)

    def get_search_table(self, mode=0):
        """
        :param mode:
            - 0: Choseong (default)
            - 1: Jungseong
            - 2: Jongseong
        """
        if mode == 1:
            return self.jungseongs
        elif mode == 2:
            return self.jongseongs
        else:
            return self.choseongs

    def _make_search_tables(self, mode=0):
        """
        :param mode:
            - 0: Choseong (default)
            - 1: Jungseong
            - 2: Jongseong
        """
        table = get_search_table(mode)

        for word in [list(word) for word in self.words]:
            items = []

            for char in word:
                items.append(hangul.split(char)[mode])

            self.table.append(items)

    def choseong(self, choseong_to_find):
        """Dictionary for choseongs
        
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

    def choseong_detail(self, jaeum, position):
        """Search words with detailed choseong info

        :param jaeum: character to search  ex) u'ㄱ'
        :param position: position of character to search
        """
        ans = []

        for idx, choseong in enumerate(self.choseongs):
            try:
                if char == choseong[position]:
                    ans.append(self.words[idx])
            except:
                continue

        if self.debug:
            print len(ans)
        return ans

    def detail_search(self, eumjul, position, mode=0):
        """
        :param mode:
            - 0: Choseong (default)
            - 1: Jungseong
            - 2: Jongseong
        """
        ans   = []
        table = self.get_search_table(mode)

        for idx, item in enumerate(table):
            try:
                if eumjul == item[position]:
                    ans.append(self.words[idx])
            except:
                continue

        if self.debug:
            print len(ans)
        return ans

    def position(self, char, positions):
        pass
