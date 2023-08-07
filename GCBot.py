import os

""" First change the following directory link to where all input files do exist """

os.chdir("D:\AI Chatbot")
import numpy as np

import pandas as pd

# File reading

with open('intents.json', 'r') as content_file:

    botdata = content_file.read()

Questions = []

Answers = []

for line in botdata.split("</pattern>"):

    if "<pattern>" in line:

        Quesn = line[line.find("<pattern>")+len("<pattern>"):]

    Questions.append(Quesn.lower())

for line in botdata.split("</template>"):

    if "<template>" in line:

        Ans = line[line.find("<template>")+len("<template>"):]

        Ans = Ans.lower()

        Answers.append(Ans.lower())

QnAdata = pd.DataFrame(np.column_stack([Questions,Answers]),columns = ["Questions","Answers"])

QnAdata["QnAcomb"] = QnAdata["Questions"]+" "+QnAdata["Answers"]

print(QnAdata.head())

for line in botdata.split("</pattern>"):

    if "<pattern>" in line:

        Quesn = line[line.find("<pattern>")+len("<pattern>"):]

Questions.append(Quesn.lower())

for line in botdata.split("</template>"):

    if "<template>" in line:

        Ans = line[line.find("<template>")+len("<template>"):]

        Ans = Ans.lower()

    Answers.append(Ans.lower())

    QnAdata = pd.DataFrame(np.column_stack([Questions,Answers]),columns = ["Questions","Answers"])

    QnAdata["QnAcomb"] = QnAdata["Questions"]+" "+QnAdata["Answers"]

print(QnAdata.head())

