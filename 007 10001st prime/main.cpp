#include<iostream>
#include<cmath>


bool isCoPrime(int num, int* primes, int current) {
	for(int i=0; i<current; i++) {
		if(sqrt(num) < primes[i]) {
			return true;
		}
		if(num%primes[i] == 0) {
			return false;
		}
	}
	return true;
}

int getNextCoPrime(int* primes, int i) {
	int prime = primes[i-1]+1;
	while(!isCoPrime(prime, primes, i)) {
		prime++;
	}
	return prime;
}

int main() {
	int primes[10001] = {2};
	for(int i=1; i<10001; i++) {
		primes[i] = getNextCoPrime(primes, i);
	}
	std::cout<<primes[10000]<<std::endl;
}
