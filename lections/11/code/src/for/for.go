package main

import "fmt"

func main() {
    i := 0;
    for i < 10 {
        fmt.Println(i)
        i++
    }

    for i := 0; i < 10; i++ {
        fmt.Println(i)
    }

    arr := []int{1, 2, 3}
    for i := range arr {
        fmt.Println(i)
    }
}
