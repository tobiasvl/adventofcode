file = io.open("input.txt", "r"):read("*all")
file = string.gsub(file, "%s", "")

function decompress(file)
  s = ""
  start = 1
  while start do
    start, stop, chars, times = string.find(file, "%((%d+)x(%d+)%)")
    if start then
      s = s .. string.sub(file, 1, start - 1)
      file = string.sub(file, stop + 1)
      for i=1,times do
        s = s .. string.sub(file, 1, chars)
      end
      file = string.sub(file, chars + 1)
    else
      s = s .. file
    end
  end
  return s
end

function decompress_length(file)
  local start, stop, chars, times = string.find(file, "%((%d+)x(%d+)%)")
  local s = 0
  if start then
    s = s + start - 1
    file = string.sub(file, stop + 1)
    s = s + (decompress_length(string.sub(file, 1, chars)) * times)
  else
    return #file
  end
  return s + decompress_length(string.sub(file, chars + 1))
end

print("Decompressed length: " .. #decompress(file))
print("Decompressed length with improved format: " .. decompress_length(file))
