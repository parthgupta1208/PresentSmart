import gpt
import time

def process(topic_list):
    data_list=[]
    for topic in topic_list:
        dct={}
        text=gpt.gpt_summarise("I am giving you a topic. return a topic and information (elaborate and in depth. make it lengthy) in ten points. strictly follow the syntax'Topic : topic goes here , Summary : summary sentence 1, summary sentence 2,summary sentence 3,summary sentence 4,summary sentence 5,summary sentence 6, summary sentence 7,summary sentence 8,summary sentence 9,summary sentence 10'. the points should give complete in-depth knowledge of the topic.",topic)
        dct["Topic"]=text.split("Summary:")[0][6:]
        dct["Summary"]=text.split("Summary:")[1].split("\n")
        print(dct)
        code=gpt.gpt_summarise("I am giving you a topic. return a short sample code snippet for the given topic. do not write anything else.",topic)
        code=code.replace("```python","```")
        print(code)
        try:
            code=(code.split("```"))[1].split("```")[0]
        except:
            pass
        dct["Code"]=code
        data_list.append(dct)
        if len(topic_list)<=1:
            pass
        else:
            time.sleep(55)
    return data_list
