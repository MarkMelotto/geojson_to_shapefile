import geopandas as gpd


def convert_station_basin_geojson_to_shapefile(input_geojson, output_folder, country):
    # Read the GeoJSON file
    gdf = gpd.read_file(input_geojson)
    # grdc_station_number = int(gdf["grdc_no"])

    # Save it as a Shapefile in the folder of the basin_id
    output_shapefile = output_folder + "/" + str(country)
    gdf.to_file(output_shapefile, driver='ESRI Shapefile')

    print(f"Shapefile saved to {output_shapefile}")


# Example usage
country = "Zimbabwe"
input_geojson = "geojsons/" + country + "/stationbasins.geojson"  # Change to your input file path
output_folder = "shapefiles/" + country  # Change to your desired output directory (without extension)
convert_station_basin_geojson_to_shapefile(input_geojson, output_folder, country)
