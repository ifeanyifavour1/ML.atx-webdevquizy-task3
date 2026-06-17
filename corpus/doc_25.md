# JavaScript Promises and Async/Await
doc_id: doc_25
topic: JavaScript
difficulty: intermediate

## What is a Promise?
A Promise represents a value that will be available in the future. It can be pending, fulfilled, or rejected.

## Creating a Promise
var promise = new Promise(function(resolve, reject) {
  if (success) { resolve("Data loaded") }
  else { reject("Error occurred") }
})

## Using .then and .catch
promise
  .then(function(result) { console.log(result) })
  .catch(function(error) { console.log(error) })

## Promise Chaining
fetch(url)
  .then(function(res) { return res.json() })
  .then(function(data) { return processData(data) })
  .then(function(result) { console.log(result) })
  .catch(function(error) { console.log(error) })

## async/await
async function loadData() {
  try {
    var response = await fetch(url)
    var data = await response.json()
    console.log(data)
  } catch (error) {
    console.log(error)
  }
}

## Promise.all
Run multiple promises in parallel:
var results = await Promise.all([fetch(url1), fetch(url2)])