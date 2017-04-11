package main

import "fmt"

func FibGenerator() (func() int) {
    i1 := 1
    i2 := 0
    return func() (ret int) {
        ret = i1 + i2
        i1 = i2
        i2 = ret
        return
    }
}

func main() {
    gen := FibGenerator()
    for i := 0; i < 10; i++ {
        fmt.Println(gen())
    }
}
