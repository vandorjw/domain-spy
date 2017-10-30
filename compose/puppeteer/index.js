const puppeteer = require('puppeteer')
const http = require('http')
const validUrl = require('valid-url')
const url = require('url')
const port = 3000

async function run(url) {
  console.log(url)
  // https://github.com/Googlechrome/puppeteer/issues/290#issuecomment-322921352
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']})
  const page = await browser.newPage()

  await page.goto(url)
  const content = await page.content()

  browser.close()
  return content
}

const requestHandler = (request, response) => {
  const parsedUrl = url.parse(request.url, true)
  const puppeteerURL = parsedUrl.query.url
  if (validUrl.isUri(puppeteerURL)) {
    content = run(parsedUrl.query.url)
    content.then(function(value){
      response.end(value)
    });
  } else {
    response.end("error: " + puppeteerURL)
  }
}

const server = http.createServer(requestHandler)

server.listen(port, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }
  console.log(`server is listening on ${port}`)
})
