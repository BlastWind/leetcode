const go = (xs) =>
  xs.length
    ? concatMap(
        // for each ele
        (x) => concatMap((ys) => [[x].concat(ys)], go(delete_(x, xs))), // delete array by that ele and add it
        xs
      )
    : [[]];

/*

Let's say xs = [1, 2, 3]

Then, answer is concatMap((x) => concatMap((ys) => [[x].concat(ys)], go(delete_(x, [1, 2, 3]))), [1, 2, 3]))

Which gets peeled into 
[1, 2, 3].reduce((a, x) => a.concat(
	(x) => concatMap((ys) => [[x].concat(ys)], go(delete_(x, [1, 2, 3]))), [1, 2, 3])(x)
), []);

Reduce iteration 1: 
	a: [], x: 1 
	[].concat((1) => concatMap((ys) => [[1].concat(ys)], go(delete_(1, [1, 2, 3]))), [1, 2, 3])(1)
)



*/
