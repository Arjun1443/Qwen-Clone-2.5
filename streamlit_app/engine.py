import re

def reward_breakdown(text,expected):
    answer=text.split('<answer>')[-1].split('</answer>')[0].strip()
    strict=bool(re.match(r'^<reasoning>\n.*?\n</reasoning>\n<answer>\n.*?\n</answer>\n$',text))
    soft=bool(re.match(r'<reasoning>.*?</reasoning>\s*<answer>.*?</answer>',text))
    count=0.0
    if text.count('<reasoning>\n')==1: count+=.125
    if text.count('\n</reasoning>\n')==1: count+=.125
    if text.count('\n<answer>\n')==1:
        count+=.125
        count-=len(text.split('\n</answer>\n')[-1])*.001
    if text.count('\n</answer>')==1:
        count+=.125
        count-=(len(text.split('\n</answer>')[-1])-1)*.001
    return answer,{'Exact answer':2.0 if answer==expected.strip() else 0.0,'Integer answer':.5 if answer.isdigit() else 0.0,'Strict format':.5 if strict else 0.0,'Soft format':.5 if soft else 0.0,'XML structure':count}
