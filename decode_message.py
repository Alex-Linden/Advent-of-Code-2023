def decode(message_file):
    # open the file and spilt into list with each element being a ling from the file
    encoded = open(message_file).read().split("\n")
    # create a dict to track what words correspond to what numbers
    num_to_word = {}
    message = ""

    for line in encoded:
        num, word = line.split(" ")
        num_to_word[int(num)] = word

    # i = num we are looking for and step is the size to add to i to find the next num
    i = 1
    step = 2
    while i <= len(num_to_word):
        message += num_to_word[i] + " "
        i += step
        step += 1

    return message


decode("decode.txt")
