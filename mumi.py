#!/usr/bin/python3

# I wrote this to quickly see whether the MU->MI puzzle in Godel-Escher-Bach
# by Douglas Hofstadter has a quick solution.
# It turns out to provably have no solution, so this doesn't converge!


def transmutes(instr):
    mutes = []

    mutes.append(instr+instr)
    if instr.endswith('I'):
        mutes.append(instr+'U')

    # 3 I's make a U
    i = 0
    while i <= len(instr)-3:
        a,b,c = instr[i:i+3]
        if a == b == c == 'I':
            mutes.append(instr[:i]+'U'+instr[i+3:])
        i += 1

    # 2 U's disappear
    i = 0
    while i <= len(instr)-2:
        a,b = instr[i:i+2]
        if a == b == 'U':
            mutes.append(instr[:i]+instr[i+2:])
        i += 1

    print(instr,"transmutes to:",mutes)
    return mutes
print(list(transmutes(_) for _ in transmutes('III')))

hit = set()

MAX_LEN = 30

stack = ['I']
while stack:
    item = stack.pop()
    mutes = transmutes(item)
    if any(_ is 'U' for _ in mutes):
        print("FOUND IT")
        break

    kept_mutes = [m for m in mutes if len(m) < MAX_LEN and m not in hit]

    hit.update(set(kept_mutes))
    stack.extend(kept_mutes)
    print("Stack length:",len(stack))

# print(transmutes('I'))
