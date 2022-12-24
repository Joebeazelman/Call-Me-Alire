# Call Me Alire

*A GNAT Studio plug-in to enable support for Alire-managed projects*

**Call Me Alire** is a cross-platform plug-in that enables GNAT Studio support for Alire-configured projects. It eliminates the compromise between GNAT Studio's productive IDE and Alire's powerful crate management facilities. You can seamlessly open and work with projects configured in Alire within GNAT Studio without executing commands from the shell. Overall, it results in significant productivity gains from a more streamlined workflow.

## Installation

Installation is fast and easy. Download **Call Me Alire** and copy it to your GNAT Studio plug-ins folder. Once complete, launch GNAT Studio and configure it by entering Alire's full executable path. For detailed instructions, proceed below.

### Requirements

- Installed GNAT Studio (version 23 or higher)

- Installed Alire (version 1.2.1 or higher)

### Step 1: Copy the plug-in file

Login in as an administrator. Depending on your platform, copy the **call_me_alire.py** file to:

- **Windows**: %HOME%.gnatstudio\plug-ins

- **MacOS**: $HOME/.gnatstudio/plug-ins

- **Unix, Linux**: $HOME/.gnatstudio/plug-ins

### Step 2: Enable the Plug-in

Launch **GNAT Studio**, if it's already running quit and relaunch it.  From the menu bar select **Edit > Preferences...** You should see a window labeled **Preferences**. On the left pane, select **Plugins**. If you see **Call Me Alire** listed directly under it, it means it already loaded; skip to the next step.

The **Preferences** page will list all the plug-ins installed in GNAT Studio in alphabetical order with checkboxes. To activate **Call Me Alire**, locate it on the list and click its checkbox. Exit by clicking the **Close** button on the window. **GNAT Studio** will ask you if you want to restart, click **Exit**.  Relaunch GNAT Studio again and return to the **Preference** page as aforementioned.

### Step 3: Configure the Plug-in

On the Preference page, you should see **Call Me Alire** on the left side of the screen. Click on it to reveal options on the larger right pane. Enter Alire's FULL executable path name in the field label **Alire executable path**. *NOTE: Depending on your theme, the field's border might be very light, click to the right of the label to see the a cursor.* Close the window and restart **GNAT Studio**. 

Test the **Call Me Alire** by opening any Alire manage project. You should see all your files in the project window. If you see the *empty.gpr*, it means an error occurred. Please create an issue on the GitHub page with as much pertinent data as you can. 

#### Appendix: Finding Alire's Executable Path

To find Alire's executable path, perform the following according to your platform terminal:

- **macOS, UNIX, Linux**: which alr

- **Windows (CMD)**: where alr

- **Powershell**: Get-Command alr

You should see a resulting path for Alire. Copy the path and return to GNAT Studios.

## Development
The plug-in is still under development. I made sure to test it as well as I can, including launching a beta in the Ada community. There's a good chance there's a bug somewhere in the code. If you encounter any issues, please submit an issue. If you want to contribute to the project, submit a pull request.