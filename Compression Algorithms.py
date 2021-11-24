# import libraries
import os
import PySimpleGUI as sg

# Compression Algorithm
import sys
from re import match

##============================ Compressing
def compress(inputString):
	outputString = ''
	lastChar = ''
	charIndex = 0
	maxIndex = len(inputString)

	while charIndex < maxIndex:

		nextChar = inputString[charIndex]
		assert(match('[A-Z]', nextChar))
		outputString += nextChar
		charIndex += 1

		if(nextChar == lastChar): # fastforward charIndex through the duplicated characters
			count = 0 # counts duplicate characters compressed
			while((charIndex+count<maxIndex) and (inputString[charIndex+count]==lastChar) and (count<9)):
				count += 1
			charIndex += count
			nextChar = str(count)
			outputString += nextChar
		lastChar = nextChar

	return outputString
    
##============================ Decoding
def decompress(inputString):
	outputString = ''
	lastChar = ''
	charIndex = 0
	maxIndex = len(inputString)

	while charIndex < maxIndex:
		nextChar = inputString[charIndex]

		if(match('[A-Z]', nextChar)):
			outputString += nextChar
		else:
			assert(match('[0-9]',nextChar) and charIndex>1 and match('[A-Z]', lastChar) and (lastChar==inputString[charIndex-2]))
			for i in range(int(nextChar)): outputString += lastChar

		charIndex += 1
		lastChar = nextChar

	return outputString
    
##============================

def main():

    #### GUI Part #####
    sg.theme("Kayak")

    # Define the window layout
    layout = [
        
        [sg.Text('Document File'),sg.Input(),sg.FileBrowse()],
        
        ##============================  Compression Algorithms        
        [
            sg.Radio("Compression", "Radio", size=(20, 1), key="-C-"),
        ],
        
        ##============================  Decompression Algorithms        
        [
            sg.Radio("Deompression", "Radio", size=(20, 1), key="-D-"),
        ],
        
        ##============================ 
        [sg.Button('Ok',size=(3, 1)), sg.Button('Cancel',size=(5, 1))]
    ]

    # Create the window and show it without the plot
    window = sg.Window('Compression', layout)
    valid = False
    
    while True:
        event, values = window.read()
        # Here we read the path of the Text file
        input_file = open(values[0], 'r')
        
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            print("Exitting")            
            window.close()
            exit()
            break

        if event == "Ok":

            #Compressed
            if values["-C-"]:
                output_file = open('Compressed.txt', 'w')
                string_text = compress(input_file.read())
                output_file.write(string_text)
                input_file.close()
                output_file.close()
                
            #Decoded
            elif values["-D-"]:
                output_file = open('Decoded.txt', 'w')
                string_text = decompress(input_file.read())
                output_file.write(string_text)
                input_file.close()
                output_file.close()
            
main()
