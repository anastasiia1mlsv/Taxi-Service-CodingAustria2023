# +
import defaults
import simulation
import plot

def main():
    
    ps = simulation.spawn_passengers(defaults.NODES)
    cars = simulation.generate_optimal_paths(defaults.PASSANGERS, defaults.NODES, defaults.EDGES)
    print(cars)
    
if __name__ == '__main__':
    main()
