from matplotlib import pyplot as plt 
import pandas

def graph(xCord, yCord, color, pointSize, borderLine, transparency):
    plt.scatter(x=xCord, y=yCord, edgecolors=color, s = pointSize , linewidths=borderLine, alpha=transparency )
    

def main():
    pass

plt.scatter(x=plot_set['weight_last_year'],
            y=plot_set['rescues_last_year'],
            edgecolors='violet',
            s=300,
            linewidths=0,
            alpha=0.5)
x = numpy.linspace(data['weight_last_year'].min(),
                   data['weight_last_year'].max(), 26)
print(x)
y = model.params[1] * x + model.params[0]
plt.plot(x, y, 'r')
#! Uncomment
plt.show()

if __name__: "__main__":
    main()
    
