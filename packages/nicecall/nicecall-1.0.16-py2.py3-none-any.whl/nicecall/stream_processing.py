class StreamProcessing():
    def __init__(self, action, filters):
        self._action = action
        self._filters = filters

    @property
    def action(self):
        return self._action

    @property
    def filters(self):
        return self._filters


class StreamProcessingBuilder():
    def __init__(self):
        self._action = None
        self._filters = []

    def replace_action(self, action):
        self._action = action

    def skip_empty(self):
        self._filters.append(lambda line: line != "")

    def skip_whitespace(self):
        self.skip_empty()
        self._filters.append(lambda line: not line.isspace())

    def build(self):
        return StreamProcessing(self._action, self._filters)
