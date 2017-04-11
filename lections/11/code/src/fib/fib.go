package main

import "fmt"

func main() {
    s := make([]int, 2, 10)
    s[0] = 1
    s[1] = 1
    for i := 2; i < 10; i++ {
        s = append(s, s[i - 1] + s[i - 2])
    }
    fmt.Println(s)
}
