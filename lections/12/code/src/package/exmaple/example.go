package example

import "fmt"

func print() {
    fmt.Println("Private");
}

func callPrintPrivate() {
    print();
}

func Print() {
    fmt.Println("Public");
}
