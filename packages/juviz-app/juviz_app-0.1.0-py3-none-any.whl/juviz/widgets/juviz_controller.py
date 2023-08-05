from aiohttp.web import Application, Request, StreamResponse, HTTPOk, HTTPBadRequest
from paraview import servermanager  # noqa

from trame.widgets import html, vuetify

NAME = "juviz-controller"
ICON = "mdi-eye-settings"
ICON_STYLE = {}

COMPACT = {
    "dense": True,
    "hide_details": True,
}


# Store the Catalyst Connection when we open Catalyst
_catalyst_connection = None


def initialize(server):
    state, ctrl = server.state, server.controller

    state.server_connection = None
    state.catalyst_connection = False

    def connect(url, port=11111):
        print(f"Connecting to {url}:{port}")
        servermanager.Connect(url, port)
        state.server_connection = f"{url}:{port}"

    def disconnect():
        print("Disconnecting")
        servermanager.Disconnect()
        state.server_connection = None

    def open_catalyst():
        print("Openning Catalyst")
        global _catalyst_connection
        _catalyst_connection = servermanager.ConnectToCatalyst()
        state.catalyst_connection = True

    def close_catalyst():
        print("Closing Catalyst")
        global _catalyst_connection
        if _catalyst_connection is not None:
            print("Closing Catalyst:")
            print(dir(_catalyst_connection))
        else:
            raise HTTPBadRequest()

    ctrl.connect_to_server = connect
    ctrl.disconnect_from_server = disconnect
    ctrl.open_catalyst = open_catalyst
    ctrl.close_catalyst = close_catalyst

    @ctrl.add("on_server_bind")
    def add_routes(aiohttp_server: Application):
        # Define Handler for the JuViz Route
        async def handle(request: Request) -> StreamResponse:
            global _catalyst_connection

            data: dict = await request.json()
            print(f"Received JuViz Request: {data = }")
            action = data["action"].lower()

            if action == "connect":
                connect(data["url"], int(data.get("port", 11111)))
            elif action == "disconnect":
                disconnect()
            elif action == "open_catalyst":
                open_catalyst()
            elif action == "close_catalyst":
                close_catalyst()

            return HTTPOk()

        # Create route
        aiohttp_server.router.add_post("/juviz", handle)


def create_panel(server):
    state, ctrl = server.state, server.controller

    # Wrapper to get the values from the state
    def _connect():
        ctrl.connect_to_server(state.juviz_server_url, int(state.juviz_server_port))

    with vuetify.VCol(v_if=(f"active_controls == '{NAME}'",), classes="mx-0 pa-0", **COMPACT):
        # Show Server Connection status
        with vuetify.VCard(classes="pa-0", flat=True, outlined=False, tile=True):
            vuetify.VDivider()
            with vuetify.VCardTitle(classes="d-flex align-center py-1"):
                html.Div("ParaView Server Connection")

            vuetify.VDivider()

            # Connection exists
            with vuetify.VCardText(v_if=("server_connection",)):
                html.Div(f"Connected to Server on '{state.server_connection}'")
                vuetify.VBtn("Disconnect", block=True, small=True, color="success", click=ctrl.disconnect_from_server)

            # Connection doesn't exist
            with vuetify.VCardText(v_if=("!server_connection",)):
                html.Div(f"Not connected to a ParaView Server")

                with vuetify.VForm(submit=_connect):
                    vuetify.VTextField(v_model=("juviz_server_url", "jwb0001i.juwels"), label="URL")
                    vuetify.VTextField(v_model=("juviz_server_port", "11111"), label="Port", type="number")
                    vuetify.VBtn("Connect", type="submit", block=True, small=True, color="success")

        # Show Catalyst Connection status
        with vuetify.VCard(classes="pa-0", flat=True, outlined=False, tile=True):
            vuetify.VDivider()
            with vuetify.VCardTitle(classes="d-flex align-center py-1"):
                html.Div("ParaView Catalyst")

            vuetify.VDivider()

            # Catalyst open
            with vuetify.VCardText(v_if=("catalyst_connection",)):
                html.Div(f"Catalyst Connection available")
                vuetify.VBtn("Disconnect", block=True, small=True, color="success", click=ctrl.close_catalyst)

            # Catalyst closed
            with vuetify.VCardText(v_if=("!catalyst_connection",)):
                html.Div(f"Catalyst Connection not open")
                vuetify.VBtn("Connect", block=True, small=True, color="success", click=ctrl.open_catalyst)

