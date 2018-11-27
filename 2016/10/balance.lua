bots = {}
outputs = {}

ops = io.lines("input.txt")
compare = {17, 61}

for line in ops do
  if string.find(line, "value") then
    local _, _, value, bot = string.find(line, "value (%d+) goes to bot (%d+)")
    value = tonumber(value)
    bot = tonumber(bot)
    if not bots[bot] then bots[bot] = {} end
    table.insert(bots[bot], value)
  else
    local _, _, bot, low_target, low, high_target, high = string.find(line, "bot (%d+) gives low to (%a+) (%d+) and high to (%a+) (%d+)")
    bot = tonumber(bot)
    if not bots[bot] then bots[bot] = {} end
    loadstring("if not " .. low_target .. "s[" .. low .. "] then " .. low_target .. "s[" .. low .. "] = {} end")()
    loadstring("if not " .. high_target .. "s[" .. high .. "] then " .. high_target .. "s[" .. high .. "] = {} end")()
    bots[bot].low_target = low_target
    bots[bot].low = tonumber(low)
    bots[bot].high_target = high_target
    bots[bot].high = tonumber(high)
  end
end

found_outputs = false
found_bot = false

while not found_bot or not found_outputs do
  if #outputs[0]>0 and #outputs[1]>0 and #outputs[2]>0 and not found_outputs then
    print("Output values: " .. outputs[0][1] * outputs[1][1] * outputs[2][1])
    found_outputs = true
  end
  for i=0,#bots do
    if bots[i][1] and bots[i][2] then
      table.sort(bots[i])
      if bots[i][1] == compare[1] and bots[i][2] == compare[2] and not found_bot then
        print("Bot number: " .. i)
        found_bot = true
      end
  
      local low, high, low_target, high_target = bots[i].low, bots[i].high, bots[i].low_target, bots[i].high_target
      low = low_target .. "s[" .. low .. "]"
      high = high_target .. "s[" .. high .. "]"
  
      loadstring("table.insert(" .. low .. ", bots[" .. i .. "][1])")()
      loadstring("table.insert(" .. high .. ", bots[" .. i .. "][2])")()
  
      bots[i][1] = nil
      bots[i][2] = nil
    end
  end
end
