/**
	Title: artOfCode-whatABook.js
    Authors: * Jamal Damir
             * Ace Baugh
   Date: 12/07/2022
   Description: MongoDB Shell Scripts for the books and customers collections.
 */

// Connection String
// mongosh "mongodb+srv://buwebdev-cluster-1.9wmv0d7.mongodb.net/web335DB" --apiVersion 1 --username web335_user

// Delete the books and customers collections.
db.books.drop();
db.customers.drop();

// Create the books and students collections using Document Validation.
db.createCollection("books", {
	validator: {
		$jsonSchema: {
			bsonType: "object",
			properties: {
				title: {
					bsonType: "string",
				},
				genre: {
					bsonType: "string",
				},
				author: {
					bsonType: "string",
				},
				bookId: {
					bsonType: "string",
				},
			},
		},
	},
});

db.createCollection("customers", {
	validator: {
		$jsonSchema: {
			bsonType: "object",
			properties: {
				firstName: {
					bsonType: "string",
				},
				lastName: {
					bsonType: "string",
				},
				customerId: {
					bsonType: "string",
				},
				wishlist: {
					bsonType: "array",
				},
			},
		},
	},
});

// Books
theArtOfWar = {
	title: "The Art Of War",
	genre: "Military Treatise",
	author: "Sun Tzu",
	bookId: "1599869772",
};

dune = {
	title: "Dune (Penguin Galaxy)",
	genre: "Sci-Fi",
	author: "Frank Herbert",
	bookId: "9780143111580",
};

hellstromsHive = {
	title: "HellstromsHive",
	genre: "Sci-Fi",
	author: "Frank Herbert",
	bookId: "0765317729",
};

thinkAndGrowRich = {
	title: "Think and Grow Rich",
	genre: "Self-Help",
	author: "Napoleon Hill",
	bookId: "1515406830",
};

theArtOfLoving = {
	title: "The Art of Loving",
	genre: "Self-Help",
	author: "Erich Fromm",
	bookId: "0061129739",
};

shutterIsland = {
	title: "Shutter Island",
	genre: "Mystery",
	author: "Dennis Lehane",
	bookId: "0061898813",
};

theGivenDay = {
	title: "Shutter Island",
	genre: "Mystery",
	author: "Dennis Lehane",
	bookId: "0380731878",
};

theHobbit = {
	title: "The Hobbit",
	genre: "Fantasy",
	author: "J. R. R. Tolkien",
	bookId: "054792822X",
};

theSilmarillion = {
	title: "The Silmarillion",
	genre: "Fantasy",
	author: "J. R. R. Tolkien",
	bookId: "0544338014",
};

theBookOfLostTales = {
	title: "The Book of Lost Tales",
	genre: "Fantasy",
	author: "J. R. R. Tolkien",
	bookId: "0395409276",
};

tomorrowAndTomorrowAndTomorrow = {
	title: "Tomorrow, and Tomorrow, and Tomorrow",
	genre: "Romance",
	author: "Gabrielle Zevin",
	bookId: "0593321200",
};

theRoadToChristmas = {
	title: "The Road to Christmas",
	genre: "Romance",
	author: "Sheila Roberts",
	bookId: "0778386562",
};

// Inserting book documents
db.books.insertOne(theArtOfWar);
db.books.insertOne(dune);
db.books.insertOne(thinkAndGrowRich);
db.books.insertOne(theArtOfLoving);
db.books.insertOne(shutterIsland);
db.books.insertOne(theHobbit);
db.books.insertOne(theSilmarillion);
db.books.insertOne(theBookOfLostTales);
db.books.insertOne(hellstromsHive);
db.books.insertOne(theGivenDay);
db.books.insertOne(tomorrowAndTomorrowAndTomorrow);
db.books.insertOne(theRoadToChristmas);

// Customers
baugh = {
	firstName: 'Ace',
	lastName: 'Baugh',
	customerId: 'c1001',
	wishlist: [
		{
			title: 'The Art Of War',
			genre: 'Military Treatise',
			author: 'Sun Tzu',
			bookId: '1599869772',
		},
		{
			title: 'Dune (Penguin Galaxy)',
			genre: 'Sci-Fi',
			author: 'Frank Herbert',
			bookId: '9780143111580',
		},
		{
			title: 'Think and Grow Rich',
			genre: 'Self-Help',
			author: 'Napoleon Hill',
			bookId: '1515406830',
		},
	],
};

damir = {
	firstName: 'Jamal',
	lastName: 'Damir',
	customerId: 'c1002',
	wishlist: [
		{
			title: 'The Art of Loving',
			genre: 'Self-Help',
			author: 'Erich Fromm',
			bookId: '0061129739',
		},
		{
			title: 'Shutter Island',
			genre: 'Mystery',
			author: 'Dennis Lehane',
			bookId: '0061898813',
		},
		{
			title: 'The Hobbit',
			genre: 'Fantasy',
			author: 'J. R. R. Tolkien',
			bookId: '054792822X',
		},
	],
};

// Inserting customer documents
db.customers.insertOne(baugh);
db.customers.insertOne(damir);

// Queries:

// Displaying list of books
db.books.find();
// Displaying books by genre
db.books.find({ genre: "Fantasy" });
// Displaying books by author
db.books.find({ author: "Sun Tzu" });
// Displaying books by bookId
db.books.find({ bookId: "1599869772" });
// Dioplaying the books in the wishlist of a customer
db.customers.find({ customerId: "c1001" }, { wishlist: 1 });
// Add a book to the wishlist
db.customers.updateOne( { customerId: "c1001" },
	{ $push: { wishlist: { title: "The Silmarillion", genre: "Fantasy", author: "J. R. R. Tolkien", bookId: "0544338014" } } } );
// Remove a book from the wishlist
db.customers.updateOne({ customerId: 'c1001' }, { $pull: { wishlist: { bookId: '0544338014' } } });

