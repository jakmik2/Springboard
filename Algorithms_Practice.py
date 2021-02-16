def do_search(input_array, target_value):
    array_min = 0
    array_max = len(input_array)

    if array_min > array_max:
        guess = -1
    else:
        guess = int((array_min + array_max) / 2)

    if guess != -1:
        while True:
            if input_array[guess] == target_value:
                break
            elif input_array[guess] < target_value:
                array_min = guess
            else:
                array_max = guess
            guess = int((array_min + array_max) / 2)

    return guess


def swap(input_array, first_index, second_index):
    temp = input_array[first_index]
    input_array[first_index] = input_array[second_index]
    input_array[second_index] = temp

    return input_array


def index_of_minimum(input_array, start_index):
    min_value_index = start_index

    for i in range(start_index + 1, len(input_array)):
        if input_array[min_value_index] > input_array[i]:
            min_value_index = i

    return min_value_index


def sort_array(input_array):
    for i in range(0, len(input_array)):
        local_min = index_of_minimum(input_array, i)
        swap(input_array, local_min, i)

    return input_array


def add_to_sorted_array_linear(input_array, append):
    input_array.append(append)
    i = len(input_array) - 1
    while True:
        if input_array[i] < input_array[i - 1] and i != 0:
            swap(input_array, i, i - 1)
        else:
            break
        i -= 1

    return input_array


def do_search_less_than(input_array, input_value):
    # returns index (in input array) of the greatest value equal to or less than input_value in the input_array

    array_min = 0
    array_max = len(input_array)
    guess = int((array_min + array_max) / 2)

    while True:
        if input_array[guess] == input_value:
            break
        elif input_array[guess] < input_value < input_array[guess + 1]:
            break
        elif input_array[guess] > input_value:
            array_max = guess
        else:
            array_min = guess

        guess = int((array_min + array_max) / 2)

    return guess


def add_to_sorted_array_binomial(input_array, append):
    new_position = do_search_less_than(input_array, append)
    a = input_array[0:new_position]
    b = input_array[new_position + 1:len(input_array)]
    a.append(append)
    return a + b


def factorial(n):
    if n == 0:
        n = 1
    elif n < 0:
        n = None
    else:
        n = n * factorial(n - 1)
    return n


def palindrome_detector(input_string):
    # Returns true or false if it is or is not a palindrome
    output = False
    str_len = len(input_string)
    if str_len == 1:
        output = True
    elif input_string[0] == input_string[str_len - 1]:
        output = palindrome_detector(input_string[1:(str_len - 1)])
    return output


def power(x, n):
    output = False

    if n == 1:
        output = x
    elif n == 0:
        output = 1
    else:
        output = x * power(x, n - 1)

    return output


# Working with Heaps and Recursion!

def move_pegs(tower, current_peg, new_peg, base_value):
    other_peg = 3 - new_peg - current_peg

    # Base Case
    # Focus on SUBPROBLEM

    if base_value == tower[current_peg][-1]:
        move = tower[current_peg].pop()
        tower[new_peg].append(move)
    else:
        tower = move_pegs(tower, current_peg, other_peg, base_value - 1)
        tower = move_pegs(tower, current_peg, new_peg, base_value)
        tower = move_pegs(tower, other_peg, new_peg, base_value - 1)

    return tower


def divide_array(input_array, p, q, r):
    a = input_array[p:q]
    b = input_array[q:r + 1]
    return a, b


def merge(a, b):
    i = j = 0
    len_a = len(a)
    len_b = len(b)
    sorted_list = []
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append((b[j]))
        j += 1

    return sorted_list


def merge_sort(input_array):
    p = 0
    r = len(input_array)
    return merge_sort2(input_array, p, r)


def merge_sort2(input_array, p, r):
    if len(input_array) <= 1:
        return input_array  # I hate this

    q = (p + r) // 2
    left = input_array[:q]
    right = input_array[q:]

    left = merge_sort(left)
    right = merge_sort(right)

    input_array = merge(left, right)

    return input_array


def quick_sort(input_array):
    r = len(input_array)
    return quick_sort2(input_array, r)


def partition(input_array):
    pivot_index = 0
    pivot = input_array[pivot_index]

    start = pivot_index + 1
    end = len(input_array)
    smaller_than_pivot = []
    greater_than_pivot = []

    for i in range(start, end):
        if pivot <= input_array[i]:
            greater_than_pivot.append(input_array[i])
        elif pivot > input_array[i]:
            smaller_than_pivot.append(input_array[i])

    return smaller_than_pivot, pivot, greater_than_pivot


def quick_sort2(input_array, r):
    if r - 1 > 1:
        left, pivot, right = partition(input_array)

        left = quick_sort(left)
        right = quick_sort(right)

        input_array = left + [pivot] + right

    return input_array


# Breadth first search code

# The Following code is built from Joe James from this video URL: https://www.youtube.com/watch?v=-uR7BSfNJko
# 2/5/2021

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + ' ' + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


# End of Paraphrased code 2/5/2021

# Code to swap numbers with roman numerals

def numerical_to_roman(int_input):

    roman_numerals = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    str_int = str(int_input)
    digits = len(str_int)

    roman_output = []

    for i in range(0, digits):
        check = int(str(1) + i * str(0))

        storage = int(str_int[digits - 1 - i])

        key = ''

        if storage == 0:
            pass
        elif storage % 5 == 0 or storage == 1:
            key = roman_numerals[storage * check]
        elif (storage + 1) % 5 == 0 or (storage + 1) % 10 == 0:
            key = roman_numerals[(storage + 1) * check]
            key = roman_numerals[check] + key
        elif (storage - 1) % 5 == 0:
            key = roman_numerals[(storage - 1) * check]
            key += roman_numerals[check]
        else:
            if storage < 5:
                key = roman_numerals[check] * storage
            else:
                key = roman_numerals[5 * check]
                key = key + roman_numerals[check] * (storage - 5)

        roman_output.insert(0, key)

    roman_output = ''.join(roman_output)

    return roman_output


if __name__ == '__main__':
    for i in range(0, 1000, 111):
        print(numerical_to_roman(i))

