import mcda.afm as afm

filename = "data/example_data/afm/MBE1-230404A-MS.0_00000.spm"
#Imports SPM file
scan, topo = afm.importBrukerAFMData(filename)
#Shows image
afm.showHeightSensor(topo)
scanSize = 5
scanSizeLabel = 'um'
#Show plane corrected image
afm.showHeightSensorCorrected(topo, scanSize, scanSizeLabel)