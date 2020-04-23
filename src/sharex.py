# Keypirinha launcher (keypirinha.com)

import keypirinha as kp
import keypirinha_util as kpu
import keypirinha_net as kpnet
import os
import json

class ShareX(kp.Plugin):
    """
    Command ShareX using Keypirinha.
    """

    # The default path for the sharex executable
    DEFAULT_SHAREX_PATH = "C:\Program Files\ShareX"

    # The default path to the user configuration files
    DEFAULT_SHAREXUSER_PATH = "{}\Documents\ShareX".format(os.path.expanduser('~'))

    SHAREX_EXE = 'ShareX.exe'
    WORKFLOW_CONFIG_FILE = 'HotkeysConfig.json'
    ITEMCAT = kp.ItemCategory.USER_BASE + 1
    LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def __init__(self):
        super().__init__()
        self.suggestions = {}        
        self.workflows = []

    def on_start(self):
        self.read_config()
        self.initialize_suggestions()

    def on_catalog(self):
        self.set_catalog([
            self.create_item(
                category=kp.ItemCategory.KEYWORD,
                label="ShareX",
                short_desc="Open ShareX or execute actions",
                target="ShareX",
                args_hint=kp.ItemArgsHint.ACCEPTED,
                hit_hint=kp.ItemHitHint.KEEPALL
            )
        ])

    def on_suggest(self, user_input, items_chain):
        if not items_chain or items_chain[0].category() != kp.ItemCategory.KEYWORD:
            return

        if items_chain:
            suggestions = []

            # custom workflow
            if (len(items_chain) > 1):
                # Only read the file the first time when the user select "Custom Workflow"
                if not user_input:
                    self.workflows = self.read_workflows()

                for workflow in self.workflows:
                    suggestions.append(
                        self.create_item(
                            category=self.ITEMCAT,
                            label=workflow.label,
                            short_desc="Job: {}".format(workflow.desc),
                            target='-workflow "{}"'.format(workflow.label),
                            args_hint=kp.ItemArgsHint.FORBIDDEN,
                            hit_hint=kp.ItemHitHint.IGNORE
                        )
                    )
            else:
                for target, suggestion in self.suggestions.items():
                    suggestions.append(
                        self.create_item(
                            category=self.ITEMCAT,
                            label=suggestion.label,
                            short_desc=suggestion.desc,
                            target=target,
                            loop_on_suggest=suggestion.loop_on_suggest if suggestion.loop_on_suggest else False,
                            args_hint=kp.ItemArgsHint.FORBIDDEN,
                            hit_hint=kp.ItemHitHint.IGNORE
                        )
                    )

            self.set_suggestions(suggestions, kp.Match.FUZZY, kp.Sort.DEFAULT)

    # Execute the selected action or open sharex
    def on_execute(self, item, action):
        kpu.shell_execute("{}\{}".format(self.sharex_path, self.SHAREX_EXE), args=item.target() if not item.target() == "ShareX" else "")

    def on_events(self, flags):
        if flags & kp.Events.PACKCONFIG:
            self.info("Configuration changed, rebuilding catalog...")
            self.on_catalog()

    # Read the configuration file and set some variables
    def read_config(self):
        settings = self.load_settings()
        self.sharex_path = settings.get_stripped("path", section="main", fallback=self.DEFAULT_SHAREX_PATH)

        if not self.file_exists("{}\{}".format(self.sharex_path, self.SHAREX_EXE)):
            self.err("Could not find ShareX executable in the provided path: ", self.sharex_path)

        self.sharex_userpath = settings.get_stripped("user_path", section="main", fallback=self.DEFAULT_SHAREXUSER_PATH)        

    # Initialize all the possible suggestions the user can select
    def initialize_suggestions(self):
        try:
            lines = self.load_text_resource('actions.json')
            data = json.loads(lines)
        except Exception as exc:
            self.err("Failed to load sharex actions. Error: {}".format(exc))
            return

        for item in data:
            loop = True if item.get('loop_on_suggest') else False
            self.suggestions[item['target']] = Suggestion(item['label'], item['desc'], loop)

    # Load all sharex defined workflows (the ones that have description)
    def read_workflows(self):
        workflows_path = "{}/{}".format(self.sharex_userpath, self.WORKFLOW_CONFIG_FILE)
        if not self.file_exists(workflows_path):
            self.err("Could not find ShareX workflows configuration file in the path:", self.sharex_userpath)
            return []

        with open(workflows_path, "r") as workflowfile:
            data = json.loads(workflowfile.read())

        workflows = []
        for item in data['Hotkeys']:
            # Only the ones with description
            if item['TaskSettings']['Description']:
                workflows.append(Suggestion(item['TaskSettings']['Description'], item['TaskSettings']['Job']))

        return workflows

    def file_exists(self, file):
        return os.path.isfile(file)

class Suggestion():
    label = None
    desc = None
    loop_on_suggest = None

    def __init__(self, label, desc, loop_on_suggest = False):
        self.label = label
        self.desc = desc
        self.loop_on_suggest = loop_on_suggest