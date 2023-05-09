import gpt

def process(filename):
    text=pdf2text.pdf2text(filename)
    summarized_text=top_sent.top_sentences(text)
    super_summarized_list=[]
    count=0
    for i in summarized_text:
        count+=1
        if count>3:
            break
        super_summarized_text=gpt.gpt_summarise(str(i[0]))
        super_summarized_list.append(super_summarized_text)
    print(super_summarized_list)
    final_list=[]
    for i in super_summarized_list:
        dct={}
        dct["Topic"]=i.split("Summary:")[0][6:]
        dct["Summary"]=i.split("Summary:")[1].split("\n")
        final_list.append(dct)
    for i in final_list:
        i["Topic"]=i["Topic"].replace("\n","").strip()
    return(final_list)