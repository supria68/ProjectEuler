
const getLargestPrimeFactor = (number) => {
	while(number % 2 === 0)
		number /= 2;

	for(let i = 3; i< number; i+=2) {
		while(number % i === 0 && i<number)
			number /= i;
	}
	return number;
}

console.log("The largest prime factor of the number 600851475143 is: "+getLargestPrimeFactor(600851475143));