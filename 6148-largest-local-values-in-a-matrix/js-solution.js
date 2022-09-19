Number.prototype[Symbol.iterator] = function* () {
    for (var i = 0; i < this; i++) yield i;
};

// range from [start, end). Note that end is exclusive
function* range(start, end) {
    for (let i = start; i < end; i++) yield i;
}

const largestLocal = (grid) =>
    [...range(0, grid.length - 2)].map((row) =>
        [...range(0, grid.length - 2)].map((col) =>
            Math.max(
                ...grid
                    .slice(row, row + 3)
                    .flatMap((rowObj) => rowObj.slice(col, col + 3))
            )
        )
    );

const largestLocalIterative = (grid) => {
    const res = [...Array(grid.length - 2)].map((_) =>
        Array(grid.length - 2).fill(0)
    );
    for (let i = 0; i < grid.length - 2; i++)
        for (let j = 0; j < grid.length - 2; j++)
            for (let ii = i; ii < i + 3; ii++)
                for (let jj = j; jj < j + 3; jj++)
                    res[i][j] = Math.max(res[i][j], grid[ii][jj]);
    return res;
};

const largestLocalIterativeBetter = (grid) => {
    const res = [...(grid.length - 2)].map((_) => Array(grid.length - 2).fill(0));
    for (const i of range(0, grid.length - 2))
        for (const j of range(0, grid.length - 2))
            for (const ii of range(i, i + 3))
                for (const jj of range(j, j + 3))
                    res[i][j] = Math.max(res[i][j], grid[ii][jj]);
    return res;
};

console.log(
    largestLocalIterativeBetter([
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2],
    ])
);
