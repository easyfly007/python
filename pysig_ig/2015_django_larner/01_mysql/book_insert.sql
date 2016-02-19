use books;

INSERT into customers values
(
	3,
	'Julie Smith',
	'25 Oak Street',
	'AIrport West'),
(
	4,
	'Alan Wong',
	'1/47 Haines Avenue',
	'Box Hill'),
(
	5,
	'Michelle Arthor',
	'357 North Road',
	'Yarraville');

INSERT into orders values
(NULL, 3, 69.98, '2007-04-02'),
(NULL, 1, 49.99, '2007-04-15'),
(NULL, 2, 74.98, '2007-04-19'),
(NULL, 3, 24.99, '2007-05-01');


INSERT into books values
(
	'0-672-31697-8',
	'Michael Margan',
	'Java 2 for professional developers',
	34.99),
(
	'0-672-31745-1',
	'Thomas Down',
	'Installing Debian GNU/Linux',
	24.99),
(
	'0-672-31509-2',
	'Pruitt, et al',
	'Teach Yourself GIMP in 24 hours',
	24.99),
(
	'0-672-31769-9',
	'Thomas Schenk',
	'Caldera OpenLinux System Administration Unleashed',
	49.99);

INSERT into order_items values
(1, '0-672-31697-8', 2),
(2, '0-672-31769-9', 1),
(3, '0-672-31769-9', 1),
(3, '0-672-31509-2', 1),
(4, '0-672-31745-1', 3);

INSERT into book_reviews values
('0-672-31697-8', 'The Morgan book is clearly written and goes well beyond most of the basic Java books out therre.');