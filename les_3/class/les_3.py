# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
# list_4 = [1, 2, 3, 4]
#
# for i, item in enumerate(list_1):
#     del item
#
# print(list_1)
#
# for i, item in enumerate(list_2):
#     list_2.remove(item)
#
# print(list_2)
#
# for i, item in enumerate(list_3):
#     list_3.pop(i)
#
# print(list_3)
#
# for i, item in enumerate(list_4[:]):
#     list_4.remove(item)
#
# print(list_4)

# Крестики-нолики

row = [''] * 3
board = [row] * 3
print(board)

board[0][0] = 'X'
print(board)

board = [[''] * 3 for _ in range(3)]
board[0][0] = 'X'
print(board)

