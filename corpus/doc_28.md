# JavaScript Error Handling
doc_id: doc_28
topic: JavaScript
difficulty: intermediate

## try/catch
Wrap code that might fail in try/catch:
try {
  var data = JSON.parse(badJSON)
} catch (error) {
  console.log("Parse failed:", error.message)
}

## finally
The finally block always runs whether or not there was an error:
try {
  doSomething()
} catch (error) {
  console.log(error)
} finally {
  console.log("Always runs")
}

## Throwing Errors
throw new Error("Something went wrong")
throw new TypeError("Expected a string")

## Error Types
- Error — general error
- TypeError — wrong data type
- ReferenceError — variable not defined
- SyntaxError — invalid JavaScript syntax
- RangeError — value out of allowed range

## Console Methods for Debugging
- console.log() — general output
- console.error() — red error message
- console.warn() — yellow warning
- console.table() — display arrays/objects as table