from flask import Flask, request
from pydantic import BaseModel,ValidationError
from NLP.Info_extract import Info_extract
import json

app = Flask(__name__)
api_path = '/api/v1/schedule'

class ResponseModel(BaseModel):
    status:bool = False
    participants: list[str] 
    agenda: str 
    date:dict 
    time:dict 


@app.route(api_path, methods=['POST'])
def parse_input():
    try:
        input_string = request.data.decode('utf-8') 
        extract = Info_extract(input_string)
        output_dict = extract.get_data() 
        data = ResponseModel(status=True,**output_dict)
        return data.json()
    except ValidationError as e:
        for err in e.errors():
            if err["loc"][0] == "time":
                output_dict["time"] = {"message":"invalid or NO Time mentioned"}
            elif err["loc"][0] == "date":
                output_dict["date"] = {"message":"invalid or NO Date mentioned"}
            elif err["loc"][0] == "participants":
                output_dict["participants"] = ["No participants mentioned"]
            elif err["loc"][0] == "agenda":
                output_dict["agenda"] = "agenda missing"
        return ResponseModel(status=False,**output_dict).json()


if __name__ == '__main__':
    app.run(debug=True)
