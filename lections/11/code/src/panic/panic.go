package main

import (
//    "fmt"
    "errors"
)

func main() {
    //defer func() {    
    //    str := recover()
    //    fmt.Println(str)
    //}()
    panic(errors.New("panic"))
}
