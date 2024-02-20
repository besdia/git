def factorial(n):
  """
  Ця функція обчислює факторіал числа n.

  Args:
      n: Ціле число

  Returns:
      Факторіал числа n
  """
  if n < 0:
    raise ValueError("Факторіал не визначений для від'ємних чисел")
  elif n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

# Приклад використання
print(factorial(5))  # Виводить 120
