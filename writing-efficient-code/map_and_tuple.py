# more efficient way to make a list

def main():
    names = ['Jason', 'Michael', 'Edward']
    legend_status = [False, False, True]
    generations = [1,1,1]
    poke_data_tuple = []
    
    for poke_tuple in zip(names, legend_status, generations):
        poke_data_tuple.append(poke_tuple)

    poke_data = [*map(list, poke_data_tuple)]
    print(poke_data)
    
    
if __name__ == "__main__":
    main()
