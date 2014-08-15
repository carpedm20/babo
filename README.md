바보 (사전)
===========

> The world will have a generation of idiots.. by Albert Einstein

This is a korean dictionary which is only for specific reasons.


Documentation
-------------

To use 바보 dictionary, you need to make a `Babo` instance.

    >>> from babo import Babo
    >>> dictionary = Babo()

###1. `Choseong` Dictionary###

If you want to find words with `Choseong(초성)`, you can use:

    >>> words = dictionary.choseong_dict(u'ㅂㅂ')
    334
    >>> print words[1]
    병비
    >>> words = dictionary.choseong_dict(u'ㄱㄴㄷ')
    16
    >>> print words[0]
    겨냥도

###2. Detailed search of `Choseong`###

If you want to find words with more detail information like you want to find words which has 'ㄱ' at second position:

    >>> words = search_choseong(u'ㄱ', 0)
    >>> print words[0]


Todo
----

- 초성 사전
- x로 시작하거나 끝나는 혹은 x를 포함하는 단어 찾기


Author
------

Taehoon Kim / [@carpedm20](http://carpedm20.github.io/about)
