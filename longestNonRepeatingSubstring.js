/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  var check = [];
  var counter = 0;
  var result = 0;
  allSubs = getAllSubstrings(s);
  allSubs.forEach((element) => {
    counter= 0
    check = []
    for (let i = 0; i < element.length; i++) {
      if (check.includes(element[i])) {
        return false;
      } else {
        counter++;
        check.push(element[i]);
        if (counter > result){
          result = counter
        }
      }
    }
  });

  return result;
};

function getAllSubstrings(str) {
  var i,
    j,
    result = [];
  for (i = 0; i < str.length; i++) {
    for (j = i + 1; j < str.length + 1; j++) {
      result.push(str.slice(i, j));
    }
  }
  return result;
}
