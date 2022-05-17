// permutations :: [a] -> [[a]]
const permutations = (xs) =>
  xs.length
    ? concatMap(
        // for each ele
        (
          x // a
        ) => concatMap((ys) => [[x].concat(ys)], permutations(delete_(x, xs))), // delete array by that ele and add it, entire concatMap returns [b] = [[]]
        xs // [a]
      ) // returns [b] = [[]]
    : [[]];

// GENERIC FUNCTIONS ----------------------------------

// concatMap :: (a -> [b]) -> [a] -> [b]
const concatMap = (f, xs) => xs.reduce((a, x) => a.concat(f(x)), []);

// delete :: Eq a => a -> [a] -> [a]
const delete_ = (x, xs) => {
  const go = (xs) => {
    return 0 < xs.length
      ? x === xs[0]
        ? xs.slice(1)
        : [xs[0]].concat(go(xs.slice(1)))
      : [];
  };
  return go(xs);
};

// TEST
console.log(JSON.stringify(permutations(["Aardvarks", "eat", "ants"])));

// concatMap executes function on every single element and push results into one array

// concatMap :: (a -> [b]) -> [a] -> [b]
// in this case, (a -> [b]) is (ys) => [[x].concat(ys)], so "a" is of type [], "b" is of type [], "[b]" is of type [[]], [a] is of type [[]]
// and so, [[x].concat(ys)] is [[]], ys is [], permutations(delete_(x, xs)) is [a], so it is [[]]
