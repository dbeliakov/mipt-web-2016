package main

import "fmt"

func sum(a... int) (ret int) {
    ret = 0
    for _, v := range a {
        ret += v
    }
    return
}

func main() {
    fmt.Println(sum(1, 2))
    fmt.Println(sum(1, 2, 3))
}
