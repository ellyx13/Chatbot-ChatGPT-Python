import os
import openai
import gradio as gr
from pyChatGPT import ChatGPT

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..9J-QjvaE-IxQhr9q.TKQVZwZDdQQ6a_oL02Jy_-i-VJF65sr_oEYp7UtZE1PO8dJsf3fH8Mtla4AsKeAuNs45WD0mLPWx7nUDVbrZgHBInTe6KJJSU5ZkmquYJnJvdkzQVWTGgBm1sq_uTcwTuRhKG0iUUtN_lEK6NTp_gSqJYJ_nw--cETeRfaeSw3Sr3itruW-Lb6_Dwq3VlufA-_5sykKeBK7RVRuU-sXKrCPXrjx1a1hknR4kRpfEBymmrM3ndjla784oetpHqPwMmZTtNxJBb_nvRth5glxUiq2PGqxPGwHljcXT93uEZvYAurAA-3DKSBsrc7aGYH8an7j9cJP9EyaWNMHPt81rAr95zIiFnFuAnTaXjasU50A8ZkPUfA0LiTe9G5SdLz3PJWJ0yn6yFr5QVKK9bAbIHE4hErQ4YRvB0l3RG5BvXsUK7vkia88_moEz_4_HMzb5jAu-zvWMKcaEsiEX26sffwNdoM9utfybK2vAsuKCWF5fnWMjJ0ZgE6kDtjMTES3ByGzjwMOU31KLoMhUknyzIq3coZX2fkeGSrqf_hGoGoy-cO9Aqlud2grF1Gd-6H2ZZd8lMVlWGz6FwziOoOOR-tjjCWJbpxKR5BOieiGGUCfZWeRJkM06qg3QqMPLe1_KwZPnkfOXIb4RfULQsLfeC_nmnSkA56xgdum9bgVXkZTlEDe2wDaZJG-ArwQGhQzS5ODS106B4FQb0_hg2jHbugAVHxEfGUDfslJY6oiAbgS-4dBNC2ApU7GoohZybjkIBedzmK83DdyMu8_sDaurgxGra4S5sjrwI-rBqV0lNdIW-PCxw_ZAY2DCpfJ8CrbZkaieyw-UAymbOD9IEv7JnbpdakO7JrJ_NSHG9Q6aMnr4p_4JWzYmmroKNf0E3uvBtteOrHc81k2PlrTa3PHU-nI-qZjh3YMFwML1NGe0SPuet8NnkDwW4H8c9Ese5sIqwylGPjYEKjx0XWLOjOxp-IiyolxZg-BZS1wAAtJlhj4KEP0TbU2r3-wxpm17SCuq01eDhznhe5oRSEqcX6Wrk4XRLqT9OBDzZ6qLILvT8IF3GujSCY0Fw84QAp_slMi7eLD8Qg9hq6NR81A-orSusQpxxqnqQkEgNmmfLOALI8c3bMAEc5Hr91YgpTARHmjzzp8Pv9DXQx7ozKfC42usNSsSLUoiTugVCCppoXIOigQ_V26MFiNH7lJ7e6amFvjFjQmtudsF065gNFo9EFXgZe_ReQjPSa3_xTOHl1zOJ_ys0JMvNfEmG5UP2mS7lIOIpHCmOjNCcSCm7bqBu7TpxUotjNbumNcBfujWabRD2aYrrUNL8Cm33gxj0GnYaaZmOZLZhy7a6Z-I9GPOo1ill2a9CWa5tf6RwiscOCtK3TwDl2cOgj3cQW_0TFY_SMPN4cpc9G-vCt-fCEV-pb2i9vWk7KGooNVYJJ2D8YyQsgpbbnp77tZy29iAssm3Vcfwl9vAQTOcLePyNchELoEyrwP3_iXNWFAI_8NWo9Zos5IdjnxGlZc5_R6pOfxi7hkh_mkXq9luTZnYIo1sSTyY49DaRgrE2nS3hAZ3_5IunmG3DSHkeNU7NLtrDN864pCLmDzmKFGlZdyXYHhI1En6UtZsnscl-BmbQprVUHjYPiBJFI1e8qed-IaM8z6YR735-cRP-R7ufvCsiHHbIDxKxFa-mDzhQz8HDVIvKC2JUpqwtV1Yvah-En4yf5MmdSJ9l7iJbNAoUlXcA8z8ui4k13TW5386gSX0pbfX1cA7nMRRpSqkuOUkA4xe_P2z6G4dmoDttaEebNWuAGhKAiagAkFd03qQplsk0q5j7lDhzfGwhSO7UHvvsInp8gnoIYb8FqWy6Rm3d8QNwuBDhEOYXs7MY2ow1pfiZJzhVh9eiAlXHnThRYFlr9jGTPnG3aoJfc79-XSitPHplG9eQAyzA6pU5VhdV8hxfnnnOz3JvXhSV9hP3JpFNwSHiMcSEb75LIRyVrBNxTp8cCt29nNPladzZ0VtRi1VY86hLmAd1kxa1NVeAegv5oBCiTiADRgNwkF7gCnQ4kbKhvTX1RsH7pgP-U0kX5bDzjQqmvBNvxIjKy7DOEaxtR4hAQiF9fTQYlofvHXKrEzdhrkxBBy611S4nFgJVkzl_XbjZj6H0o1lhato64yLFadXpAsDqKxkQCQAF-Ems_D6-kS-M6uGdH3kXiFi843ZUx_FjE9bG5irFYmG11smp9Aq_58Py8L5Vea4YnpOTReDmi3MTX9wT6d6KcXf_k0eCKM2WtsPfLXow4S0u00x2zPpvRL3OGx1biE97tnkT8xyqD5jGHHiw9wzODvoc2169Q5YHcRopPQEdBjJ6dMYJeA.AH9MITJf9SFleqdkO2R6Sg'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat




start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

def outputsGPT(input, history):
    resp = api1.send_message(input)
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    output = resp['message']
    history.append((input, output))
    print("Human: ", input)
    print("ChatGPT: ", output)
    return history, history


block = gr.Blocks()
api1 = ChatGPT(session_token) 

with block:
    try:
        chatbot = gr.Chatbot()
        message = gr.Textbox(placeholder=prompt)
        state = gr.State()
        submit = gr.Button("SEND")
        submit.click(outputsGPT, inputs=[message, state], outputs=[chatbot, state])
    except Exception as e:
        print("Error: ", e.message, e.args)

block.launch(debug = False, show_api=False)