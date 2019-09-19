create table 'book'(
id INTEGER primary key not null,
title varchar(512) not null,
page_count integer not null check(page_count>0)
);

create table author(
id integer primary key not null,
name varchar(255) not null
);

create table author_book(
author_id integer not null,
book_id integer not null,
foreign key(author_id) REFERENCES author(id),
foreign key (book_id) references book(id),
UNIQUE(author_id,book_id)
);

select title,page_count, group_concat(author.name, '/') from book
join author_book on book.id=author_book.book_id
join author on author_book.author_id=author.id
where author.name in ('Mashka','Dashka')
group by book_id;

select author.name,book.title from author
join author_book on author.id=author_book.author_id
join book on author_book.book_id=book.id
where book.title ='GariShproter9'
group by book_id;


select book.title,group_concat(author.name)from author
join author_book on author.id=author_book.author_id
join book on author_book.book_id=book.id
where book.title like '%GariShproter1%'
group by book_id



select group_concat(author.name,' & ') as authors,book.title from book
join author_book on book.id=author_book.book_id
join author on author_book.author_id=author.id
where book.page_count BETWEEN 100 and 1000
group by book.id;