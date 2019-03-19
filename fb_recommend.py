from colorama import Fore, Back, Style, init
init()

def open_file():
    try:
        file = input("\nPlease enter file name(big or small): ")
        file = file + ".txt"
        fp = open(file)
        n = fp.readline()
        n = int(n)
        network = []

        for i in range(n):
            network.append([])

        for oku in fp:
            sp = oku.split(" ")
            network[int(sp[0])].append(int(sp[1]))
            network[int(sp[1])].append(int(sp[0]))

        return network
    except FileNotFoundError:
        print("File Not Found! TRY AGAIN!")
        main()
    finally:
        fp.close()


def num_in_common_between_lists(list1, list2):
    counter = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                counter += 1
    return counter


def init_matrix(n):
    """Create an nxn matrix, initialize with zeros, and return the matrix."""
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix


def calc_similarity_scores(network):
    n = len(network)
    matrix = init_matrix(n)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = num_in_common_between_lists(network[i], network[j])

    return matrix


def recommend(user_id, network, similarity_matrix):
    n = len(network)
    biggest = 0
    index = -1
    for i in range(n):
        bayrak = True
        if i != user_id and similarity_matrix[user_id][i] > biggest:
            for j in range(len(network[user_id])):
                if network[user_id][j] == i:
                    bayrak = False
                    break
            if bayrak:
                biggest = similarity_matrix[user_id][i]
                index = i
    return index

def main():
    network = open_file()
    matrix = calc_similarity_scores(network)
    print("\nFacebook Friend Recommendation.")
    bayrak = True
    while bayrak:
        user = int(input("\nEnter user who you want to the recommendations for\n(0 to " + str(len(network)-1) + "): "))
        rec = recommend(user, network, matrix)
        
        text = "Most recommended person for " + Fore.GREEN + str(user) + Style.RESET_ALL + " is " + Fore.MAGENTA + str(rec) + Style.RESET_ALL
        print(text)

        choice = input("\nDo you want to continue (yes/no):")
        if choice.lower() == 'yes':
            pass
        elif choice.lower() == 'no':
            bye = Fore.RED + "BYE!" + Style.RESET_ALL
            print(bye)
            bayrak = False
        else:
            print("Inappropriate Input")
            bayrak = False

if __name__ == "__main__":
    main()