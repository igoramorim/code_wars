package kata

import "testing"

func TestHighAndLow1(t *testing.T) {
	want := "42 -9"
	result := HighAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
	if want != result {
		t.Fatalf("Expected: %s. Got: %s", want, result)
	}
}

func TestHighAndLow2(t *testing.T) {
	want := "3 1"
	result := HighAndLow("1 2 3")
	if want != result {
		t.Fatalf("Expected: %s. Got: %s", want, result)
	}
}
