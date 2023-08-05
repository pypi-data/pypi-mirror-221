#    Copyright © 2021 Andrei Puchko
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import sys

if __name__ == "__main__":

    sys.path.insert(0, ".")

    from demo.demo import demo

    demo()

from PyQt6.QtWidgets import QProgressBar


from q2gui.pyqt6.q2widget import Q2Widget


class q2progressbar(QProgressBar, Q2Widget):
    def __init__(self, meta):
        super().__init__(meta)
        self.set_text(meta["label"])
        self.setMaximum(0)
        self.setMinimum(0)

    def set_max(self, value):
        self.setMaximum(value)

    def set_min(self, value):
        self.setMinimum(value)

    def set_value(self, value):
        if self.minimum() < self.maximum():
            self.setValue(value)
