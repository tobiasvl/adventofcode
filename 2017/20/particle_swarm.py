from re import match
from collections import defaultdict
from operator import add, itemgetter

particles = []
with open('input.txt') as f:
    particle = 0
    for line in f:
        attrs = match('p=<([-0-9]*),([-0-9]*),([-0-9]*)>, '
                      'v=<([-0-9]*),([-0-9]*),([-0-9]*)>, '
                      'a=<([-0-9]*),([-0-9]*),([-0-9]*)', line)
        p, v, a = (map(int, (attrs.group(i) for i in (1, 2, 3))),
                   map(int, (attrs.group(i) for i in (4, 5, 6))),
                   map(int, (attrs.group(i) for i in (7, 8, 9))))
        particles.append({'p': tuple(p), 'v': tuple(v), 'a': tuple(a)})
        particle += 1

safe_particles = range(len(particles))
shortest_distances = {k: 0 for k in xrange(len(particles))}
time_since_last_collision = 0

# Should probably find an actual condition for when all collisions
# are resolved
while time_since_last_collision < 1000:
    time_since_last_collision += 1
    positions = defaultdict(list)
    distances = [0 for _ in xrange(len(particles))]
    for p in xrange(len(particles)):
        particles[p]['v'] = tuple(map(add, particles[p]['v'], particles[p]['a']))
        particles[p]['p'] = tuple(map(add, particles[p]['p'], particles[p]['v']))
        distances[p] = sum(map(abs, particles[p]['p']))
        positions[particles[p]['p']].append(p)
    shortest_distances[distances.index(min(distances))] += 1
    for k, v in positions.iteritems():
        if len(v) > 1:
            time_since_last_collision = 0
            for i in v:
                safe_particles.remove(i)

closest_particle = max(shortest_distances.iteritems(), key=itemgetter(1))[0]
print "Particle %d stays closest to position <0,0,0>" % closest_particle
print "%d particles left after collisions are resolved" % len(safe_particles)
