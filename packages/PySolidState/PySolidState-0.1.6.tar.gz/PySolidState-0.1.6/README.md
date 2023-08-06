<h1 align="center"> <a href="https://imgur.com/L01ipPl"><img src="https://i.imgur.com/L01ipPl.png" title="source: imgur.com" /></a>
  
<h1 align="center"> PySolidState (PySS) </h1>

>PySS es una biblioteca desarrollada como una herramienta de apoyo para el estudio introductorio del estado sólido y los conceptos básicos de los materiales. Su enfoque principal es proporcionar apoyo visual y funcionalidades que permitan asentar los conceptos fundamentales en esta área de estudio, desde estructuras cristalinas hasta modelos de enlace fuerte. Con un conjunto de herramientas y funcionalidades, PySolidState permite a investigadores y estudiantes analizar y simular varios aspectos de la física del estado sólido. Además, esta biblioteca se combina con notas de curso sobre estado sólido, lo que la convierte en un recurso bastante completo para el aprendizaje de la materia a nivel universitario. Gracias a su enfoque en la visualización y el apoyo práctico, PySolidState se convierte en una valiosa herramienta que, junto con las notas de curso, ofrece una base sólida para comprender los principios y fundamentos del estado sólido.

**Deployment**

![PyPI](https://img.shields.io/pypi/v/PySolidState)

## Recursos
- Documentación
- [Notas del curso de estado sólido](https://yerimi.gitbook.io/materias./modelo-tight-binding)

## Instalación
Se recomienda utilizar pip para la instalación. Asegúrese de que la última versión esté instalada, ya que PySS se actualiza con frecuencia:

>Nota: Es importante antes de instalar la libreria PySolidState haber ejecutado la consola en modo administrador si se trabajara con jupyter notebook.

ejecute los siguientes comando para la instalación:
```python
   pip install PySolidState    # Instalacion normal
   pip install --upgrade PySolidState  # o actualizar si es necesario
```
**Dependencias Requeridas:**
- Python 3.9+
- matplotlib >=3.7.1
- numpy>=1.24.3
- mayavi>=4.7.2
- scikit-spatial>=7.0.0

## Uso
Antes de dar los primeros pasos en la librería, es fundamental tener en cuenta la siguiente convención de ángulos entre los vectores de la red, los cuales serán utilizados en PySolidState:

<h1 align="center"><a href="https://imgur.com/k601U6V"><img src="https://i.imgur.com/k601U6Vm.png" title="source: imgur.com" /></a>

<h1 align="center">(α, β, γ)</h1>

Esta convención de ángulos juega un papel crucial en el funcionamiento adecuado de la librería PySolidState y es importante asegurarse de seguir correctamente esta notación al utilizarla. 

### Crear Red (Create Lattice):
Uno de los conceptos mas basico y fundamental en el estado solido es el de red, siendo las unicas posibles en formar estructuras cistalinas las redes de Bravais; para crea una de estas tenemos dos formas de hacerlo:

**1)** Construyendo la red a partir de los parámetros:
- ***System*** = Nombres de sistemas de redes de Bravais.
- ***structure_type*** = centrada en las caras, centrada en el cuerpo o centrada en las bases;  si la el sistema tiene de red.
- ***dimension*** = dimensión en la cual se creara la red 2D o 3D.
  
Nota: Si la red es 3D tambien se le puede pasar otro atributo llamado ***size*** (cuya función es mostrar la celda en diferentes tamaños "N" veces el parametro de red.)

A continuación se muestra un ejemplo de uso:
```python
from PySolidState.crystal_structure.lattice import Lattice  # Importamos el modulo estructura cristalina de la libreria junto al metodo lattices

lattice = Lattice(system='cubic',structure_type='face_centered', dimension='3D') # Se crea la red
lattice.plot()  # Se grafica la red
```
**2)** Construyendo la red a partir de los parámetros_
- ***magnitude***  = tupla con la norma de cada uno de los vectores de la red a1, a2 y a3.
- ***angles*** = tupla con los angulos que describen los vectores de la red (α, β, γ).
- ***dimension*** = dimensión en la cual se creara la red 2D o 3D.
  
Nota: Si la red es 3D tambien se le puede pasar otro atributo llamado ***size*** (cuya función es mostrar la celda en diferentes tamaños "N" veces el parametro de red.)

A continuación se muestra un ejemplo de uso:
```python
from PySolidState.crystal_structure.lattice import Lattice  # Importamos el modulo estructura cristalina de la libreria junto al metodo lattices

lattice = Lattice(magnitude=(1,1,1),angles=(90,90,90), dimension='3D') # Se crea la red
lattice.plot()  # Se grafica la red
```
### Crear base (Create base):
El otro concepto más básico es el de base, siendo esta base el conjunto de átomos que se acomodan en cada punto de red para formar la estructura cristalina. A continuación se muestra un ejemplo de como crear esta base de átomos:

```python
# Se importan los módulos Lattice, Atom, Base
from PySolidState.crystal_structure.lattice import Lattice
from PySolidState.crystal_structure.atom import Atom
from PySolidState.crystal_structure.base import Base

#Se crean los átomos que harán parte de la base de átomos
atom2 = Atom(name='Na+', size= 0.2, color= 'orangered')
atom1 = Atom(name='Cl-', size= 0.3, color= 'springgreen')

#Se crea la red a la cual se acomodaran
lattice = Lattice(system='cubic',structure_type='face_centered', dimension='3D')

# Se crea la base de átomos
base = Base(lattice_vectors= lattice.vectors, atoms=[[atom1, [0,0,0]],[atom2, [0.5,0,0]],[atom2, [0,0.5,0]],[atom2, [0,0,0.5]]], dimension='3D')

#Se grafica la base de atomos en un punto de red
base.plot()
```
Como notamos en el ejemplo la clase Base se inicializa pasándole los vectores de la red, una lista que contiene listas de los átomos creados, con su vector posición en la base a formar y la dimensión en la que se describirá.

### Crear estructurá cristalina
Con los dos conceptos previamente mostrados podemos formar lo que se conoce como estructura cristalina o cristal, siendo esta estructura la unión de una red de Bravais con una base de átomos, para ello a continuación se muestra un ejemplo de como construirla:


```python
# Se importan los modulos Lattice, Atom, Base y CristalStruture.
%matplotlib widget
from PySolidState.crystal_structure.lattice import Lattice
from PySolidState.crystal_structure.atom import Atom
from PySolidState.crystal_structure.base import Base
from PySolidState.crystal_structure.crystalStructure import CrystalStructure

#Se crean los átomos que harán parte de la base de átomos.
atom2 = Atom(name='Na+', size= 0.2, color= 'orangered')
atom1 = Atom(name='Cl-', size= 0.3, color= 'springgreen')

#Se crea la red de Bravais en la cual se acomodara la base de atomos.
lattice = Lattice(system='cubic',structure_type='face_centered', dimension='3D')
# Se crea la base de átomos
base = Base(lattice_vectors= lattice.vectors, atoms=[[atom1, [0,0,0]],[atom2, [0.5,0,0]],[atom2, [0,0.5,0]],[atom2, [0,0,0.5]]], dimension='3D')

# Se crea la estructura cristalina o cristal uniendo la red y la base ya creadas
crs = CrystalStructure(lattice=lattice, base=base, dimension='3D')
#Se crea la figura de la red cristalina o cristal Na+Cl- (Cloruro de Sodio)
crs.plot()
```
### Crear Celdas de una red o una estructura cristalina
Dada una estructura cristalina o una red, también podemos utilizar la librería para crear su celda unidad y celdas primitivas. Entre estas, se encuentra la celda de Wigner-Seitz.


#### Celdas unidad (CU) y Celdas primitiva(CP) 
Para crear una celda unidad o primitiva  solo se tiene que crear una red o una estructura cristalina a la cual se le hallara, para ello utilizar el metodo **cell**, el cual requiere de los siguientes parametros.

Si es para una red:

- **lattice** = nombre de la red creada.
- **vectors** = Lista que contiene los vectores de red que permitan la creacion de una CU o una CP, teniendo sus propiedades.

Si es para una estructura cristalina:

- **crystalStructure** = nombre de la estructura cristalina creada.
- **vectors** = Lista que contiene los vectores de red que permitan la creacion de una CU o una CP, teniendo sus propiedades.


###### Ejemplo Aplicado a una red:
```python
#Libreria PySolidState
%matplotlib widget
from PySolidState.crystal_structure.lattice import Lattice
from PySolidState.crystal_structure.cell import Cell

#Se crea la red de Bravais en la cual se acomodara la base de atomos.
lattice = Lattice(system='cubic',structure_type='face_centered', dimension='3D')

# Se crea la celda unidad de la red creada
cell = Cell(lattice = lattice, vectors=[[1,0,0],[0,1,0],[0,0,1]])
cell.plot(show_points=False, legends = False, axes = False)
```
###### Ejemplo Aplicado a una Estructura Cristalina:

```python
#Libreria PySolidState
%matplotlib widget
from PySolidState.crystal_structure.lattice import Lattice
from PySolidState.crystal_structure.atom import Atom
from PySolidState.crystal_structure.base import Base
from PySolidState.crystal_structure.crystalStructure import CrystalStructure
from PySolidState.crystal_structure.cell import Cell

# Contruimos la red FCC

#nota: system = lattice_name_Bravais y zise = Tamaño red
lattice_FCC = Lattice(system='cubic',structure_type='face_centered', dimension='3D', zise = 2)

#Contruimos la base de atomos
atom1 = Atom(name='Zn 2+', size= 0.2, color= 'blue')
atom2 = Atom(name='S 2-', size= 0.3, color= 'green')
base_sulfurodezinc = Base(lattice_vectors= lattice.vectors, atoms=[[atom1, [0,0,0]],[atom2, [0.25,0.25,0.25]]], dimension='3D')

# Se contruye la estructura cristalina
crs_sulfurodezinc = CrystalStructure(lattice= lattice_FCC, base= base_sulfurodezinc, dimension='3D')
crs_sulfurodezinc.plot()

#nota: crystalStructure = crystal_structure_name_created y vectors = network vectors that define a CU.
cell = Cell(crystalStructure= crs_sulfurodezinc, vectors=[[1,0,0],[0,1,0],[0,0,1]])
cell.plot(show_points=False, legends = False, axes = False)
```
#### Celda de Wigner Seitz (WS)
Para crear una celda WS  solo se tiene que crear una red o una estructura cristalina a la cual se le hallara, para ello utilizar el metodo **cell**, el cual solo requerira del parametro **lattice** = nombre de la red creada o **crystalStructure** = nombre de la estructura cristalina creada.

###### Ejemplo Aplicado a una red:
```python
#Libreria PySolidState
%matplotlib widget
from PySolidState.crystal_structure.lattice import Lattice
from PySolidState.crystal_structure.cell import Cell

#Se crea la red de Bravais en la cual se acomodara la base de atomos.
lattice = Lattice(system='cubic',structure_type='face_centered', dimension='3D')

# Se crea la celda unidad de la red creada
cell = Cell(lattice = lattice)
cell.plot(show_points=False, legends = False, axes = False)
```
###### Ejemplo Aplicado a una Estructura Cristalina:
```python
#Libreria PySolidState
%matplotlib widget
from PySolidState.crystal_structure.lattice import Lattice
from PySolidState.crystal_structure.atom import Atom
from PySolidState.crystal_structure.base import Base
from PySolidState.crystal_structure.crystalStructure import CrystalStructure
from PySolidState.crystal_structure.cell import Cell

# Contruimos la red FCC

#nota: system = lattice_name_Bravais y zise = Tamaño red
lattice_FCC = Lattice(system='cubic',structure_type='face_centered', dimension='3D', zise = 2)

#Contruimos la base de atomos
atom1 = Atom(name='Zn 2+', size= 0.2, color= 'blue')
atom2 = Atom(name='S 2-', size= 0.3, color= 'green')
base_sulfurodezinc = Base(lattice_vectors= lattice.vectors, atoms=[[atom1, [0,0,0]],[atom2, [0.25,0.25,0.25]]], dimension='3D')

# Se contruye la estructura cristalina
crs_sulfurodezinc = CrystalStructure(lattice= lattice_FCC, base= base_sulfurodezinc, dimension='3D')
crs_sulfurodezinc.plot()

#nota: crystalStructure = crystal_structure_name_created y vectors = network vectors that define a CU.
cell = Cell(crystalStructure= crs_sulfurodezinc)
cell.plot(show_points=False, legends = False, axes = False)
```
**Nota**: A la hora de graficar se puede permitir o no la visualizacion de los puntos de red, las leyendas y los ejes.
