import sys
import re
# To be exported to a tools package later
class FlagObject:
    # Params
    #  - flag: a string representing the flag
    #  - callback: a method which will be called if the flag is detected. This method takes in an optional parm which is the argument
    #  - wheher or not the flag takes an argument
    def __init__(self, flag, callback, has_argument=False, case_sensitive = False):
        self.flag = flag
        self.callback = callback
        self.has_argument = has_argument
        self.case_sensitive = case_sensitive

    def __str__(self):
        return "flag: " + self.flag (" [arg]" if self.has_argument == True else "")

    def __hash__(self):
        return hash(str(self))

    def __eq__(self,other):
        if not other is type(self):
            return False
        return self.flag == other.flag if self.case_sensitive else self.flag.lower() == other.flag.lower()

def run(flag_dict):
    arguments = sys.argv[1:]
    for i in range(len(arguments)):
        current_flag = arguments[i]
        value = None
        #We want to check if the pointer is at a flag or an argument.
        if re.match(r'[-][a-zA-Z]+', current_flag) == None:
            continue
        if i + 1 < len(arguments):
            value = arguments[i + 1].replace("\"", "")
        try:
            flag = flag_dict[current_flag]
            if flag != None:
                flag.callback(value)
        except Exception as e:
            print(f'Ran into an error {str(e)}')