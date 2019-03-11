# pylang_ident

Processes a file, line by line, using the "langid" library to identify the language of the line within a given confidence level.
Language is reported using ISO 2 character codes: https://www.sitepoint.com/iso-2-letter-language-codes/
Commas are removed during processing so that the output can be in CSV format.
Only messages identified as Non-English are reported.
