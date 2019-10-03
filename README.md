# PowerAItoTensorflowXML
A script to add filenames to PowerAI's XML files, so they can be used with the common xml_to_csv.py script

This is a simple script to change the output XMLs from IBM's PowerAI vision into a format that can be read by the XML to CSV script
that everyone uses. I did have to modify the indexes from the XML to csv script, so I included that here as well. Credit goes to
edjeelectronics, and/or readthedocs.io for that script, although I can't be certain of the original authors.

it SHOULD replace jpeg and JPG with jpg, but that doesn't seem to be working. I just used egrep and sed to fix that, though. If someone wants to fix that, by all means go ahead.

## Usage
just drop it in your images folder and run it.
