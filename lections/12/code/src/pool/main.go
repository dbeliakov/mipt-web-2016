package main

import "fmt"

type Pool struct{}

func NewPool() Pool {
	return Pool{}
}

func (this *Pool) exec(f func(...interface{}) interface{}, args ...interface{}) chan interface{} {
	c := make(chan interface{})
	go func() {
		val := f(args...)
		c <- val
		close(c)
	}()
	return c
}

func main() {
	p := NewPool()
	res := make([]chan interface{}, 0)
	for i := 1; i <= 10; i++ {
		res = append(res, p.exec(func(args ...interface{}) interface{} {
			val := 1
			for _, a := range args {
				val *= a.(int)
			}
			return val
		}, i, i))
	}
	for _, r := range res {
		val := <-r
		fmt.Println(val)
	}
}
