import shapefile as shp
import geopandas as gpd

def create_patches (n_x: int, n_y: int, file_directory: str):
    """
    create and saves a shapefile of a grid of polygons

    Parameters
    ----------
    n_x: int
        number of polygons in the x-axis
    n_y: int
        number of polygons in the y-axis
    file_directory: str
        the full directory of the saved file (must end in .shp)
    
    Returns
    -------
    geopandas object
        the geopandas objec read from the saved shapefile
    """
    w = shp.Writer(rf'{file_directory}')
    w.autoBalance = 1
    w.field('id')
    id = 0
    dist = 0

    for j in range(n_y):
        for i in range(n_x):
            id += 1
            vertices = []
            parts = []
            vertices.append([i + dist, j + dist])
            vertices.append([i + dist + 1, j + dist])
            vertices.append([i + dist + 1, j + dist + 1])
            vertices.append([i + dist, j + dist + 1])
            parts.append(vertices)
            w.poly(parts)
            w.record(id)
    
    w.close()
    temp = gpd.read_file(rf'{file_directory}')
    return(temp)


