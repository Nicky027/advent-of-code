package numbers

import "testing"

func TestGetSpokenNumber(t *testing.T) {
	got := GetSpokenNumber([]int{0, 3, 6}, 2020)
	want := 436

	if got != want {
		t.Errorf("got %d want %d", got, want)
	}
}
