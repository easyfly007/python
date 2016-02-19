#!/usr/local/bin/python
# Description:  Use this python script to analyze simulation regression report

import re

global _debug_print_
_debug_print_ = False


ac_analysis_entry_pattern = '[^\\n]+\.ac\d+\s+.+\(.+\).*\s+\d+\.\w+\s+AC Analysis\s+.+\n'
dc_analysis_entry_pattern = '[^\\n]+\.sw\d+\s+.+\(.+\).*\s+\d+\.\w+\s+DC Analysis\s+.+\n'
tran_analysis_entry_pattern = '[^\\n]+\.tr\d+\s+.+\(.+\).*\s+\d+\.\w+\s+Tran Analysis\s+.+\n'

# match all the patterns
def get_specific_entries(context, pattern):
    match = re.compile(pattern).findall(context)
    entries = []
    if match:
        for m in match:
            item_tokens = m.split()
            try:
                case_tokens = item_tokens[0].split('.')
                case_name = ""
                for i in range(len(case_tokens) - 1):
                    case_name += case_tokens[i] + '.'
                case_name += 'sp'
                ana_type = item_tokens[3] + " " + item_tokens[4]
                max_diff = item_tokens[2]
                worst_signal = item_tokens[1]
                entry = [case_name, ana_type, max_diff, worst_signal]
                entries.append(entry)
                if _debug_print_ == True:
                    print entry
            except:
                print "Pattern \'%s\' found, while some syntax error happens." %pattern
                return None
        return entries
    else:
        print "no match for pattern \'%s\'"%pattern
        return None


def  get_ac_diff(context):
    return get_specific_entries(context, ac_analysis_entry_pattern)

def  get_dc_diff(context):
    return get_specific_entries(context, dc_analysis_entry_pattern)

def  get_tran_diff(context):
    return get_specific_entries(context, tran_analysis_entry_pattern)

def run():
    import sys
    buf = open("demo.acc").read()

    ac_result = get_ac_diff(buf)
    print "ac result:"
    print ac_result
    if ac_result is not None:
        print len(ac_result)

    dc_result = get_dc_diff(buf)
    print "dc result:"
    print dc_result
    if dc_result is not None:
        print len(dc_result)

    tran_result = get_tran_diff(buf)
    print "tran result:"
    print tran_result
    if tran_result is not None:
        print len(tran_result)

if __name__=='__main__':
    run()
