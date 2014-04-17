import os, sublime_plugin, sublime, subprocess, threading

##########
# Basics #
##########

# Specify your PDDL project folder:
# e.g.:
# PDDL_project_root_folder = "~/Documents/myPDDL/"
PDDL_project_root_folder = "~/Documents/myPDDL/"

# Shell command for opening Sublime Text (normally one of subl,
# sublime, sublime-text)
sublime_text="sublime-text"


###########
# Experts #
###########

class MypddlCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        # Start a thread so that Sublime is not locked 
        thread = MypddlThread(self.view, edit, **args)
        thread.start()


class MypddlThread(threading.Thread):
    """ Thread for myPDDL """

    # Initalize variables
    def __init__(self,view, edit, **args):
        self.view = view
        self.args = args
        self.file_name = view.file_name()
        threading.Thread.__init__(self)

    # Run thread
    def run(self):
                
        # Get name of opened file in Sublime Text
        file_name=self.view.file_name()
        # Run myPDDL
        # -diagram
        if self.args['text'][0] == "diagram":
            os.system("myPDDL "+ "diagram" + " " + file_name)
            
        # -distance
        if self.args['text'][0] == "distance":
            os.system("myPDDL "+ "distance" + " " + file_name)
        # -new
        if self.args['text'][0] == "new":
            self.view.window().show_input_panel("Please enter the name of the new PDDL project:",
                                                'pddl-project-name', self.on_done, None, None)

    # Create the folder for myPDDL-new
    def on_done(self, user_input):
        
        # Expand the user (if path is specified with a '~')
        PDDL_project_root_folder_expanded = os.path.expanduser(PDDL_project_root_folder)
        
        # Create project root folder if it does not exist yet 
        if not os.path.exists(PDDL_project_root_folder_expanded):
            os.makedirs(PDDL_project_root_folder_expanded)

        # Create project folder using myPDDL-new
        subprocess.Popen(["myPDDL", "new", user_input, PDDL_project_root_folder_expanded])

        # Open created project in Sublime Text
        PDDL_project_folder = PDDL_project_root_folder_expanded + "/" +  user_input + "/"
        subprocess.Popen([sublime_text, PDDL_project_folder])
