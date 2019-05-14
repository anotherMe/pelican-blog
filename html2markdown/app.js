
/*
  Convert HTML files in *input* folder to markdown files in *output* folder

  ref: https://github.com/domchristie/turndown
*/

const TurndownService = require('turndown')
const path = require('path');
const fs = require('fs');

var turndownService = new TurndownService();
//turndownService.keep(['pre']) //make sure we keep pre elements
var blogDataPath = path.resolve(__dirname, './input');
var blogPath = path.resolve(__dirname, './output');
var markdownArray = fs.readdirSync(blogDataPath);

// read HTML files
markdownArray.filter(file => file.indexOf('.html') > -1)
  .map(file => {
    const markdown = fs.readFileSync(path.resolve(blogDataPath, file), 'utf8')
    const html = turndownService.turndown(markdown)
    return { file, html }
  })

// create new markdown files
markdownArray.forEach(item => {
  const filename = `${item.file.slice(0, -5)}.md`
  fs.writeFile(`${blogPath}/${filename}`, item.html, err => {
    if (err) {
      return console.log(err)
    }
    console.log(`${filename} saved`)
  })
})
