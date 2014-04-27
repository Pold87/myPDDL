import os, sublime_plugin, sublime, subprocess, threading

class MypddlCommand(sublime_plugin.TextCommand):
    
    def run(self, edit, **args):
        file_name = self.view.file_name()
        mypddl_cmd =  "myPDDL"
        dir_name = None
        if file_name is not None:
            dir_name = os.path.dirname(file_name)
        # Start a thread so that Sublime is not locked 
        thread = MypddlThread(self.view, edit, file_name, dir_name, mypddl_cmd, **args)
        thread.start()


class MypddlThread(threading.Thread):
    """ Thread for myPDDL """

    # Initalize variables
    def __init__(self, view, edit, file_name, dir_name, mypddl_cmd, **args):
        self.view = view
        self.args = args
        self.file_name = file_name
        self.dir_name = dir_name
        self.mypddl_cmd = mypddl_cmd
        super(MypddlThread, self).__init__(self)

    # Run thread
    def run(self):
                
        # Run myPDDL
        # -diagram
        if self.args['text'][0] == "diagram":
            if self.dir_name:
                os.chdir(self.dir_name)
            subprocess.Popen([self.mypddl_cmd, "diagram", self.file_name])
            
        # -distance
        if self.args['text'][0] == "distance":
            subprocess.Popen([self.mypddl_cmd, "distance", self.file_name])
        # -new
        if self.args['text'][0] == "new":
            self.view.window().show_input_panel("Please enter the name of the new PDDL project:",
                                                'pddl-project-name', self.on_done, None, None)

    # Create the folder for myPDDL-new
    def on_done(self, user_input):
        
        s = sublime.load_settings("PDDL.sublime-settings")
        PDDL_project_root_folder_default = s.get("pddl_project_folder")
        sublime_text_default = s.get("sublime_shell_cmd")
        
        # Shell command for running Sublime Text
        sublime_text = self.view.settings().get('sublime_shell_cmd', sublime_text_default)
            
        # Folder for saving PDDL Projects
        PDDL_project_root_folder = self.view.settings().get('pddl_project_folder', PDDL_project_root_folder_default)

        # Expand the user (if path is specified with a '~')
        PDDL_project_root_folder_expanded = os.path.expanduser(PDDL_project_root_folder)
        
        # Create project root folder if it does not exist yet 
        if not os.path.exists(PDDL_project_root_folder_expanded):
            os.makedirs(PDDL_project_root_folder_expanded)

        # Create project folder using myPDDL-new
        subprocess.call([self.mypddl_cmd, "new", user_input, PDDL_project_root_folder_expanded])

        # Open created project in Sublime Text
        PDDL_project_folder = os.path.join(PDDL_project_root_folder_expanded, user_input)
        subprocess.Popen([sublime_text, "-a", PDDL_project_folder])
