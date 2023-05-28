import transport_analysis_module as ppms
filename = 'Example Data/Transport Data/TRP4_MBE1-230327A-MS_RvsH_50K.dat'
min_field = -5
temperature, magnetic_field_df, bridge1_resistance_df, bridge2_resistance_df = ppms.RvsH_dat_file_import(filename)
fielddown, resistancedown, Hall_resistancedown, fieldup, resistanceup, Hall_resistanceup = ppms.get_RvsH_down_and_up(magnetic_field_df,bridge1_resistance_df,bridge2_resistance_df,min_field)
# FieldVals,RxxAvg, FinalRxx, RxyAvg, FinalRxy = ppms.sym_antisym_interpolation(fielddown, resistancedown, Hall_resistancedown, fieldup, resistanceup, Hall_resistanceup,min_field)
FixedField, RxxAvg, FinalRxx, RxyAvg, FinalRxy = ppms.interpolate_and_symmetrize(fielddown, resistancedown, Hall_resistancedown, fieldup, resistanceup, Hall_resistanceup)
ppms.Field_vs_Rxx_down_and_up(FixedField,RxxAvg,temperature,'TRP4_MBE1-230327A-MS_RvsH_50K')
ppms.Field_vs_Rxy_down_and_up(FixedField,RxyAvg,temperature,'TRP4_MBE1-230327A-MS_RvsH_50K')

ppms.updown_data_writer(fieldup, resistanceup, Hall_resistanceup, fielddown, resistancedown, Hall_resistancedown,'TRP4_MBE1-230327A-MS_RvsH_50K')
