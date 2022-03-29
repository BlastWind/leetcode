/*
  BFS with indegrees
*/

var canFinish = function (numCourses, prerequisites) {
  if (prerequisites.length === 0) return true;

  var incoming = Array.from({ length: numCourses }, () => []);
  var outgoing = Array.from({ length: numCourses }, () => []);

  for (var prereq of prerequisites) {
    outgoing[prereq[0]].push(prereq[1]);

    incoming[prereq[1]].push(prereq[0]);
  }

  for (let i = 0; i < outgoing.length; i++) {
    if (incoming[i].length === 0 && outgoing[i].length === 0) {
      outgoing[i] = null;
      incoming[i] = null;
    }
  }

  var noIncomingNodes = incoming.reduce(
    (accumulator, curVal, curIndex) =>
      curVal != null && curVal.length === 0
        ? accumulator.concat(curIndex)
        : accumulator,
    []
  );
  if (noIncomingNodes.length === 0) return false;
  var queue = [];
  noIncomingNodes.forEach((e) => queue.push(e));

  while (queue.length > 0) {
    var next = queue.pop();
    for (var out of outgoing[next]) {
      incoming[out] = incoming[out].filter((e) => e !== next);
      if (incoming[out].length === 0) {
        queue.push(out);
      }
    }
  }

  return incoming.every((node) => node === null || node.length === 0);
};

console.log(
  canFinish(3, [
    [1, 0],
    [2, 0],
  ])
);
