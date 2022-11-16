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
# Find ascii strings.
# @category: strings 

def get_strnigs(start_addr, count=10):
    str_end = findBytes(start_addr, b'\x00')
    while count > 0:
        str_begin = int(str_end.toString(), 16) - 1
        c = getByte(toAddr(str_begin))
        while isprintable(c) and str_begin > 0:
            str_begin -= 1
            c = getByte(toAddr(str_begin))
        str_begin += 1
        if (toAddr(str_begin) != str_end):
            print('Found str at 0x%s'% str_begin)
            clearListing(toAddr(str_begin), str_end)
            createAsciiString(toAddr(str_begin),)
            count -= 1
        str_end = findBytes(str_end.next(), b'\x00')


def isprintable(c):
    # '\n' = 10, '\t' = 9
    if 32 <= c < 128 or c == 9 or c == 10: 
        return True
    return False


def main():
    start_addr = currentLocation.getAddress()
    count = askInt('strings count', 'Please enter num of strings: ')
    get_strnigs(start_addr, count)


if __name__ == '__main__':
    main()
