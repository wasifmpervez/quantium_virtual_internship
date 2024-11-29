from dash_app import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#title", timeout=10)

def test_viz(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization")

def test_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#regions-radio")