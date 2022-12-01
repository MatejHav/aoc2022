(lambda x: print(x[0], sum(x[:3])))(sorted(map(lambda x: sum(map(int, x.split('\n'))), open('01.txt').read().split('\n\n')), reverse=True))
