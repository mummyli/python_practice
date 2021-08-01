import re

text = 'foo = 23 + 42 * 10'

NAME = r"(?P<NAME>[A-Za-z_][a-zA-Z0-9_]*)"
NUM = r"(?P<NUM>\d+)"
PLUS = r"(?P<PLUS>\+)"
TIMES = r"(?P<TIMS>\*)"
EQ = r"(?P<EQ>=)"
WS = r"(?P<WS>\s+)"

master_pat = re.compile("|".join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner(text)
for match in iter(scanner.match, None):
    print(match.lastgroup, match.group())