package kata

import (
	"fmt"
	"sort"
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

	for _, word := range strings.Split(morseCode, "   ") {
		for _, letter := range strings.Split(word, " ") {
			b.WriteString(MORSE_CODE[string(letter)])
		}
		b.WriteString(" ")
	}

	return strings.TrimSpace(b.String())
}

/*
https://www.codewars.com/kata/54b72c16cd7f5154e9000457

In this kata you have to write a Morse code decoder for wired electrical telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together,
which can be detected on a remote station. The Morse code encodes every character being transmitted as a
sequence of "dots" (short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.

"Dash" – is 3 time units long.

Pause between dots and dashes in a character – is 1 time unit long.

Pause between characters inside a word – is 3 time units long.

Pause between words – is 7 time units long.

However, the standard does not specify how long that "time unit" is. And in fact different operators would transmit
at different speed. An amateur person may need a few seconds to transmit a single character, a skilled professional
can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware that checks the line periodically,
and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is not connected
(remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a string containing
only symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".

That said, your task is to implement two functions:

1. Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to dots .,
dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's may
naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble discerning if
the particular sequence of 1's is a dot or a dash, assume it's a dot.

2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.
*/
func DecodeBits(bits string) string {
	timeUnit := CalcTimeUnit(bits)
	if timeUnit == 0 {
		return "."
	}
	// "Dash" – is 3 time units long
	dash := strings.Repeat("111", timeUnit)
	// Pause between characters inside a word – is 3 time units long.
	pauseBetweenChars := strings.Repeat("000", timeUnit)
	// Pause between words – is 7 time units long.
	pauseBetweenWords := strings.Repeat("0000000", timeUnit)

	var b strings.Builder
	pulses := 0
	bits = strings.TrimLeft(bits, "0")

	for _, word := range strings.Split(bits, pauseBetweenWords) {
		chars := strings.Split(word, pauseBetweenChars)
		for _, char := range chars {
			for i, bit := range char {
				var nextBit rune

				if i == len(char)-1 { // if last bit
					nextBit = '0' // assume the next is 0 even if it does'n exist
				} else {
					nextBit = rune(char[i+1])
				}

				if bit == '1' {
					pulses++
					if nextBit == '0' {
						if pulses < len(dash) {
							b.WriteString(".")
						} else {
							b.WriteString("-")
						}
						pulses = 0
					}
				}
			}
			b.WriteString(" ")
		}
		b.WriteString("  ")
	}

	return strings.TrimRight(b.String(), " ")
}

func CalcTimeUnit(bits string) int {
	// If there is no pause we cant compare
	// the pulses to see whether it is a dot or dash
	if !strings.Contains(bits, "0") {
		return 0
	}

	fieldsPulse := strings.FieldsFunc(bits, func(c rune) bool { return c == '0' })
	fieldsPause := strings.FieldsFunc(bits, func(c rune) bool { return c == '1' })

	m := make(map[string]int)
	// We only need 2 entries
	// one for dot and one for dash to compare
	for _, field := range fieldsPulse {
		if len(m) == 2 {
			break
		}
		if _, exists := m[field]; !exists {
			m[field] = len(field)
		}
	}

	// If there wasn't 2 differente sequence of bits
	// It means we can't say if it is a dot or a dash
	// So we need to verify the pauses
	if len(m) < 2 {
		fmt.Println(fieldsPause)
		return 0
	}

	// Now we need to get the smallest len
	lens := []int{}
	for _, v := range m {
		lens = append(lens, v)
	}

	sort.Ints(lens)

	return lens[0]
}

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
