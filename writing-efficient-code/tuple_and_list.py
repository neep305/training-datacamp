
def main():
    names = ['Jason', 'Michael', 'Edward']
    legend_status = [False, False, True]
    generations = [1,1,1]
    
    poke_data = []
    
    for poke_tuple in zip(names, legend_status, generations):
        poke_list = list(poke_tuple)
        poke_data.append(poke_list)
    
    print(poke_data)
    
    
if __name__ == "__main__":
    main()
