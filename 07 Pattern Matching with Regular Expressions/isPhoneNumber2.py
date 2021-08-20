import re
message = 'Call me at 415-555-1011 tomorrow.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print('Phone number found: ' + mo.group())