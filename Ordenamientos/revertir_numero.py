def revertir(A,B):
  if A==0:
    return 1
  else:
    print(A[B-1])
  return revertir(A,B-1)

print(revertir(5236,0))