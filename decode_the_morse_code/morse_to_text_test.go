package kata

import "testing"

func TestDecodeMorseHeyJude(t *testing.T) {
	want := "HEY JUDE"
	resut := DecodeMorse(".... . -.--   .--- ..- -.. .")
	if want != resut {
		t.Fatalf("Excepted: %s Got: %s", want, resut)
	}
}

func TestDecodeMorseIgorAmorim(t *testing.T) {
	want := "IGOR AMORIM"
	resut := DecodeMorse(".. --. --- .-.   .- -- --- .-. .. --")
	if want != resut {
		t.Fatalf("Excepted: %s Got: %s", want, resut)
	}
}
