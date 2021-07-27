import re

t = 'ㅋ<<>ㅋㅋ>>\"\">ㅋ*|::**컄ㅋㅋㅋ||| //// ????'
regex = r'[?|*|\\|:|/|.|<|>|"|\|]'
nm = re.sub(regex, '', t)
print(nm)
