def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    count = 0
    for index, number in enumerate(data):
        if int(data[index]) > int(data[index-1]):
            count+=1

    print(count)

if __name__ == '__main__':
    main()