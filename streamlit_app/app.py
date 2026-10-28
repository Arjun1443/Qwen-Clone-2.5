import pandas as pd
import streamlit as st
from engine import reward_breakdown
from ui import page

page('GRPO Reward Lab','Inspect how formatting and answer rewards shape a fine-tuning signal.','QWEN FINE-TUNING')
st.info('This app evaluates reward functions from the Qwen2.5 study notebook. It does not run or fine-tune the 3B model on Community Cloud.')
left,right=st.columns([3,2])
with left:
    expected=st.text_input('Expected final answer',value='42')
    response=st.text_area('Candidate response',value='<reasoning>\nShort explanation.\n</reasoning>\n<answer>\n42\n</answer>\n',height=260,max_chars=10000)
answer,rewards=reward_breakdown(response,expected)
with right:
    st.metric('Total reward',f'{sum(rewards.values()):.3f}')
    st.metric('Extracted answer',answer[:60] or '(empty)')
    st.bar_chart(pd.DataFrame({'Reward':list(rewards),'Value':list(rewards.values())}).set_index('Reward'))
st.download_button('Download reward breakdown',pd.DataFrame([rewards]).to_csv(index=False),'reward-breakdown.csv','text/csv')
with st.expander('Why a high reward is not a good answer',expanded=True):
    st.markdown("""The functions reproduce the notebook's exact-match, integer, strict/soft formatting, and XML-count rewards. Formatting can earn points even when the answer is wrong. Regexes preserve the notebook behavior, including its treatment of newlines and trailing text.

The notebook credits Unsloth and uses Qwen2.5-3B-Instruct with GSM8K and GRPO. Training requires a compatible GPU environment; this app provides an inspectable reward-function experiment rather than a claim of original model development.
""")
