package kata

import (
	"strings"
)

/*
https://www.codewars.com/kata/54b724efac3d5402db00065e

In this kata you have to write a simple Morse code decoder.

While the Morse code is now mostly superseded by voice and digital data communication
channels, it still has its use in some applications around the world.

The Morse code encodes every character as a sequence of "dots" and "dashes". For example,
the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−.

The Morse code is case-insensitive, traditionally capital letters are used. When the message
is written in Morse code, a single space is used to separate the character codes and 3 spaces
are used to separate words.

For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most
notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···.
These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

DecodeMorse(".... . -.--   .--- ..- -.. .")
// should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
*/
func DecodeMorse(morseCode string) string {
	var b strings.Builder

	for _, word := range strings.Split(morseCode, SPACE_BETWEEN_WORDS) {
		for _, letter := range strings.Split(word, " ") {
			b.WriteString(MORSE_CODE[string(letter)])
		}
		b.WriteString(" ")
	}

	return strings.TrimSpace(b.String())
}

const SPACE_BETWEEN_WORDS = "   "

var MORSE_CODE map[string]string

func init() {
	MORSE_CODE = make(map[string]string)

	MORSE_CODE[".-"] = "A"
	MORSE_CODE["-..."] = "B"
	MORSE_CODE["-.-."] = "C"
	MORSE_CODE["-.."] = "D"
	MORSE_CODE["."] = "E"
	MORSE_CODE["..-."] = "F"
	MORSE_CODE["--."] = "G"
	MORSE_CODE["...."] = "H"
	MORSE_CODE[".."] = "I"
	MORSE_CODE[".---"] = "J"
	MORSE_CODE["-.-"] = "K"
	MORSE_CODE[".-.."] = "L"
	MORSE_CODE["--"] = "M"
	MORSE_CODE["-."] = "N"
	MORSE_CODE["---"] = "O"
	MORSE_CODE[".--."] = "P"
	MORSE_CODE["--.-"] = "Q"
	MORSE_CODE[".-."] = "R"
	MORSE_CODE["..."] = "S"
	MORSE_CODE["-"] = "T"
	MORSE_CODE["..-"] = "U"
	MORSE_CODE["...-"] = "V"
	MORSE_CODE[".--"] = "W"
	MORSE_CODE["-..-"] = "X"
	MORSE_CODE["-.--"] = "Y"
	MORSE_CODE["--.."] = "Z"

	MORSE_CODE["-----"] = "0"
	MORSE_CODE[".----"] = "1"
	MORSE_CODE["..---"] = "2"
	MORSE_CODE["...--"] = "3"
	MORSE_CODE["....-"] = "4"
	MORSE_CODE["....."] = "5"
	MORSE_CODE["-...."] = "6"
	MORSE_CODE["--..."] = "7"
	MORSE_CODE["---.."] = "8"
	MORSE_CODE["----."] = "9"

	MORSE_CODE["...---..."] = "SOS"

	MORSE_CODE["-..-."] = "/"
	MORSE_CODE["-.--."] = "("
	MORSE_CODE["-.--.-"] = ")"
	MORSE_CODE["..--.-"] = "_"
	MORSE_CODE["-....-"] = "-"
	MORSE_CODE["--..--"] = ","
	MORSE_CODE[".-.-.-"] = "."
	MORSE_CODE["---..."] = ":"
	MORSE_CODE["-.-.-."] = ";"
	MORSE_CODE["-.-.--"] = "!"
	MORSE_CODE[".----."] = "'"
	MORSE_CODE[".-.-."] = "+"
	MORSE_CODE["..--.."] = "?"
	MORSE_CODE["-...-"] = "="
	MORSE_CODE[".--.-."] = "@"
	MORSE_CODE["...-..-"] = "$"
	MORSE_CODE[".-..."] = "&"
	// MORSE_CODE[".-..-."] = "\""
}
