for row in range(10): #this line prints numbers from range 0 to 9
 for column in range(10):
  print('<' if row % 2 == 1 else '>', end='')
  # the line above prints the '<' symbol if the number in row when row %2 has a remainder, else prints '>' when there is no remainder...the "end=''" prints the characters with spaces between them
 print(row)
