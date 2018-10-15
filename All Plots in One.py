import matplotlib.pyplot as plt
x=range(-10,10)
y=[]
x1=[1,2,3]
y1 = [10,20,5]
z = [100,200,300,400,500]
z1 = ['apple','mango','orange','grapes','watermelon']
v = [2,2,2,1,2,4,4,4,4,7,7,7,8,8,8,8,8,9,9,9,9,9]
for i in x:
    y.append(i**2)
plt.figure()
plt.subplot(2,3,1)
plt.plot(x,y,c = 'blue',lw = 3,label = 'Y = X^2',marker = 'o',ls = '--')
plt.title('PLOT')
plt.legend()
plt.subplot(2,3,2)
plt.scatter(x,y,facecolor = 'red',edgecolor = 'blue')
plt.title('SCATTER PLOT')
plt.legend()
plt.subplot(2,3,4)
plt.bar(x1,y1,facecolor = 'black',edgecolor = 'white')
plt.title('bar-graph')
plt.subplot(2,3,3)
plt.barh(x1,y1,facecolor = 'black',edgecolor = 'white')
plt.title('bar-horizontal-graph')
plt.subplot(2,3,5)
plt.hist(v,bins = 20)
plt.title('histogram')
plt.subplot(2,3,6)
plt.pie(z,labels = z1,explode = (0,.1,0,0,0),autopct = '%0.1f%%',shadow = True)
plt.title('Pie- Chart')
plt.show()
