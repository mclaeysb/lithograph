import mapnik
import xml.etree.ElementTree as ET

# set map width
width = 2**10

# load fonts
custom_fonts_dir = 'font'
mapnik.register_fonts(custom_fonts_dir)

# mapnik XML as object
mapnik_xml = ET.parse('cassini.xml')

# get values from XML
map_srs = mapnik_xml.getroot().attrib['srs']
param_center = mapnik_xml.getroot().findall("./Parameters/Parameter[@name='center']")[0].text
param_center_x, param_center_y, param_zoom = [float(i) for i in param_center.split(',')]

# map projection
map_proj = mapnik.Projection(map_srs)
# WGS84 projection
wgs84_proj = mapnik.Projection('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')

# make map object
m = mapnik.Map(width,width)
mapnik.load_map(m, 'cassini.xml')

# set center point
wgs84_proj_center = mapnik.Coord(param_center_x,param_center_y)  
transform = mapnik.ProjTransform(wgs84_proj, map_proj)
map_proj_center = transform.forward(wgs84_proj_center)

# m.zoom_all()

bounds = mapnik.Box2d(146304.91,6388064.94,507792.46,6679144.51)
m.zoom_to_box(bounds)

# m.pan_and_zoom(int(map_proj_center.x),int(map_proj_center.y),param_zoom)
mapnik.render_to_file(m, 'the_image.png')