
import pandas as pd
import openai
import os

# store your openai key
openai.api_key = "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"

#openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Extract keywords from this text:\n\nBlack-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors.",
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.8,
  presence_penalty=0.0
)

