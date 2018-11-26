function print_board()
  local i, s = 0, ""
  for y=1,h do
    for x=1,w do
      s = s .. (grid[y][x] and "#" or " ")
      if grid[y][x] then i = i+1 end
    end
    s = s .. "\n"
  end
  return i, s
end

local ops = {}
for line in io.lines("input.txt") do
  table.insert(ops, line)
end
w, h = 50, 6


grid = {}

for y=1,h do
  table.insert(grid, {})
  for x=1,w do
    table.insert(grid[y], false)
  end
end

for _, line in pairs(ops) do
  if string.find(line, "rect") then
    local _, _, x, y = string.find(line, "rect (%d+)x(%d+)")
    for yy=1,y do
      for xx=1,x do
        grid[yy][xx] = true
      end
    end
  elseif string.find(line, "rotate column") then
    local _, _, x, times = string.find(line, "rotate column x=(%d+) by (%d+)")
    x = x+1
    for i=1,times do
      local temp = grid[1][x]
      for yy=1,h do
        local temp2 = temp
        temp = grid[yy][x]
        grid[yy][x] = temp2
      end
      grid[1][x] = temp
    end
  elseif string.find(line, "rotate row") then
    local _, _, y, times = string.find(line, "rotate row y=(%d+) by (%d+)")
    y = y+1
    for i=1,times do
      local temp = grid[y][1]
      for xx=1,w do
        local temp2 = temp
        temp = grid[y][xx]
        grid[y][xx] = temp2
      end
      grid[y][1] = temp
    end
  end
end

local i, s = print_board()
print("Lit pixels: " .. i)
print("Code:\n" .. s)
