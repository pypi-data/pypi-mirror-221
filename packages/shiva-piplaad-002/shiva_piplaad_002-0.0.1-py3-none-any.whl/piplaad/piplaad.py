import openai


class create:
    def __init__(self, api_key):
        self.api_key = api_key

    def text(self, data, word_count):
        def clean_text(data):
            clean_text = str(data).strip()
            return clean_text
        
        openai.api_key = self.api_key
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt= data,
                temperature=0,
                max_tokens=word_count,
                top_p=1,
                frequency_penalty=0.2,
                presence_penalty=0
            )

            text = response["choices"][0]["text"]
            text = clean_text(text)
            return text
        
        except openai.error.OpenAIError as e:
            print(e.error)

    def text_command(self, command, data, word_count):
        def clean_text(data):
            clean_text = str(data).strip()
            return clean_text

        command = command + ": "
        combined_data = command + data       
        openai.api_key = self.api_key

        try: 
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt= combined_data,
                temperature=0,
                max_tokens=word_count,
                top_p=1,
                frequency_penalty=0.2,
                presence_penalty=0
            )

            text = response["choices"][0]["text"]
            text = clean_text(text)
            return text
        
        except openai.error.OpenAIError as e:
            print(e.error)

