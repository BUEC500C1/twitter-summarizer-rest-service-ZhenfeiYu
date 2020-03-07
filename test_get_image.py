from get_image import *
def test_tweet2image():
    assert tweet2image('blakelively','blakelively')
    assert tweet2image('EXO','EXO')
    assert tweet2image('sehun','sehun')
    assert tweet2image('baekhyun','baekhyun')
    assert tweet2image('evanlin','evanlin')
    assert tweet2image('chanyeol','chanyeol')
