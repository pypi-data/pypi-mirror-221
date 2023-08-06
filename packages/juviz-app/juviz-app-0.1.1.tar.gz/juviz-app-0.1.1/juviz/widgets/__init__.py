# Panels
from pv_visualizer.app.ui import algorithms, files, pipeline, settings
from . import juviz_controller

# Widgets
from pv_visualizer.html.data_information import DataInformation
from pv_visualizer.html.file_browser import ParaViewFileBrowser
from pv_visualizer.html.filters import Algorithms
from pv_visualizer.html.pipeline import PipelineBrowser
from pv_visualizer.html.proxy_editor import ProxyEditor

__all__ = [
    # Panels
    algorithms,
    files,
    juviz_controller,
    pipeline,
    settings,

    # Widgets
    DataInformation,
    ParaViewFileBrowser,
    Algorithms,
    PipelineBrowser,
    ProxyEditor
]
