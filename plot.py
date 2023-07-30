from matplotlib import pyplot as plt

def export_plot(nodes, edges, ps):
    
    for n in nodes:
#         plt.scatter(*coordinates[n], c = 'blue')
        plt.text(coordinates[n][0], coordinates[n][1], n, c = 'blue')

    for edge in edges:
        plt.plot([coordinates[edge['Nodes'][0]][0], coordinates[edge['Nodes'][1]][0]], [coordinates[edge['Nodes'][0]][1], coordinates[edge['Nodes'][1]][1]],
                c = 'grey', alpha = 0.5)
                
    for p in ps:
        coord = coordinates[p['Start']]
        plt.text(coord[0], coord[1], p['Name'], c = 'green')
        coord = coordinates[p['Target']]
        plt.text(coord[0], coord[1], p['Name'], c = 'red')
        
    plt.savefig('sim_result.jpg')
