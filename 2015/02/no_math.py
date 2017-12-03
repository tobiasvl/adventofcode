with open('input.txt') as f:
    presents = [[int(dimension) for dimension in line.strip().split('x')] for line in f if line != '\n']

paper = 0
ribbon = 0
for dimensions in presents:
    l, w, h = dimensions
    paper_dimensions = (l*w, w*h, h*l)
    paper += sum(map(lambda x: 2*x, paper_dimensions))
    paper += min(paper_dimensions)

    ribbon += l*w*h
    dimensions.remove(max(dimensions))
    ribbon += sum(map(lambda x: x+x, dimensions))

print "%d square feet of paper" % paper
print "%d feet of ribbon" % ribbon
