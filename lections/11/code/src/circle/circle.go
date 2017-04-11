package main

import (
    "fmt"
    "math"
)

type Shape interface {
    area() float64
}

type Circle struct {
    x float64
    y float64
    r float64
}

func (c Circle) area() float64 {
    return math.Pi * c.r*c.r
}

func (c *Circle) area() float64 {
    return 0
}

func main() {
    var c Shape = Circle{x: 0, y: 0, r: 5}
    fmt.Println(c.area())
}
