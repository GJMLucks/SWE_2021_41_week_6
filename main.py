def twoSum(nums: List[int], target: int) -> List[int]:
  length = len(nums)
  indexList = { i : v for i, v in enumerate(nums) }
  sortedIndexList = sorted(indexList.items(), key = lambda item : item[1])
  
  for i in range(length-1):
    for j in range(i+1, length):
      sum = sortedIndexList[i][1] + sortedIndexList[j][1]
      if sum < target:
        continue
      if sum > target:
        break
      return [ sortedIndexList[i][0], sortedIndexList[j][0] ]
  return []