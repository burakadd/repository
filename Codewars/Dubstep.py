import re


def song_decoder(song):
    return re.sub('\s+', ' ', song.replace("WUB", " ")).strip()



#    return song.replace("WUB", " ").replace("  ", " ")


pat = re.compile(r'\s+')
s = '  \t  foo   \t   bar \t  '
print(pat.sub('', s)) # prints "foobar
#
#
#
#
# Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
# Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
# Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")


print(song_decoder("WUBWUBWUBAWUBWUBWUBBWUBWUBWUBWUBWUBWUBWUBCWUB"))