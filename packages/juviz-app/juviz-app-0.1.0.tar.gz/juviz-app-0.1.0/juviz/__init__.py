from pathlib import Path

from paraview import simple    # noqa
from paraview.web import venv  # noqa - Required for loading the venv with trame when pvpython is used

from trame.app import get_server, dev
from trame_simput import get_simput_manager
from trame_vuetify.ui.vuetify import SinglePageWithDrawerLayout
from trame.widgets import vuetify, paraview, simput, html

from assets import asset_manager
from widgets import files, pipeline, algorithms, juviz_controller, settings
from pv_visualizer.app.ui import state_change, view_toolbox
from pv_visualizer.app.engine import initialize as initialize_paraview


COMPACT = {
    "dense": True,
    "hide_details": True,
}


# All the Panels that should be accessible in the Sidebar. Each entry must have the following values/functions:
#  - NAME: Name of the Panel for state storing (files, pipeline, etc.)
#  - ICON: Icon for the Button in the Toolbar
#  - ICON_STYLE: Dictionary with additional styles for the icon
#  - initialize(server): Initialize the State (Callbacks, etc.)
#  - create_panel(server): Create the Panel
# Available Panels
SIDEBAR_PANELS = [
    files,
    pipeline,
    algorithms,
    juviz_controller,
    settings,
]


def main(**kwargs):
    server = get_server()
    state, ctrl = server.state, server.controller
    initialize_paraview(server, [])

    # Add data to argparser
    server.cli.add_argument(
        "--data", help="Path to browse", dest="data", default=str(Path.home())
    )

    # Name and Icon
    state.trame__title = "Visualizer"
    state.trame__favicon = asset_manager.icon

    # Controller
    @ctrl.add("on_server_reload")
    def _reload():
        dev.reload(
            files,
            settings,
            state_change,
        )
    ctrl.on_data_change.add(ctrl.view_update)
    ctrl.on_data_change.add(ctrl.pipeline_update)

    # Init Components
    for m in state_change, *SIDEBAR_PANELS:
        m.initialize(server)

    # Init Simput
    simput_manager = get_simput_manager("pxm")
    simput_widget = simput.Simput(
        simput_manager,
        prefix="pxm",
        trame_server=server,
        ref="simput",
        query=("search", ""),
    )
    ctrl.pxm_apply = simput_widget.apply
    ctrl.pxm_reset = simput_widget.reset

    with SinglePageWithDrawerLayout(server, show_drawer=True, width=300) as layout:
        layout.root = simput_widget
        layout.title.set_text("Visualizer")

        with layout.icon as icon:
            html.Img(src=asset_manager.icon, height=40)
            icon.click = None

        # Toolbar
        with layout.toolbar as tb:
            tb.dense = True
            tb.clipped_right = True
            vuetify.VSpacer()
            vuetify.VTextField(
                v_show=("!!active_controls",),
                v_model=("search", ""),
                clearable=True,
                outlined=True,
                filled=True,
                rounded=True,
                prepend_inner_icon="mdi-magnify",
                style="max-width: 30vw;",
                **COMPACT,
            )
            vuetify.VSpacer()
            with vuetify.VBtnToggle(
                v_model=("active_controls", "files"),
                **COMPACT,
                outlined=True,
                rounded=True,
            ):
                for item in SIDEBAR_PANELS:
                    with vuetify.VBtn(value=item.NAME, **COMPACT):
                        vuetify.VIcon(item.ICON, **item.ICON_STYLE)

        # Drawer
        with layout.drawer as dr:
            dr.right = True
            for item in SIDEBAR_PANELS:
                item.create_panel(server)

        # Main content
        with layout.content:
            with vuetify.VContainer(fluid=True, classes="fill-height pa-0 ma-0"):
                view_toolbox.create_view_toolbox(server)
                html_view = paraview.VtkRemoteLocalView(
                    simple.GetRenderView() if simple else None,
                    interactive_ratio=("view_interactive_ratio", 1),
                    interactive_quality=("view_interactive_quality", 70),
                    mode="remote",
                    namespace="view",
                    style="width: 100%; height: 100%;",
                )
                ctrl.view_replace = html_view.replace_view
                ctrl.view_update = html_view.update
                ctrl.view_reset_camera = html_view.reset_camera
                ctrl.on_server_ready.add(ctrl.view_update)

    return server.start(**kwargs)


if __name__ == '__main__':
    main()
