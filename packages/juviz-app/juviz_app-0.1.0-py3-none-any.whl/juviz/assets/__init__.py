"""
Configure an AssetManager to provide icons, images, etc., to your application
"""
from pv_visualizer.app.assets import LocalFileManager

asset_manager = LocalFileManager(__file__)
asset_manager.url("icon", "./FZJ_Logo.svg")
