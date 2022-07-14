
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


col_pos=int(position[0])
row_pos=int(position[1])
map[col_pos-1][row_pos-1]="❌"

#Alternate approach:

# if row_pos==1:
#     if col_pos==1:
#         row1[0]="X"
#     elif col_pos==2:
#         row1[1]="X"
#     elif col_pos==3:
#         row1[2]="X"
# elif row_pos==2:
#     if col_pos==1:
#         row2[0]="X"
#     elif col_pos==2:
#         row2[1]="X"
#     elif col_pos==3:
#         row2[2]="X"
# elif row_pos==3:
#     if col_pos==1:
#         row3[0]="X"
#     elif col_pos==2:
#         row3[1]="X"
#     elif col_pos==3:
#         row3[2]="X"

print(f"{row1}\n{row2}\n{row3}")