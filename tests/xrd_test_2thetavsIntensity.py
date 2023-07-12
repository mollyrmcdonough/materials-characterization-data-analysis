import mcda.xrd as xrd

filename = "data/example_data/xrd/XRD4_MBE1-230331A-MS_Gonio Pixcel.xrdml"
df = xrd.parsexrdml_2ThetavsIntensity(filename)
xrd.plot2ThetavsIntensity(df)
