import os
import subprocess

import sublime_plugin


class OpenGhosttyCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        path = view.file_name() if view else None
        if path:
            cwd = os.path.dirname(path)
        else:
            folders = self.window.folders()
            cwd = folders[0] if folders else os.path.expanduser("~")
        # ghostty's own --help: launching the emulator from the CLI is unsupported on macOS
        subprocess.Popen(
            ["open", "-na", "Ghostty.app", "--args", "--working-directory=" + cwd]
        )
