class lexicon(object):
    def __init__(self):
        pass
    def scan(words1):
        lex = [('direction', 'north', 'south', 'east', 'west'),
                   ('verb', 'go', 'kill', 'eat'),
                   ('stop', 'the', 'in', 'of'),
                   ('number', 1234 , 91234, 3),
                   ('noun', 'bear', 'princess')]
        words = words1.lower().split()
        pairs = []
        for word in words:
            try:
                word = int(word)
            except ValueError:
                pass
            if word in lex[0]:
                pairs.append(('direction', word))
            elif word in lex[1]:
                pairs.append(('verb', word))
            elif word in lex[2]:
                pairs.append(('stop', word))
            elif word in lex[3]:
                pairs.append(('number', word))
            elif word in lex[4]:
                pairs.append(('noun', word))
            else:
                pairs.append(('error', word))
        return (pairs)
