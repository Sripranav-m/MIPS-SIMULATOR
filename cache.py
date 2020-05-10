import math

def divide_address(address, num_of_sets, num_of_block_words):

    div_add = []

    num_bits_offset = int(math.log2(num_of_block_words))
    num_bits_index = int(math.log2(num_of_sets))

    div_add.append(address[0 : (len(address) - (num_bits_index + num_bits_offset)) ])
    div_add.append(address[len(address) - (num_bits_index + num_bits_offset)  : len(address) - num_bits_offset])
    if(num_bits_offset == 0 ):
        div_add.append('')
    else:
        div_add.append(address[ -(num_bits_offset):])

    return div_add


def cache_insert(cache1, address_list):  
    if(len(cache1[int(address_list[1],2)]) < ( num_of_lines / num_of_sets)):
        cache1[int(address_list[1],2)].insert(0, [address_list])
    else:
        cache1[int(address_list[1],2)].pop()
        cache1[int(address_list[1],2)].insert(0,[address_list])

def cache2_insert(cache2, address_list):    
    if(len(cache2[int(address_list[1],2)]) < ( num_of_lines_2 / num_of_sets_2)):
        cache2[int(address_list[1],2)].insert(0, [address_list])
    else:
        cache2[int(address_list[1],2)].pop(-1)
        cache2[int(address_list[1],2)].insert(0,[address_list])

################## data of cache 1 ####################

set_size = 2 #int(input("Enter set associativity: "))
cache_size = 32 #int(input("Enter cache size: "))
block_size = 4 #int(input("Enter block size: "))

num_of_lines = cache_size/block_size

num_of_sets = int(num_of_lines/set_size)

num_of_block_words = int(block_size/4)


######### data of cache2 ##############

set_size_2 = 2 #int(input("Enter set associativity of cache 2: "))
cache_size_2 =  32 #int(input("Enter cache size of cache 2: "))

num_of_lines_2 = int(cache_size_2 / block_size)
num_of_sets_2 = int(num_of_lines_2 / set_size_2)


cache1 = [[[[""] for k in range(num_of_block_words)] for j in range(set_size)] for i in range(num_of_sets)]

cache2 = [[[[""] for k in range(num_of_block_words)] for j in range(set_size_2)] for i in range(num_of_sets_2)]
            

while(True):    

    #acess_latency = int(input('Enter access latencies: '))

    x = int(input("Enter the number you want to search in cache: "))

    address = '{:032b}'.format(x)

    divided_address = divide_address(address, num_of_sets, num_of_block_words)

    cach1_fl = 0
    cach2_fl = 0

    num_of_misses = 0

    for i in range(len(cache1[int(divided_address[1],2)])):
        if(cache1[int(divided_address[1],2)][i] != [['']]):
            if(int(cache1[int(divided_address[1],2)][i][0][0],2) == int(divided_address[0],2)):
                print("It is a hit in cache 1")
                cach1_fl = 1
                cache1[int(divided_address[1],2)].insert(0, cache1[int(divided_address[1],2)].pop(i))



    if cach1_fl == 0:
        print("It is a miss in cache1: ")
        num_of_misses += 1    

        cache2_divided_address = divide_address(address, num_of_sets_2, num_of_block_words)
        
        cache1_divided_address = divide_address(address, num_of_sets, num_of_block_words)

        for i in range( len ( cache2[ int( cache2_divided_address[1], 2) ])) :
            if(cache2[ int(cache2_divided_address[1], 2)][i] != [['']]) :
                if( int(cache2[int(cache2_divided_address[1],2)][i][0][0],2) == int(cache2_divided_address[0],2) ) :
                    print("It's a hit in cache 2")
                    cach2_fl = 1
                    cache_insert(cache1, cache2[int(cache1_divided_address[1], 2)][i][0])
                    cache2[int(divided_address[1],2)].insert(0, cache1[int(divided_address[1],2)].pop(i))                    

        if(cach2_fl == 0):
            print("It's a miss in cache 2")
            
            from_data_segment = int(input("Enter value from data segment: "))

            data_segment = '{:032b}'.format(from_data_segment)

            data_segment_list = divide_address(data_segment, num_of_sets, num_of_block_words)

            cache2_insert(cache2, data_segment_list)
            cache_insert(cache1, data_segment_list)

    print(cache1)
    print(cache2)
