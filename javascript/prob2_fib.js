let sum = 0;
let fib_numbers = [1, 2];

const nextFibTerm = (fib) => {
	return fib[fib.length - 1] + fib[fib.length - 2];
}

while (fib_numbers[fib_numbers.length - 1] < 4e+6) {
	fib_numbers.push(nextFibTerm(fib_numbers));
}

fib_numbers.map(val => {
	if(val % 2 === 0)
		sum += val;
})

console.log("Considering the terms in the Fibonacci sequence whose values do not exceed four million, the sum of the even-valued terms is: "+sum);