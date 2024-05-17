#  Returns the longest name in the name file
def stage_1(name_file): return max(name_file.read().split(), key=len)


#  Returns the sum of the lengths of the names in the name file
def stage_2(name_file): return sum(len(name) for name in name_file.read().split())


#  Prints the shortest names in the name file
def stage_3(name_file):
    names = name_file.read().splitlines()
    min_length = min(len(name) for name in names)
    print("\n".join(name for name in names if len(name) == min_length))


def main():

    with open(r'C:\Users\user\PycharmProjects\next\names.txt') as name_file:
        print(stage_1(name_file))
        name_file.seek(0)  # Reset the pointer back after each stage
        print(stage_2(name_file))
        name_file.seek(0)  # Reset the pointer back after each stage
        stage_3(name_file)
        name_file.seek(0)  # Reset the pointer back after each stage
        stage_3(name_file)


if __name__ == '__main__':
    main()
