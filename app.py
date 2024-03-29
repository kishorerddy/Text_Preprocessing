import streamlit as st
import pandas as pd
import re
import emoji
file=st.file_uploader("Choose a file")

check_button=st.button("Check")
remove_button=st.button("Remove")
with st.sidebar:
    radio_button=st.radio("Preprocessing Data",["html_tags","Urls","Unwanted_characters","emojis","lower_upper",'Hashtags',"Mentions","All"])

if(file and check_button):
    df=pd.read_csv(file,names=["text_data"])
    def eda(data1,column):
        lower_upper=' '.join(data1[column]).islower()
        html_tags=data1[column].apply(lambda x: True if re.search('<.*?>',x) else False).sum()
        Urls=data1[column].apply(lambda x: True if re.search('http[s]?://.+?\S+',x) else False).sum()
        Hashtags=data1[column].apply(lambda x: True if re.search('#\S+',x) else False).sum()
        Mentions=data1[column].apply(lambda x: True if re.search('@\S+',x) else False).sum()
        Unwanted_characters=data1[column].apply(lambda x: True if re.search("[]\.\*'\-#@$%^(0-9)]",x) else False).sum()
        emojis=data1[column].apply(lambda x: True if emoji.emoji_count(x) else False).sum()
        if(lower_upper==False):
            st.write('your data contains lower and upper case')
        if(html_tags>0):
            st.write("Your data contains html tags")
        if(Urls>0):
            st.write("Your data contains urls")
        if(Hashtags>0):
            st.write("Your data contains hashtags")
        if(Mentions>0):
            st.write("Your data contains mentions")
        if(Unwanted_characters):
            st.write("Your data contains unwanted chars")
        if(emojis):
            st.write("Your data contains emojis")

    eda(df,"text_data")
if(file and radio_button=="All" and remove_button):
    df=pd.read_csv(file,names=["text_data"])
    def basic_pp(x, emoj="f"):
         
        if emoj == "t":
            x = emoji.demojize(x)
        
        x = x.lower()
        x = re.sub('<.*?>',' ', x)
        x = re.sub('http[s]?://.+?\S+', ' ', x)
        x = re.sub('#\S+', ' ', x)
        x = re.sub('@\S+', ' ', x)
        x = re.sub("[\]\.\*'\-&!$%^,;?(0-9)_:#]", ' ', x)
        return x
    cleaned_data=df["text_data"].apply(basic_pp,args="t")
    for i in cleaned_data:
        st.write(i)


if(file and radio_button=='html_tags' and remove_button):
    df=pd.read_csv(file,names=["text_data"])
    def html_tags(x):
        x = re.sub('<.*?>',' ', x)
        return x

    for i in df['text_data'].apply(html_tags):
        st.write(i)

if(file and radio_button=='Urls' and remove_button):
    df=pd.read_csv(file,names=["text_data"])
    def Urls(x):
        x = re.sub('http[s]?://.+?\S+', ' ', x)
        return x

    for i in df['text_data'].apply(Urls):
        st.write(i)        

if(file and radio_button=='Unwanted_characters' and remove_button):
    df=pd.read_csv(file,names=["text_data"])
    def Unwanted_characters(x):
        x = re.sub("[\]\.\*'\-&!$%^,;?(0-9)_:#]", ' ', x)
        return x

    for i in df['text_data'].apply(Unwanted_characters):
        st.write(i)     

if(file and radio_button=='emojis' and remove_button):
    df=pd.read_csv(file,names=["text_data"])
    def emojis(x,emojiss='f'):
        if emojiss=='t':
            x = emoji.demojize(x)
        return x

    for i in df['text_data'].apply(emojis,args="t"):
        st.write(i) 

if(file and radio_button=='lower_upper' and remove_button):
    df=pd.read_csv(file,names=["text_data"])
    def lower_upper(x):
        x = x.lower()
        return x

    for i in df['text_data'].apply(lower_upper):
        st.write(i)  

if(file and radio_button=='Mentions' and remove_button):
    df=pd.read_csv(file,names=["text_data"])
    def Mentions(x):
        x = re.sub('@\S+', ' ', x)
        return x

    for i in df['text_data'].apply(Mentions):
        st.write(i) 

 
if(file and radio_button=='Hashtags' and remove_button):
    df=pd.read_csv(file,names=["text_data"])
    def Hashtags(x):
        x = re.sub('#\S+', ' ', x)
        return x

    for i in df['text_data'].apply(Hashtags):
        st.write(i) 
 