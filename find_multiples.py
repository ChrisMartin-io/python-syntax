def find_multiples(nums, count):
  return_arr = []
  for num in nums:
    if num % count == 0:
      # print("num: ", num)
      return_arr.append(num)
      # print("return_arr", return_arr)
  return return_arr


print(find_multiples([1, 2, 3], 2)) # 2