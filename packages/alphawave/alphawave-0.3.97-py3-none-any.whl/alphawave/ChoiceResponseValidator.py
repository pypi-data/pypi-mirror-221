from promptrix.promptrixTypes import PromptFunctions, PromptMemory, Tokenizer
from alphawave.alphawaveTypes import PromptResponse, Validation, PromptResponseValidator
import json
import traceback

class ChoiceResponseValidator(PromptResponseValidator):
    def __init__(self, choices=None, missing_choice_feedback="Response did not contain a choice from "):
        self.choices = []
        if choices is None or type(choices) != list:
            print(f' ChoiceResponseValidator init must be provided a list of string choices')
        else:
            for choice in choices:
                self.choices.append(choice.lower())
        self.missing_choice_feedback = missing_choice_feedback+str(self.choices)
        
    def validate_response(self, memory: PromptMemory, functions: PromptFunctions, tokenizer: Tokenizer, response: PromptResponse, remaining_attempts) -> Validation:
        message = response['message']
        if type(message) != str:
            text = str(message)
        else:
            text = message
        text = text.lower()
        min_find = 9999
        # find first choice in returned text. Sloppy, could check for multiple choice matches.
        for choice in self.choices:
            if choice in text:
                if text.find(choice) < min_find or (text.find(choice) == min_find and len(choice) > len(found_choice)):
                    # this will make sure 'does not' beats 'does' in same start pos!
                    min_find = text.find(choice)
                    found_choice = choice
        if min_find < 9999:
            return {
                'type': 'Validation',
                'valid': True,
                'value': found_choice
            }
                
        return {
            'type': 'Validation',
            'valid': False,
            'feedback': self.missing_choice_feedback 
        }
