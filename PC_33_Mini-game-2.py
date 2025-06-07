# This is 33rd code of this python course
# This code is a mini-game (Secret code word)

# Tasks of this game:
# 1. coding function:
#    - If the word contains at least 3 characters:
#         - Remove the first letter and append it at the end
#         - Then append three characters at the start and end
#    - Else: reverse the string

# 2. decoding function:
#    - If the word contains less than 3 characters, reverse it
#    - Else:
#         - Remove 3 characters from start and end
#         - Then remove the last letter and place it at the beginning

def coding(strg):
    if len(strg) >= 3:
        a = strg[0]              # Get first character
        strg = strg[1:] + a      # Move first character to the end
        p = "cba"                # Prefix
        s = "zyx"                # Suffix
        strg = p + strg + s
        print("Coded:", strg)
        return strg
    else:
        strg = strg[::-1]
        print("Coded:", strg)
        return strg


def decoding(code):
    if len(code) < 3:
        code = code[::-1]
        print("Decoded:", code)
        return code
    else:
        core = code[3:-3]        # Remove 3 from start and end
        core = core[-1] + core[:-1]  # Move last letter to the beginning
        print("Decoded:", core)
        return core


# Example usage:
c = coding("pavan")
d = decoding(c)

c2 = coding("hi")
d2 = decoding(c2)
