from .saveplotcontext import SavePlotContext
from .utils import load_pickle, write_pickle
import saveplotcontext


VERSION = '1.0.5'


def set_skip_all_show_plots(skip: bool) -> None:
    """
    A global version of SavePlotContext.skip_show_plots which applies to all SavePlotContext instances. If set to True,
    overrides the value of skip_show_plots passed into the constructor of a SavePlotContext object

    Parameters
    ----------
    skip
        Whether or not to skip 'show' calls
    """
    saveplotcontext.skip_all_show_plots = skip