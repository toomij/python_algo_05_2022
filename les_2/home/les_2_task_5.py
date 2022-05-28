for i in range(32, 128):
    print(f'\t{i} - {chr(i)}', end='')
    if i % 10 == 1:
        print()