import geopandas as gpd


def convert_geojson_to_shapefile(input_geojson, output_folder):
    # Read the GeoJSON file
    gdf = gpd.read_file(input_geojson)
    grdc_station_number = int(gdf["grdc_no"])

    # Save it as a Shapefile in the folder of the basin_id
    output_shapefile = output_folder + "/" + str(grdc_station_number)
    gdf.to_file(output_shapefile, driver='ESRI Shapefile')

    print(f"Shapefile saved to {output_shapefile}")


# Example usage
input_geojson = "geojsons/stationbasins.geojson"  # Change to your input file path
output_folder = "shapefiles"  # Change to your desired output directory (without extension)
convert_geojson_to_shapefile(input_geojson, output_folder)
