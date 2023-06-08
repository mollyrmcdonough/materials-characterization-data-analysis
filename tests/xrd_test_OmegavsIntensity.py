import mcda.xrd as xrd

filename = 'data/example_data/xrd/XRD4_MBE1-230331A-MS_33.9475 Omega.xrdml'
df = xrd.parsexrdml_OmegavsIntensity(filename)
xrd.plotOmegavsIntensity(df)