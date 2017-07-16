add <- function(x, y) {
  return (x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return (x * y)
}

divide <- function(x, y) {
  return (x / y)
}

power <- function(x, n) {
  return (x ^ n)
}

nth_root <- function(x, n) {
  return (x ^ (1/n))
}

square_root <- function(x) {
  return (nth_root (x, 2))
}

factorial <- function(n) {
  if (n < 0) return (Inf)
  if (n > 1) return (n * factorial(n - 1))
  else return (1)
}

reciprocal <- function(x) {
  return (1/x)
}

logarithm <- function(x) {
  return (log10(x))
}

print (add (1, 2))
print (add (c(1, 2), c(3, 4)))

print (subtract (4, 3))
print (subtract (5.3, 6.9))

print (multiply (5, 4))
print (multiply (3.8, -2.6))

print (divide (10, 2))
print (divide (-5, 7))
print (divide (0, 6))
print (divide (7, 0))

print (power (2, 3))
print (power (10, -2))
print (power (10, 0.5))

print (square_root(4))
print (square_root(-4))
print (square_root(0.5))

print (nth_root(8, 3))
print (nth_root(8,-3))
print (nth_root(100, 0))

print (factorial(3))
print (factorial(-1))

print (reciprocal (8))
print (reciprocal (-10))
print (reciprocal (0))

print (logarithm(10))
print (logarithm(100))
print (logarithm (0.1))
print (logarithm (-10))
