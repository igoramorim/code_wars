package kata

import "testing"

func TestAbbrevCompleteName(t *testing.T) {
	name := "Igor Amorim"
	want := "I.A"

	result := AbbrevName(name)
	if want != result {
		t.Fatalf(`Expected: %s Got: %s`, name, result)
	}
}

func TestAbbrevIncompleteName(t *testing.T) {
	name := "I Amorim"
	want := "I.A"

	result := AbbrevName(name)
	if want != result {
		t.Fatalf(`Expected: %s Got: %s`, name, result)
	}
}
