def pick(numbers: str, target):

    print("function called", numbers, target)

    if target <= 0:
        return True

    else:
        availables = [i for i in range(len(numbers)) if int(numbers[i])]
        print("available", availables)

        ahead_win = False

        if availables[-1] >= target:
            return True

        else:
            print("trying to guess")
            for available in availables:
                # taking available
                # we win if there is atleast one false from the stage ahead
                print("picking", available)

                numbers_copy = [el for el in numbers]
                numbers_copy[available] = '0'
                numbers_copy = ''.join(numbers_copy)
                print("callling functon")
                # value_from_function = pick(numbers_copy, target)
                ahead_win = ahead_win and pick(numbers_copy, target - available)

            verdict = 1 ^ ahead_win
            return verdict


if __name__ == '__main__':

    max_choosable = 10
    target = 11

    availables = ''.join([str(1)]*(max_choosable + 1))

    res = pick(availables, target)

    print(res)



