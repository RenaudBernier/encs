from collections import deque


dq = deque()



def algoSearch(dq, left, right, x): # NOTE: dq is a deque!!!
  mid = left + int((right-left)/2)
  
  if dq[mid] < x:
    algoSearch(dq, left, mid-1, x)
  elif dq[mid] > x:
    algoSearch(dq, mid+1, right, x)
  else:
    return mid

def explore(root):
  print(1)


def traversal(root):
  if root.left is not None:
    traversal(root.left)

  explore(root)

  if root.right is not None:
    traversal(root.right)


def algoSpace(n):
  arr = []
  for i in range(n):
    for j in range(i, n):
      arr.append(j)



def algoTime(n):
  i = 1
  while i < n:
    for j in range(i):
      print(i, j)
    i *= 2




i = 1
def algoNest(arr):
  i = 0
  def inner(x):
    nonlocal i
    arr[i] = x
    i += 1
  return inner

myList = [1, 2, 3, 4]
myFunc = algoNest(myList)

myFunc(4)
myFunc(9)

print(myList)
print(i)



