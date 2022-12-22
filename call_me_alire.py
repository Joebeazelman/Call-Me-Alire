"""
Call Me Alire

Enables seamless integration with Alire

A handy cross-platform solution for seamlessly integrating GnatStudio and Alire. Now you can open 
your projects directly within GPS without ever typing another command from the terminal!

"""

import os
import subprocess
import GPS

call_me_alire_app = None

plugin_name = "Call-Me-Alire"
plugin_alire_exe_pref = f"Plugins/{plugin_name}/Alire-Executable-Path"

printenv_fmt = "unix"         # Use unix format for alr printenv
printenv_prefix = "export "
printenv_line_delimeter = "="

logger = GPS.Logger(plugin_name)

GPS.Preference(plugin_alire_exe_pref).create(
    "Alire executable path", "string",
    """Full path of Alire executable (to find it, run "which alr" from your OS terminal) """,
    "")

class Call_Me_Alire(object):
    def __init__(self):
        self.alire_exec_path = ""

        # setup call backs
        self.__on_preferences_changed(hook=None)
        self.__on_project_changing(hook=None, file=GPS.Project.root().file())
        GPS.execute_action("reload project")

        GPS.Hook("preferences_changed").add(self.__on_preferences_changed)
        GPS.Hook("project_changing").add(self.__on_project_changing)

    def __del__(self):
        GPS.Hook("preferences_changed").remove(self.__on_preferences_changed)
        GPS.Hook("project_changing").remove(self.__on_project_changing)

    def __on_preferences_changed(self, hook):
        v = GPS.Preference(plugin_alire_exe_pref).get()
        if v != self.alire_exec_path:
            self.alire_exec_path = v
            logger.log("Alire executable path set.")

    def __on_project_changing(self, hook, file):
        logger.log("Get path to Alire executable")
        if self.alire_exec_path:        
            cmd = ' '.join([self.alire_exec_path, 'printenv', f'--{printenv_fmt}'])
            proc = subprocess.Popen(cmd,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE, 
                                    shell=True, text=True, 
                                    cwd=file.directory())
            out, err = proc.communicate()
            logger.log(f"alr printenv output: {out}")

            if proc.returncode == 0:
                env_vars = dict(
                    var.removeprefix(printenv_prefix).replace('"','').split(printenv_line_delimeter)
                    for var in list(out.splitlines())
                )
                GPS.setenv("GPR_PROJECT_PATH", env_vars["GPR_PROJECT_PATH"])
                GPS.setenv("PATH", env_vars["PATH"])
            else:
                logger.log("Project ISN'T an Alire project.")
                return None
        else:
            logger.log("Alire path NOT set in preferences")

def on_gps_started(h):
    global call_me_alire_app
    call_me_alire_app = Call_Me_Alire()

GPS.Hook("gps_started").add(on_gps_started)
