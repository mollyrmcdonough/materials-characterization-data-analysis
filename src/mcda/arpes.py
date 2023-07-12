import igor

# Replace this with the path to your .ibw file
file_path = "data/example_data/arpes/ARP2_MBE1-210408A-MS_210415_1390V_05mm_8th/ZrTe2_on_Gr_post_anneal_gamma00018th Harmonic SR.ibw"

# Load the .ibw file
wave = igor.load(file_path)

# The returned object is a dictionary containing the wave's data and other information
data = wave["wData"]

print(data)
