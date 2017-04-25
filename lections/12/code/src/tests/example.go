package example

func Average(vals []float64) float64 {
    var res float64 = 0
    for _, val := range vals {
        res += val
    }
    return res / float64(len(vals))
}
