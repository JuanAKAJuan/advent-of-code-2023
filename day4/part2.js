const fs = require('fs');

fs.readFile('day4/input.txt', 'utf8', (err, data) => {
	if (err) throw err;

	const lines = data.split('\n').map((x) => x.replace(/  /g, ' 0'));
	lines.pop(); // There is an empty string at the end, get rid of it.

	const cardCount = new Array(lines.length).fill(1);

	lines.forEach((row, index) => {
		const [_, card] = row.split(': ');
		const [winning, picked] = card.split(' | ');

		const point = picked
			.split(" ")
			.filter((card) => winning.includes(card))
			.length;

		// Add the amount of cards the current card has to each of the cards
		// in front of it that it can reach with its points.
		// Ex) if points = 4 and currentCardCount = 2 then add 2 cards
		//     to each card ahead from currentCard <= currentCard + points
		if (point) {
			for (let i = index + 1; i <= index + point; i++) {
				cardCount[i] += cardCount[index];
			}
		}
	});
	console.log(cardCount.reduce((accumulator, element) => accumulator + element));
});

