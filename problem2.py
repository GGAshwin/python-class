#given a multi line input check whether the multi line input is a request letter
x='''Dear abc
i humbly kjdhfk
ksjkdjfjk
Thank you'''
if x.startswith('Dear'):
    print('This is a request letter')
else:
    print('Not a request letter')