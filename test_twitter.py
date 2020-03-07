from twitter import get_tweets
def test_get_tweets():
    assert get_tweets('blakelively','blakelively')
    assert get_tweets('EXO','EXO')
    assert get_tweets('sehun','sehun')
    assert get_tweets('baekhyun','baekhyun')
    assert get_tweets('evanlin','evanlin')
    assert get_tweets('chanyeol','chanyeol')
