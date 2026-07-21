#pass : to neglect the block of code in a loop or conditional statement. It is used as a placeholder when the code is syntactically required but you do not want to execute any code.

# 1. pass : to neglect expected indentation error 

#3. continue : to skip the current iteration of the loop and continue with the next iteration.
for i in range (1,11):
  if (i == 3):
    continue
  print(i)

# 4.else : to execute a block of code when the loop is completed normally without any break statement. It is executed when the loop is not terminated by a break statement.
for i in range (1,11):
  if(i == 3):
    break
  print(i)
else:
  print("Loop executed successfully.")