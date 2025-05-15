import geopandas as gpd
import matplotlib.pyplot as plt


def save_shapefile_catchments(input_big_shapefile, output_folder):
    shape=gpd.read_file(input_big_shapefile)

    # print(shape)
    grdcs = shape['grdc_no']
    # print(len(grdcs))
    print("Starting process to divide the big shapefile")
    count = 1
    for grdc in grdcs:
        to_plot = shape[shape['grdc_no'] == grdc]
        # to_plot.plot()
        # plt.show()
        output_shapefile = output_folder + "/" + "AF_" + str(int(grdc))
        # output_shapefile = output_folder + "/" + "AF"

        to_plot.to_file(output_shapefile, driver='ESRI Shapefile')
        print(f"Saved {int(count)}/{int(len(grdcs))}")
        count += 1
    print("Finished process to divide the big shapefile")


if __name__ == '__main__':
    input_big_shapefile = 'shapefiles/Zimbabwe/Zimbabwe.shp'
    output_folder = 'shapefiles/all_Zimbabwe'

    save_shapefile_catchments(input_big_shapefile,output_folder)