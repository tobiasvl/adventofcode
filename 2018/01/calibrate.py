freqs = []
with open('input.txt') as f:
    freqs = [int(freq.strip()) for freq in f]

def calibrate(twice=False):
    freq = 0
    seen = set()
    while True:
        for f in freqs:
            freq += f
            if freq in seen:
                return freq
            else:
                seen.add(freq)
        if not twice:
            return freq

print calibrate()
print calibrate(True)
