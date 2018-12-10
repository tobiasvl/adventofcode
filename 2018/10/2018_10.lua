lines = io.lines("input.txt")

stars = {}

for line in lines do
    local star = {pos={}, vel={}}
    star.pos.x, star.pos.y, star.vel.x, star.vel.y = string.match(line, "position=< *(-?%d+), *(-?%d+)> velocity=< *(-?%d+), *(-?%d+)>")
    table.insert(stars, star)
end

-- heuristics
start_at = 9999
for _, star in ipairs(stars) do
    star.pos.x = star.pos.x + star.vel.x * start_at
    star.pos.y = star.pos.y + star.vel.y * start_at
end

for second = start_at, math.huge do
    table.sort(stars, function(star1, star2)
        if star1.pos.y ~= star2.pos.y then
            return star1.pos.y < star2.pos.y
        else
            return star1.pos.x < star2.pos.x
        end
    end)

    local height = stars[#stars].pos.y - stars[1].pos.y

    if height > 9 then
        for _, star in ipairs(stars) do
            star.pos.x = star.pos.x + star.vel.x
            star.pos.y = star.pos.y + star.vel.y
        end
    else
        local old_x = stars[1].pos.x - 1
        s = ""
        for _, star in ipairs(stars) do
            -- points can overlap
            if old_x > star.pos.x then
                print(s)
                s = "#"
            elseif old_x < star.pos.x then
                s = s .. string.rep(" ", star.pos.x - old_x - 1) .. "#"
            end
            old_x = star.pos.x
        end
        print(s)
        print(second)
        break
    end
end
