import spacy
from snips_nlu_parsers import BuiltinEntityParser

try:
    nlp = spacy.load("en_core_web_sm")
    nlp1 = spacy.load("NLP/output/model-best")
    parser = BuiltinEntityParser.build(language="en")
except Exception as e:
    print("Error --> {}".format(e))

class Info_extract:
    def __init__(self,input:str):
        self.data = {"participants":None,"agenda":"","date":None,"time":None}
        self.doc = nlp(input)
        self.train_agenda_nlp = nlp1(input)
    def get_data(self):
        participants = []
        for ent in self.train_agenda_nlp.ents:
            if ent.label_ == "AGENDA":
                self.data["agenda"] = ent.text
        for ent in self.doc.ents:
            if ent.label_ == "PERSON":
                participants.append(ent.text)
                self.data["participants"] = participants
            elif ent.label_ == "DATE":
                parsing = parser.parse(ent.text)
                date = parsing[0]["entity"]
                self.data["date"] = date
            elif ent.label_ == "TIME":
                parsing = parser.parse(ent.text)
                time = parsing[0]["entity"]
                self.data["time"] = time
        return self.data   
    