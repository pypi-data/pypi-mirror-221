# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from lifegu42d.app.lifegu42d_app import Lifegu42dApp


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ MAIN
# └─────────────────────────────────────────────────────────────────────────────────────


def main() -> None:
    """Main entry point"""

    # Initialize app instance
    app = Lifegu42dApp()

    # Run application instance
    app.run()
