#!/usr/bin/env python
import langid
from langid.langid import LanguageIdentifier, model

'''
Processes a file, line by line, using the "langid" library to identify the language of the line within a given confidence level.
Language is reported using ISO 2 character codes: https://www.sitepoint.com/iso-2-letter-language-codes/
Commas are removed during processing so that the output can be in CSV format. 
Only messages identified as Non-English are reported.
'''

identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

confidence_target = 0.9999

english = 0
non_english = 0
total = 0
unsure = 0
sure = 0
scored_english_messages = []
scored_non_english_messages = []

with open('sampleMessages.txt') as f:
    for message in f:
        total += 1
        message = (message.rstrip()).replace(',', '')
        res = identifier.classify(message)
        lang = ((str(res).split(' '))[0]).split("'",3)[1]
        score = ((str(res).split(' '))[1]).rstrip(')')
        if lang != 'en':
            non_english += 1
            if str(score) >= str(confidence_target):
                scored_non_english_messages.append(('{},{},{}').format(lang, score, message))
                sure += 1
            else:
                unsure += 1
        else:
            english += 1
            if str(score) >= str(confidence_target):
                scored_english_messages.append(('{},{},{}').format(lang, score, message))
                sure += 1
            else:
                unsure += 1

for message in scored_non_english_messages:
    print(message)

print('---')
print('Total messages analyzed: {}').format(total)
print('{} were identified with a confidence level of {} or higher - {}%').format(sure, confidence_target, str(round((float(sure)/float(total)*100),2)).split('.')[0])
print('{} were indentified as English and {} non-English with confidence').format(len(scored_english_messages), len(scored_non_english_messages))
