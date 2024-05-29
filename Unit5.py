# Personalized ID iterator
class IDIterator:
    def __init__(self, start_id=0):
        self.id_ = start_id
        self.max_id = 999999999  # Max ID number

    def __iter__(self):
        return self

    def __next__(self):
        while self.id_ <= self.max_id:
            current_id = self.id_
            self.id_ += 1  # Increase for next ID
            if check_id_valid(current_id):
                return current_id  # Return valid id
        raise StopIteration


# Personalized ID generator
def id_generator(start_id):
    max_id = 999999999  # Max ID number
    current_id = start_id

    while current_id <= max_id:
        if check_id_valid(current_id):
            yield current_id  # ID is valid
        current_id += 1  # Increase for next ID


# Returns whether a given id is valid
def check_id_valid(id_number):
    id_str = str(id_number)  # Convert to string for iteration
    total = 0
    for i in range(9):
        factor = 2 if i % 2 == 1 else 1  # Check if location is even or odd
        result = int(id_str[i]) * factor  # Multiply by the correct factor
        if result > 9:
            result = result // 10 + result % 10  # If the sum is greater than 9 add both numbers of the id
        total += result  # Sum all the results together
    return total % 10 == 0  # If the final total is dividable by 10 with no leftover id is valid True


def main():
    user_input_id = int(input('Enter ID: '))
    user_input_choice = input('Generator or Iterator? (gen/it)? ')

    if user_input_choice == 'it':
        id_iter = IDIterator(user_input_id)  # Use iterator
        for id_num in range(10):
            print(next(id_iter))
    else:
        count = 0  # Counter for the number of IDs generated
        for id_num in id_generator(user_input_id):  # Use generator
            print(id_num)
            count += 1  # Increase counter
            if count >= 10:  # Stop after generating 10 IDs
                break


if __name__ == '__main__':
    main()
