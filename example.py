import matplotlib.pyplot as plt
import nanoscope
from nanoscope import files
from nanoscope.constants import FORCE, METRIC, VOLTS, PLT_kwargs

i_chan = 0  # This will provide Nanoscope channel #1
with files.HoldCurveFile("ForceHold.spm") as file_:
    channel = file_[i_chan]
    # get timed data of channel
    ft_plot, ax_properties = channel.create_force_time_plot(METRIC)
    plt.plot(ft_plot.x, ft_plot.y)
    plt.gca().set(**ax_properties)  # set axes properties
    plt.show()

    hold_plot, ax_properties = channel.create_force_hold_time_plot(METRIC)
    plt.plot(hold_plot.x, hold_plot.y)
    plt.gca().set(**ax_properties)  # set axes properties
    plt.show()