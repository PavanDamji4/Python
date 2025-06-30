# This is 72nd code of this python course
# This code demonstrates the use of Regular Expressions

import re

para = '''The sun was setting behind the hills,
painting the sky in shades of orange and red.
Birds flew back to their nests, chirping softly.
A calm breeze moved through the trees.
Children laughed in the distance as they played.
The smell of fresh earth filled the air.
It was a peaceful moment after a long day.
Nature seemed to whisper a lullaby.'''

pattern = r'in'
print(re.search(pattern,para))
matches = re.finditer(pattern,para)
for match in matches:
    print(match)

pattern = r'[a-z]+n'
print(re.match(pattern,para))