
/* 1. Open the file and begin reading the data asynchronously.
   2. Split the data at the new line character and turn all of the single digits
	  into double digits by adding a 0 in front of them.
   3. Have the answer be a reduce() of input.
   4. In the reduce(), discard the card numbers and store the cards (make sure
      to account for any undefined cards).
   5. Seperate the values on the cards into winning numbers and picked numbers.
   6. Find how many matches there are between the winning numbers and picked
      numbers.
   7. Get the points for that card by taking the amount of matches - 1, then
      having that value be the raised power for a base 2 (ie. 2^3, 2^1, 2^0).
	  If there are 0 matches, then just have the points for that card equal 0.
   8. Return the accumalator + the points to get the total points for all the
      cards.
 */

const fs = require('fs');

fs.readFile('day4/input.txt', 'utf8', (err, data) => {
	if (err) throw err;
	// Split the data into lines and add a 0 in front of single digit numbers.
	const input = data.split('\n').map((x) => x.replace(/  /g, " 0"));
	const result = input.reduce((accumulator, element) => {
		const [_, cards] = element.split(': ');
		if (!cards) {
			return accumulator;
		}
		const [winning, picked] = cards.split(' | ');

		const point = picked
			.split(" ")
			// Go through winning and only find the cards that match picked.
			.filter((card) => winning.includes(card))
			.length; // Then give me the length of how many matches we found

		const value = point === 0 ? 0 : Math.pow(2, point - 1);
		return accumulator + value;
	}, 0);
	console.log(result);
});
