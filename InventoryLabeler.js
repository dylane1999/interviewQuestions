function deviceNamesSystem(devicenames) {
  // Write your code here
  var results = [];
  var counter = 1;
  devicenames.forEach((element) => {
    if (!results.includes(element)) {
      results.push(element);
    } else {
      while (results.includes(element)) {
        temp = element + counter;
        counter++;
        if (!results.includes(temp)) {
          results.push(temp);
          counter = 1;
          break;
        }
      }
    }
  });

  return results;
}
