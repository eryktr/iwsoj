package main

import (
	"fmt"
	"math"
	"os"
	"bufio"
	"log"
	"strconv"
)


func prime(n int) int {
	if n < 2 {
		return 0
	} else {
		counter := 0
		for i := 2; i <= n; i++ {
			counter = counter + 1
			for j := 2; j <= (int(math.Round(math.Sqrt(float64(i))))); j++ {
				if i % j == 0 {
					counter = counter - 1
					break
				}
			} 
		}
		return counter
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		i1, err := strconv.Atoi(scanner.Text())
		if err == nil {
			fmt.Println(prime(i1))
		}
	}

	if err := scanner.Err(); err != nil {
		log.Println(err)
	}
}