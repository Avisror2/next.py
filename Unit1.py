#  Returns the longest name in the name file
def stage_1(name_file): return max(name_file.read().split(), key=len)


#  Returns the sum of the lengths of the names in the name file
def stage_2(name_file): return sum(len(name) for name in name_file.read().split())


#  Prints the shortest names in the name file
def stage_3(name_file):
    names = name_file.read().splitlines()
    min_length = min(len(name) for name in names)
    print("\n".join(name for name in names if len(name) == min_length))


#  Creates a new file called name_length and writes all the name lengths to it from name file
def stage_4(name_file):
    with open('name_length.txt', "w+") as name_length_file:
        for name in name_file.read().split():
            name_length_file.write('{}\n'.format(name))


def main():

    with open(r'C:\Users\user\PycharmProjects\next\names.txt') as name_file:

        print(stage_1(name_file))  # Stage 1
        name_file.seek(0)  # Reset the pointer back after each stage

        print(stage_2(name_file))  # Stage 2
        name_file.seek(0)

        stage_3(name_file)  # Stage 3
        name_file.seek(0)

        stage_4(name_file)  # Stage 4
        name_file.seek(0)


if __name__ == '__main__':
    main()
