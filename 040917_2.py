import numpy as np
import pylab as pl
# Crea un vector (arreglo) con los vectores del eje X
x = [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
pl.xlabel('year')
y = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 3, 2, 2, 2, 2, 1]
pl.ylabel('number of girlfriends and pets per year')
pl.plot (x,y, 'bo')
# Guardar la grafica en formato png
pl.savefig('temp2.png')
pl.show()
