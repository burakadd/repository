def recover_secret(triplets):
    secret = []
    while triplets:
        second_and_third_letters = [letter for array in triplets for letter in array[1:]]
        for array in triplets:
            if array[0] not in second_and_third_letters:
                secret.append(array[0])
                triplets = list(map(
                    lambda array: array[1:] if secret[-1] == array[0] else array, triplets))
                break
        triplets = list(filter(lambda array: bool(array), triplets))
    return ''.join(secret)


recoverSecret = recover_secret