def squared(x):
    squared = x ** 2
    print("The square of %d is %d." % (x, squared))

squared(24)

def shut_down(s):
  if s == "yes":
    print("Shutting Down")
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

shut_down("yes")