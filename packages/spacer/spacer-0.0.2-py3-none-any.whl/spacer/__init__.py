from typing import Any, Dict, List

from ._version import __version__
from .handlers import setup_handlers


def _jupyter_labextension_paths() -> List[Dict[str, str]]:
    return [{
        "src": "labextension",
        "dest": "@datalayer/spacer"
    }]


def _jupyter_server_extension_points() -> List[Dict[str, Any]]:
    return [{
        "module": "spacer"
    }]


def _load_jupyter_server_extension(server_app):
    """Registers the API handler to receive HTTP requests from the frontend extension.

    Parameters
    ----------
    server_app: jupyter_server.serverapp.ServerApp
    """
    setup_handlers(server_app.web_app)
    name = "spacer"
    server_app.log.info(f"Registered {name} server extension")


# For backward compatibility with notebook server - useful for Binder/JupyterHub
load_jupyter_server_extension = _load_jupyter_server_extension
