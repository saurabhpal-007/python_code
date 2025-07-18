# 1 satr pattern 

# for i in range(1,5):
#     for j in range(1,5):
#         if j<=i:
#             print("*", end=' ')
#         else:
#             print(" ", end="")
#     print()

# -------------------------------------------------

 # 2nd satr pattern 

# for i in range(1,5):
#     for j in range(1,5):
#         if j>=5-i:
#             print("*", end='')
#         else:
#             print(" ", end="")
#     print()

# -------------------------------------------------

 # 3rd satr pattern 

# for i in range(1,5):
#     for j in range(1,5):
#         if j<=5-i:
#             print("*", end='')
#         else:
#             print(" ", end="")
#     print()

# ------------------------------------------------

# 4th satr pattern 

# for i in range(1,5):
#     for j in range(1,5):
#         if j>=i:
#             print("*", end='')
#         else:
#             print(" ", end="")
#     print()

# ------------------------------------------------

# 5th satr pattern 

# for i in range(1,5):
#     for j in range(1,8):
#         if j>=5-i and j<=3+i:
#             print("*", end='')
#         else:
#             print(" ", end="")
#     print()

# ---------------------------------------------------------

# 6th satr pattern 

# for i in range(1,5):
#     for j in range(1,8):
#         if j>=i and j<=8-i:
#             print("*", end='')
#         else:
#             print(" ", end="")
#     print()

# --------------------------------------------------

# 7th satr pattern 

for i in range(1,5):
    for j in range(1,8):
        if j<=5-i or j>=3+i:
            print("*", end='')
        else:
            print(" ", end="")
    print()