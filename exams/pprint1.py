import pprint
message = "It was a bright cold day in April, and the clocks were striking fourteen."
count = {}
for character in message:
    if character not in count:
        count[character]=1
    else:
        count[character] = count[character]+1
pprint.pprint(count)