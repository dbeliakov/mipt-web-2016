package main

import "fmt"

func main() {
    for i := 0; i < 10; i++ {
        if i % 2 == 0 {
            fmt.Println(i)
        }
    }
    if i := 2; i % 2 == 0 {
        fmt.Println("Should print")
    }
    if i := 2; i % 2 == 1 {
        fmt.Println("Shouldn't print")
    }
}
