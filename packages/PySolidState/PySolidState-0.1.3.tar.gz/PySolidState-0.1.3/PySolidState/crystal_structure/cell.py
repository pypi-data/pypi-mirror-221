from PySolidState.crystal_structure.lattice import Lattice
from PySolidState.crystal_structure.crystalStructure import CrystalStructure
from PySolidState.crystal_structure.base import Base
from PySolidState.crystal_structure.atom import Atom


import numpy as np
import itertools
import mayavi.mlab
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.patches as patches
import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerPatch
from scipy.spatial import ConvexHull, Delaunay
from matplotlib import colors





class Cell:
    def __init__(self, lattice: Lattice = None, crystalStructure: CrystalStructure = None, vectors: list = None) -> None:

        self.vectors = vectors
        self.__crystalStructure = crystalStructure

        if lattice is not None:
            self.__lattice = lattice

        elif crystalStructure is not None:
            self.__lattice = crystalStructure.lattice
            self.__base = crystalStructure.base
        else:
            raise ValueError(
                "You must provide either a 'lattice' or a 'crystalStructure'.")

        self.__points = self.__lattice.points
        self.dimension = self.__lattice.dimension
        self.__structure_type = self.__lattice.structure_type
        self.__system = self.__lattice.system

    def plot(self, show_points=True, legends = True, axes = True):
        # Se crea la celda a partir de los vectores
        if self.vectors is not None:
            if self.dimension == '2D':
                points = self._generate_polygon_points(self.vectors)  # Calcular los puntos


                fig = plt.figure(figsize=(6, 6))
                ax = fig.add_subplot(111, aspect='equal')

                ax.add_patch(Polygon(points, closed=True, edgecolor='blue',
                             facecolor='blue', linewidth=4.0, fill=True, alpha=0.3))

                ax.scatter(
                    self.__points[:, 0], self.__points[:, 1], color='black', label='Points')
                
                # Graficar los atomos
                if self.__crystalStructure is not None:
                    atoms = []
                    for point in self.__lattice.points:
                        for atom in self.__base.atoms:
                            new_position =  list(np.array(atom[1]) + np.array(point))
                            new_atom = [atom[0], new_position]
                            atoms.append(new_atom)

                    handles, labels = ax.get_legend_handles_labels()
                    unique_atom_names = set(labels)

                    for atom in self.__base.atoms:
                        atom_name = atom[0].name
                        circle = patches.Circle((atom[1][0], atom[1][1]), radius=atom[0].size, facecolor=atom[0].color, edgecolor=atom[0].color, alpha=0.5, label=atom_name)
                        if atom_name not in unique_atom_names:
                            handles.append(circle)
                            labels.append(atom_name)
                            unique_atom_names.add(atom_name)

                    ax.legend(handles, labels, loc='upper right', handlelength=1, handletextpad=1,handler_map={mpatches.Circle: self._HandlerCircle(radius = 2)},borderpad = 0.8)
                    # Graficar los atomos
                    for atom in atoms:
                        atom_name = atom[0].name
                        circle = patches.Circle((atom[1][0], atom[1][1]), radius=atom[0].size, facecolor=atom[0].color, edgecolor=atom[0].color, alpha=0.5, label=atom_name)
                        ax.add_artist(circle)
                
                ax.quiver(0, 0, self.__lattice.vectors[0][0], self.__lattice.vectors[0][1],  angles='xy', scale_units='xy', scale=1, color='black')
                ax.quiver(0, 0, self.__lattice.vectors[1][0], self.__lattice.vectors[1][1],  angles='xy', scale_units='xy', scale=1, color='black')

                # Show the names of the vectors
                ax.text(self.__lattice.vectors[0][0] + 0.3, self.__lattice.vectors[0][1], r"$\vec{a_1}$", fontsize=12, color='black', ha='center', va='center')
                ax.text(self.__lattice.vectors[1][0], self.__lattice.vectors[1][1] + 0.3, r"$\vec{a_2}$", fontsize=12, color='black', ha='center', va='center')

                ax.set_aspect('equal')
                ax.set_xlim(- 3, 3)
                ax.set_ylim(- 3, 3)
                ax.axis('off')  # Disable reference axes

                plt.show()

            elif self.dimension == '3D':
                poly_vertices ,points_list = self._generate_polygon_points(self.vectors)  #Puntos el poliedro y puntos por cara del poliedro
                
 

                mayavi.mlab.figure(bgcolor=(1, 1, 1))

                if self.__crystalStructure is not None:
                    # Calcular los puntos dentro de la celda
                    atoms = []
                    for point in self.__lattice.points:
                        for atom in self.__base.atoms:
                            new_position =  list(np.array(atom[1]) + np.array(point))
                            if self._is_point_inside_polyhedron(np.array(new_position), poly_vertices):
                                new_atom = [atom[0], new_position]
                                atoms.append(new_atom)

                    unique_atom_names = []
                    count = 0
                    for atom in atoms:
                        self._plot_sphere(atom[1][0],atom[1][1],atom[1][2], r=atom[0].size, color_name= atom[0].color )
                        # Mostraar los nombres de los atomos
                        if legends == True:
                            if atom[0].name not in unique_atom_names:
                                unique_atom_names.append(atom[0].name)
                                self._plot_sphere(2,2.5,2.5-count, r=atom[0].size, color_name= atom[0].color )
                                mayavi.mlab.text3d(2,2.5+atom[0].size,2.5-atom[0].size -count, atom[0].name, color=(0, 0, 0), scale=0.1)

                                count += 2* atom[0].size

                for points in points_list:
                    # Obtener las coordenadas X, Y, Z de los puntos
                    x_points, y_points, z_points = points[:,
                                                          0], points[:, 1], points[:, 2]

                    # Calcular el punto central del hexágono
                    central_point = np.mean(points, axis=0)

                    # Crear una lista de triángulos conectando el punto central con los puntos adyacentes
                    triangles = [[i, (i+1) % len(points), len(points)]
                                 for i in range(len(points))]

                    # Agregar el punto central al final de las listas de coordenadas
                    x_points = np.append(x_points, central_point[0])
                    y_points = np.append(y_points, central_point[1])
                    z_points = np.append(z_points, central_point[2])

                    # Puntos para formar las lineas
                    x_lines = np.append(points[:, 0], points[:, 0][0])
                    y_lines = np.append(points[:, 1], points[:, 1][0])
                    z_lines = np.append(points[:, 2], points[:, 2][0])

                    # Dibujar las lineas
                    mayavi.mlab.plot3d(x_lines, y_lines, z_lines, color=(
                        0, 0, 0), tube_radius=0.008)

                    if show_points:
                        # Dibujar los puntos de la lattice
                        mayavi.mlab.points3d(self.__points[:, 0], self.__points[:, 1], self.__points[:, 2], mode="sphere", color=(
                            0, 0, 0,), scale_factor=0.1)
                    
                    # Dibujar los vectores
                    if axes == True:
                        for vector in self.__lattice.vectors:
                            mayavi.mlab.quiver3d(
                                0, 0, 0, vector[0], vector[1], vector[2], color=(0, 0, 0), scale_factor=1)

                        mayavi.mlab.text3d(self.__lattice.vectors[0][0], self.__lattice.vectors[0]
                                        [1], self.__lattice.vectors[0][2], 'a1', color=(0, 0, 0), scale=0.1)
                        mayavi.mlab.text3d(self.__lattice.vectors[1][0], self.__lattice.vectors[1]
                                        [1], self.__lattice.vectors[1][2], 'a2', color=(0, 0, 0), scale=0.1)
                        mayavi.mlab.text3d(self.__lattice.vectors[2][0], self.__lattice.vectors[2]
                                        [1], self.__lattice.vectors[2][2], 'a3', color=(0, 0, 0), scale=0.1)

                    # Dibujar la malla para formar el hexágono completo
                    mayavi.mlab.triangular_mesh(
                        x_points, y_points, z_points, triangles, color=(0, 0.3, 0.6), opacity=0.5)

                # Mostrar la figura con todos los conjuntos de puntos
                mayavi.mlab.show()

        # Se crea la celda de Wigner Seitz
        else:
            if self.dimension == '2D':
                reference_point = np.array([0, 0])
                points = self._find_nearest_neighbors(self.__points, 3)[:, :2]

                lines1, intersection_points = self._construct_wigner2D(
                    points, reference_point)
                nearest_intersection = self._find_nearest_neighbors(
                    list(intersection_points.keys()), 1)
                nearest_intersection = self._sort_points_clockwise(
                    nearest_intersection)

                lines = []
                for point in nearest_intersection:
                    for line in intersection_points[tuple(point)]:
                        lines.append(line)

                fig = plt.figure(figsize=(6, 6))
                ax = fig.add_subplot(111, aspect='equal')
                for line in lines:
                    ax.plot([line[0][0], line[1][0]], [
                            line[0][1], line[1][1]], color='black', ls='--')

                ax.add_patch(Polygon(nearest_intersection, closed=True, edgecolor='blue',
                             facecolor='blue', linewidth=4.0, fill=True, alpha=0.3))

                ax.scatter(
                    self.__points[:, 0], self.__points[:, 1], color='black', label='Points')
                
                # Graficar los atomos
                if self.__crystalStructure is not None:
                    atoms = []
                    for point in self.__lattice.points:
                        for atom in self.__base.atoms:
                            new_position =  list(np.array(atom[1]) + np.array(point))
                            new_atom = [atom[0], new_position]
                            atoms.append(new_atom)

                    handles, labels = ax.get_legend_handles_labels()
                    unique_atom_names = set(labels)

                    for atom in self.__base.atoms:
                        atom_name = atom[0].name
                        circle = patches.Circle((atom[1][0], atom[1][1]), radius=atom[0].size, facecolor=atom[0].color, edgecolor=atom[0].color, alpha=0.5, label=atom_name)
                        if atom_name not in unique_atom_names:
                            handles.append(circle)
                            labels.append(atom_name)
                            unique_atom_names.add(atom_name)

                    ax.legend(handles, labels, loc='upper right', handlelength=1, handletextpad=1,handler_map={mpatches.Circle: self._HandlerCircle(radius = 2)},borderpad = 0.8)
                    # Graficar los atomos
                    for atom in atoms:
                        atom_name = atom[0].name
                        circle = patches.Circle((atom[1][0], atom[1][1]), radius=atom[0].size, facecolor=atom[0].color, edgecolor=atom[0].color, alpha=0.5, label=atom_name)
                        ax.add_artist(circle)
                
                ax.quiver(0, 0, self.__lattice.vectors[0][0], self.__lattice.vectors[0][1],  angles='xy', scale_units='xy', scale=1, color='black')
                ax.quiver(0, 0, self.__lattice.vectors[1][0], self.__lattice.vectors[1][1],  angles='xy', scale_units='xy', scale=1, color='black')

                # Show the names of the vectors
                ax.text(self.__lattice.vectors[0][0] + 0.3, self.__lattice.vectors[0][1], r"$\vec{a_1}$", fontsize=12, color='black', ha='center', va='center')
                ax.text(self.__lattice.vectors[1][0], self.__lattice.vectors[1][1] + 0.3, r"$\vec{a_2}$", fontsize=12, color='black', ha='center', va='center')
                #ax.scatter(reference_point[0], reference_point[1], color='blue', label='Reference Point')
                ax.set_aspect('equal')
                ax.set_xlim(- 3, 3)
                ax.set_ylim(- 3, 3)
                ax.axis('off')  # Disable reference axes

                plt.show()

            elif self.dimension == '3D':
                points_nearest = self._find_nearest_neighbors(self.__points, 3)
                if self.__structure_type == 'base_centered':
                    points_nearest = self._find_nearest_neighbors(
                        self.__points, 10)

                 # Tomar hasta los terceros puntos de la red más cercanos #10

                poly_vertices,points_list = self._find_intersections(points_nearest, 1) #  poly_vertices
                if len(points_list) == 0:
                    poly_vertices,points_list = self._find_intersections(points_nearest, 2)


                mayavi.mlab.figure(bgcolor=(1, 1, 1))

                if self.__crystalStructure is not None:
                    # Calcular los puntos dentro de la celda
                    atoms = []
                    for point in self.__lattice.points:
                        for atom in self.__base.atoms:
                            new_position =  list(np.array(atom[1]) + np.array(point))
                            if self._is_point_inside_polyhedron(np.array(new_position), poly_vertices):
                                new_atom = [atom[0], new_position]
                                atoms.append(new_atom)

                    unique_atom_names = []
                    count = 0
                    for atom in atoms:
                        self._plot_sphere(atom[1][0],atom[1][1],atom[1][2], r=atom[0].size, color_name= atom[0].color )
                        # Mostraar los nombres de los atomos
                        if legends == True:
                            if atom[0].name not in unique_atom_names:
                                unique_atom_names.append(atom[0].name)
                                self._plot_sphere(2,2.5,2.5-count, r=atom[0].size, color_name= atom[0].color )
                                mayavi.mlab.text3d(2,2.5 +atom[0].size,2.5-atom[0].size -count, atom[0].name, color=(0, 0, 0), scale=0.1)

                                count += 2* atom[0].size

                for points in points_list:
                    # Obtener las coordenadas X, Y, Z de los puntos
                    x_points, y_points, z_points = points[:,
                                                          0], points[:, 1], points[:, 2]

                    # Calcular el punto central del hexágono
                    central_point = np.mean(points, axes=0)

                    # Crear una lista de triángulos conectando el punto central con los puntos adyacentes
                    triangles = [[i, (i+1) % len(points), len(points)]
                                 for i in range(len(points))]

                    # Agregar el punto central al final de las listas de coordenadas
                    x_points = np.append(x_points, central_point[0])
                    y_points = np.append(y_points, central_point[1])
                    z_points = np.append(z_points, central_point[2])

                    # Puntos para formar las lineas
                    x_lines = np.append(points[:, 0], points[:, 0][0])
                    y_lines = np.append(points[:, 1], points[:, 1][0])
                    z_lines = np.append(points[:, 2], points[:, 2][0])

                    # Dibujar las lineas
                    mayavi.mlab.plot3d(x_lines, y_lines, z_lines, color=(
                        0, 0, 0), tube_radius=0.008)

                    # Dibujar puntos de la red
                    if show_points == True:
                        mayavi.mlab.points3d(self.__points[:, 0], self.__points[:, 1], self.__points[:, 2], mode="sphere", color=(
                            0, 0, 0,), scale_factor=0.1)
                    
                    # Dibujar los vectores
                    if axes == True: 
                        for vector in self.__lattice.vectors:
                            mayavi.mlab.quiver3d(
                                0, 0, 0, vector[0], vector[1], vector[2], color=(0, 0, 0), scale_factor=1)

                        mayavi.mlab.text3d(self.__lattice.vectors[0][0], self.__lattice.vectors[0]
                                        [1], self.__lattice.vectors[0][2], 'a1', color=(0, 0, 0), scale=0.2)
                        mayavi.mlab.text3d(self.__lattice.vectors[1][0], self.__lattice.vectors[1]
                                        [1], self.__lattice.vectors[1][2], 'a2', color=(0, 0, 0), scale=0.2)
                        mayavi.mlab.text3d(self.__lattice.vectors[2][0], self.__lattice.vectors[2]
                                        [1], self.__lattice.vectors[2][2], 'a3', color=(0, 0, 0), scale=0.2)

                    # Dibujar la malla para formar el hexágono completo
                    mayavi.mlab.triangular_mesh(
                        x_points, y_points, z_points, triangles, color=(0, 0.3, 0.6), opacity=0.5)

                # Mostrar la figura con todos los conjuntos de puntos
                mayavi.mlab.show()

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

    def _is_point_inside_polyhedron(self,point, poly_vertices):
        hull = ConvexHull(poly_vertices)
        hull_tri = Delaunay(poly_vertices[hull.vertices])
        return hull_tri.find_simplex([point]) >= 0

    def _generate_polygon_points(self, vectors: list[np.array]) -> list[np.array]:
        if len(vectors) == 2:  # 2D - Create a square
            # Ignore the third component (z-axis) since we are working in R2
            vector1 = vectors[0]
            vector2 = vectors[1]

            # Find the four vertices of the square
            vertex1 = np.array([0, 0, 0])
            vertex2 = vertex1 + vector1
            vertex3 = vertex2 + vector2
            vertex4 = vertex1 + vector2

            # Create an array with the four vertices
            points = np.array([vertex1, vertex2, vertex3, vertex4])

            polygon_points = []
            for point in points:
                new_point = np.dot(point, self.__lattice.vectors)[:2]
                polygon_points.append(new_point)

        elif len(vectors) == 3:  # 3D - Create a cube
            # No need to ignore any component in 3D
            vector1 = vectors[0]
            vector2 = vectors[1]
            vector3 = vectors[2]

            # Find the eight vertices of the cube
            vertex1 = np.array([0, 0, 0])
            vertex2 = vertex1 + vector1
            vertex3 = vertex2 + vector2
            vertex4 = vertex1 + vector2
            vertex5 = vertex1 + vector3
            vertex6 = vertex2 + vector3
            vertex7 = vertex3 + vector3
            vertex8 = vertex1 + vector3 + vector2

            points = [vertex1, vertex2, vertex3, vertex4,
                      vertex5, vertex6, vertex7, vertex8]
            faces_indices = [
                [0, 1, 2, 3],  # Cara 1
                [0, 1, 5, 4],  # Cara 2
                [1, 2, 6, 5],  # Cara 3
                [0, 3, 7, 4],  # Cara 4
                [2, 3, 7, 6],  # Cara 5
                [4, 5, 6, 7]   # Cara 6
            ]

            new_points = []
            for point in points:
                new_point = np.dot(point, self.__lattice.vectors)
                new_points.append(new_point)

            polygon_points = []
            for face in faces_indices:
                points_face = []
                for index in face:
                    points_face.append(new_points[index])
                polygon_points.append(np.array(points_face))

        else:
            raise ValueError(
                "The function supports 2D (two vectors) and 3D (three vectors) only.")

        return np.array(new_points),polygon_points


    def _plot_sphere(self,x_0, y_0, z_0, r=0.5, color_name='red'):
        """
        Plot a sphere in 3D space.

        Args:
            x_0 (float): x-coordinate of the sphere's center.
            y_0 (float): y-coordinate of the sphere's center.
            z_0 (float): z-coordinate of the sphere's center.
            r (float, optional): Radius of the sphere. Default is 0.5.
            color_name (str, optional): Color of the sphere. Default is 'red'.

        Returns:
            None
        """
        phi, theta = np.mgrid[0:2 * np.pi:75j, 0:np.pi:75j]
        x = r * np.cos(phi) * np.sin(theta) + x_0
        y = r * np.sin(phi) * np.sin(theta) + y_0
        z = r * np.cos(theta) + z_0
        rgb = self._get_rgb(color_name)
        mayavi.mlab.mesh(x, y, z, color=rgb, opacity=1)

    def _get_rgb(self, color_name):
        """
        Get the RGB color values from a color name.

        Args:
            color_name (str): Name of the color.

        Returns:
            tuple: RGB color values as a tuple (red, green, blue).

        Raises:
            KeyError: If the color name is not found in the color dictionary.
        """
        hex_color = colors.cnames[color_name]
        rgb_color = colors.hex2color(hex_color)
        return rgb_color

# -----------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------


    def _line_intersection(self, line1, line2):
        x1, y1 = line1[0]
        x2, y2 = line1[1]
        x3, y3 = line2[0]
        x4, y4 = line2[1]
        # Calcular las coordenadas de la intersección
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator != 0:
            x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2)
                 * (x3 * y4 - y3 * x4)) / denominator
            y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2)
                 * (x3 * y4 - y3 * x4)) / denominator
            return round(x, 5), round(y, 5)
        else:
            return None

    def _perpendicular_line(self, line):
        x1, y1 = line[0]
        x2, y2 = line[1]

        l = 1.2
        if (self.__system == 'rectangular') and (self.__structure_type != 'centered'):
            l = 2.2
        # Calcular el punto medio de la línea
        midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

        # Calcular la longitud de la línea perpendicular como el doble de la longitud de la línea original
        perpendicular_length = 2 * np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # Calcular los puntos iniciales y finales de la línea perpendicular
        dx = (y2 - y1) / perpendicular_length
        dy = (x1 - x2) / perpendicular_length
        perpendicular_start = (midpoint[0] - l * dx, midpoint[1] - l * dy)
        perpendicular_end = (midpoint[0] + l * dx, midpoint[1] + l * dy)

        return [perpendicular_start, perpendicular_end]

    def _sort_points_clockwise(self, points):
        if len(points[0]) == 2:
            reference_point = np.array([0, 0])
        angles = np.arctan2(
            points[:, 1] - reference_point[1], points[:, 0] - reference_point[0])
        sorted_indices = np.argsort(angles)
        sorted_points = points[sorted_indices]
        return sorted_points

    def _construct_wigner2D(self, points: list, reference_point: np.array):
        # Calcular las distancias desde el punto de referencia a todos los demás puntos
        distances = np.linalg.norm(points - reference_point, axis=1)

        # Encontrar los índices de los puntos más cercanos
        # Excluye el punto de referencia
        nearest_indices = np.argsort(distances)

        # Obtener los vectores que conectan el punto de referencia con los puntos más cercanos
        vectors = (points[nearest_indices] - reference_point)

        # Calcular los ángulos entre los vectores y ordenarlos en sentido horario
        angles = np.arctan2(vectors[:, 1], vectors[:, 0])
        sorted_indices = np.argsort(angles)

        # Obtener los vectores ordenados en sentido horario
        sorted_vectors = vectors[sorted_indices]

        lines = []
        for vector in sorted_vectors:
            line = self._perpendicular_line([reference_point, vector])
            lines.append(line)

        points_intersection = {}

        for i in range(len(lines)):
            for j in range(i+1, len(lines)):
                line1 = lines[i]
                line2 = lines[j]

                point_intersection = self._line_intersection(line1, line2)

                if point_intersection in list(points_intersection.keys()):
                    points_intersection[point_intersection].append(line1)
                    points_intersection[point_intersection].append(line2)
                else:
                    points_intersection[point_intersection] = [line1, line2]

        if None in list(points_intersection.keys()):
            del points_intersection[None]
        return lines, points_intersection
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

    def _find_nearest_neighbors(self, points: np.array([list]), k: int) -> np.array([list]):
        """Esta función calcula los *primeros vecinos*, para esto usa los vecinos más cercanos y los siguientes"""

        distances = {}  # Diccionario para guardar las distancias a cada punto, donde la llave será la distancia y el valor el punto
        if len(points[0]) == 2:
            initial_point = np.array([0, 0])
        else:
            initial_point = np.array([0, 0, 0])  # Punto de referencia

        for point in points:  # Calculo de las distancias
            distance = round(np.linalg.norm(
                point - initial_point), 2)  # Calcula la norma
            if distance > 0:  # Para el punto de referencia pues es cero, entonces no lo tengo en cuenta
                if distance in distances:  # Si ya hay una distancia como esa entonces agrega a esa llave
                    distances[distance].append(list(point))
                else:  # Sino lo hace por primera vez
                    distances[distance] = [list(point)]

        # Ordena las distancias y toma las dos más cortas
        minimal_distances = sorted(distances.keys())[:k]
        nearest_neighbors = []

        # Obtiene los puntos a los que corresponde dicha distancia
        for distance in minimal_distances:
            nearest_neighbors.extend(distances[distance])

        nearest_neighbors = np.array(nearest_neighbors)

        return nearest_neighbors

    def _change_to_2d_coordinates(self, points):
        # Encuentra el centroide
        centroid = np.mean(points, axis=0)

        # Encuentra el vector normal al plano
        normal_vector = np.cross(points[1] - points[0], points[2] - points[0])

        # Normaliza el vector normal
        normal_vector /= np.linalg.norm(normal_vector)

        # Elige un vector arbitrario v1
        v1 = points[0] - centroid

        # Calcula v2 como el producto cruz entre v1 y el vector normal
        v2 = np.cross(v1, normal_vector)

        # Calcula v3 como el producto cruz entre el vector normal y v2
        v3 = np.cross(normal_vector, v2)

        # Normaliza v1, v2 y v3
        v1 /= np.linalg.norm(v1)
        v2 /= np.linalg.norm(v2)
        v3 /= np.linalg.norm(v3)

        # Proyecta los puntos en los vectores v1 y v2 para obtener las coordenadas 2D
        coordinates_2d = np.array(
            [(np.dot(point - centroid, v1), np.dot(point - centroid, v2)) for point in points])

        return coordinates_2d

    def _sort_points_3d(self, points_3d):
        # Convertir los puntos 3D a 2D
        points_2d = self._change_to_2d_coordinates(points_3d)

        # Ordenar los puntos en 2D y obtener los índices de ordenamiento
        reference_point = points_2d[0]
        angles = np.arctan2(
            points_2d[:, 1] - reference_point[1], points_2d[:, 0] - reference_point[0])
        sorted_indices = np.argsort(angles)

        # Ordenar los puntos en 3D utilizando el mismo orden que en 2D
        sorted_points_3d = points_3d[sorted_indices]

        return sorted_points_3d

    # Calcular el punto de intersección entre tres planos
    def _calculate_intersection_point(self, plane1, plane2, plane3):
        # Vectores normales a los planos
        norm1 = np.array(plane1)
        norm2 = np.array(plane2)
        norm3 = np.array(plane3)

        point1 = norm1 / 2  # Punto en plano
        point2 = norm2 / 2  # Punto en plano
        point3 = norm3 / 2  # Punto en plano

        d1 = np.dot(norm1, point1)
        d2 = np.dot(norm2, point2)
        d3 = np.dot(norm3, point3)

        A = np.array([[norm1[0], norm1[1], norm1[2]], [
            norm2[0], norm2[1], norm2[2]], [norm3[0], norm3[1], norm3[2]]])
        b = np.array([d1, d2, d3])

        try:
            intersection_point = np.linalg.solve(A, b)
            return intersection_point
        except np.linalg.LinAlgError:
            # El sistema de ecuaciones no tiene solución o tiene infinitas soluciones
            return None

    def _find_intersections(self, points, n):
        points = np.round(points, 3)
        intersections = {}

        # Generar todas las combinaciones únicas de 3 puntos
        combinations = itertools.combinations(points, 3)
        for combination in combinations:
            intersection = self._calculate_intersection_point(*combination)
            if intersection is not None:
                for plane in combination:
                    if str(plane.tolist()) not in list(intersections.keys()):
                        intersections[str(plane.tolist())] = [intersection]
                    else:
                        intersections[str(plane.tolist())].append(intersection)

        p = self._find_nearest_neighbors(
            list(itertools.chain.from_iterable(intersections.values())), n)

        unique_points = []
        for point in p:
            if not any(np.allclose(point, unique_point) for unique_point in unique_points):
                unique_points.append(point)

        final_points = {}
        for key in intersections.keys():
            points_in_plane = list(intersections[key])
            points_to_keep = []
            for point in unique_points:
                is_in_list = any(np.all(np.isclose(point, p))
                                 for p in points_in_plane)
                if is_in_list:
                    points_to_keep.append(list(point))

            final_points[key] = points_to_keep

        poligon_points = []
        for key_ in list(final_points.keys()):
            if len(final_points[key_]) >= 4:
                poligon_point = self._sort_points_3d(
                    np.array(final_points[key_]))
                poligon_points.append(poligon_point)

        return  np.array(unique_points),poligon_points
    
    class _HandlerCircle(HandlerPatch):
        def __init__(self, radius=5, **kwargs):
            self.radius = radius
            super().__init__(**kwargs)

        def create_artists(self, legend, orig_handle,
                        xdescent, ydescent, width, height, fontsize, trans):
            center_x = xdescent + width / 2
            center_y = ydescent + height / 2
            radius = min(width, height) / 2 * self.radius
            circle = mpatches.Circle((center_x, center_y), radius, facecolor=orig_handle.get_facecolor(),
                                    edgecolor=orig_handle.get_edgecolor(), linewidth=orig_handle.get_linewidth())
            self.update_prop(circle, orig_handle, legend)
            circle.set_transform(trans)
            return [circle]


