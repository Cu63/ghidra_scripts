## ###
#  IP: GHIDRA
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#       http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
##
# An example of asking for user input.

# Note the ability to pre-populate values for some of these variables when AskScript.properties file exists.
# Also notice how the previous input is saved.


#@category Info

from io import StringIO
import sys

if __name__ == '__main__':
    #file = open(file.getPath(), 'w')
    tmp = sys.stdout
    man = StringIO()
    file = askFile('File', 'Enter file name to save file:')
    file = open(file.getPath(), 'wb')
    sys.stdout = file
    print(help())
    sys.stdout = tmp
    file.close()
