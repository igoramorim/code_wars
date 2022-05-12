package kata

import "testing"

func TestDecodeBasicBits1(t *testing.T) {
	want := "E"
	result := DecodeMorse(DecodeBits("1"))
	if want != result {
		t.Fatalf("Excepted: %s Got: %s", want, result)
	}
}

func TestDecodeBasicBits2(t *testing.T) {
	want := "I"
	result := DecodeMorse(DecodeBits("101"))
	if want != result {
		t.Fatalf("Excepted: %s Got: %s", want, result)
	}
}

func TestDecodeBasicBits3(t *testing.T) {
	want := "EE"
	result := DecodeMorse(DecodeBits("10001"))
	if want != result {
		t.Fatalf("Excepted: %s Got: %s", want, result)
	}
}

func TestDecodeBasicBits4(t *testing.T) {
	want := "A"
	result := DecodeMorse(DecodeBits("10111"))
	if want != result {
		t.Fatalf("Excepted: %s Got: %s", want, result)
	}
}

func TestDecodeBasicBits5(t *testing.T) {
	want := "M"
	result := DecodeMorse(DecodeBits("1110111"))
	if want != result {
		t.Fatalf("Excepted: %s Got: %s", want, result)
	}
}
