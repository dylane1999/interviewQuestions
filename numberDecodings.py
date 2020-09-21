import sys


def numDecodings(message):
    if not message:
        return 0

    # Array to store the # of decodings
    results = [0 for _ in range(len(message) + 1)]

    results[0] = 1 # possible decodings for nonzero message w/ one char is one

    if message[0] == '0':     # 0 does not have a decoding
        results[1] = 0
    else:
        results[1] = 1

    for i in range(2, len(results)):

        # Check for single decode
        if message[i - 1] != '0':
            results[i] += results[i - 1]

        # Check for double decode
        possibleDecode = int(message[i - 2: i])
        if possibleDecode >= 10 and possibleDecode <= 26:
            results[i] += results[i - 2]
    return results[len(message)]


def main():
    for line in sys.stdin:
        print(numDecodings(line))


