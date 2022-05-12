package kata

import "testing"

func TestDecodeMultipleBitsPerDot1(t *testing.T) {
	want := "E"
	result := DecodeMorse(DecodeBits("111"))
	if want != result {
		t.Fatalf("Excepted: %s Got: %s", want, result)
	}
}

func TestDecodeMultipleBitsPerDot2(t *testing.T) {
	want := "E"
	result := DecodeMorse(DecodeBits("1111111"))
	if want != result {
		t.Fatalf("Excepted: %s Got: %s", want, result)
	}
}

func TestDecodeMultipleBitsPerDot3(t *testing.T) {
	want := "M"
	result := DecodeMorse(DecodeBits("110011"))
	if want != result {
		t.Fatalf("Excepted: %s Got: %s", want, result)
	}
}
