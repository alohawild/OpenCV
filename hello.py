#!/usr/bin/env python
"""
    Copyright 2018  by Michael Wild (alohawild)
                    and by Ernest Bonat, Ph.D.
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
        http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
==============================================================================

"""
__author__ = 'michaelwild'
__copyright__ = "Copyright (C) 2018 Michael Wild and Ernest Bonat, Ph.D."
__license__ = "Apache License, Version 2.0"
__version__ = "0.0.1"
__credits__ = ["Michael Wild", "Ernest Bonat, Ph.D."]
__maintainer__ = "Michael Wild"
__email__ = ["alohawild@mac.com", "ernest.bonat@gmail.com"]
__status__ = "Initial"

import cv2
import sys
import xgboost as xgb

# =============================================================
# Main program begins here


print("Program: hello")
print("Version ", __version__, " ", __copyright__, " ", __license__)
print("Running on ", sys.version)
print("CV version: ", cv2.__version__)
print("XGBoost version: ", xgb.__version__)

print("Hello World CV")

img = cv2.imread('hello world.gif',0)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
