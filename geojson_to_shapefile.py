import geopandas as gpd


def convert_geojson_to_shapefile(input_geojson, output_shapefile):
    # Read the GeoJSON file
    gdf = gpd.read_file(input_geojson)

    # Save it as a Shapefile
    gdf.to_file(output_shapefile, driver='ESRI Shapefile')

    print(f"Shapefile saved to {output_shapefile}")


# Example usage
input_geojson = "geojsons/stationbasins.geojson"  # Change to your input file path
output_shapefile = "shapefiles/output_shapefile"  # Change to your desired output directory (without extension)
convert_geojson_to_shapefile(input_geojson, output_shapefile)
