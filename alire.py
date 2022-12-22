"""
Call Me Alire

Enables seamless Alire and GnatStudio integration.

"""

import os
import subprocess
import GPS

call_me_alire_app = None

plugin_name = "Call-Me-Alire"
plugin_alire_exe_pref = f"Plugins/{plugin_name}/Alire-Executable-Path"

printenv_fmt = "unix"         # Use unix format
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
        self.gpr_project_path = ""
        self.project_path = GPS.Project.root().file().directory()
        self.gpr_proj_path_key = "GPR_PROJECT_PATH"

        # setup call backs
        self.__on_preferences_changed(hook=None)
        self.__on_project_changed(hook=None)
  
        GPS.Hook("preferences_changed").add(self.__on_preferences_changed)
        GPS.Hook("project_changed").add(self.__on_project_changed)
        GPS.Hook("project_changing").add(self.__on_project_changing)

    def __del__(self):
        GPS.Hook("preferences_changed").remove(self.__on_preferences_changed)
        GPS.Hook("project_changed").remove(self.__on_project_changed)
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
                for k, v in env_vars.items():
                    print(k, v)
                    GPS.setenv(k, v)
            else:
                logger.log("Project ISN'T an Alire project.")
                return None
        else:
            logger.log("Alire path NOT set in preferences")

    def __on_project_changed(self, hook):
        print("Project Changed")

def on_gps_started(h):
    global call_me_alire_app
    call_me_alire_app = Call_Me_Alire()

GPS.Hook("gps_started").add(on_gps_started)
