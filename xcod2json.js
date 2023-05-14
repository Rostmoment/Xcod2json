const fs = require('fs');
let jsondata = {
  data: [],
  textures: []
};

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter xcod name: ', (filename) => {
  fs.readFile(filename, 'hex', (err, data) => {
    if (err) {
      console.error(err);
      rl.close();
      return;
    }
    const picCount = parseInt(data.slice(10, 12), 16);
    let parse = 7;
    let parseWidth = 8;
    let parseWidth2 = 9;
    let parseHeight = 10;
    let parseHeight2 = 11;

    for (let i = 0; i < picCount; i++) {
      const pixelType = parseInt(data.slice(parse * 2, (parse * 2) + 2), 16);
      const width1 = parseInt(data.slice(parseWidth * 2, (parseWidth * 2) + 2), 16);
      const width2 = parseInt(data.slice(parseWidth2 * 2, (parseWidth2 * 2) + 2), 16);
      const height1 = parseInt(data.slice(parseHeight * 2, (parseHeight * 2) + 2), 16);
      const height2 = parseInt(data.slice(parseHeight2 * 2, (parseHeight2 * 2) + 2), 16);
      const width = (width1 * 256) + width2;
      const height = (height1 * 256) + height2;

      const texture = {
        pixelType: pixelType,
        width: width,
        height: height
      };
      jsondata.textures.push(texture);

      parse += 6;
      parseHeight += 6;
      parseHeight2 += 6;
      parseWidth += 6;
      parseWidth2 += 6;
    }

    const picData = {
      pictureCount: picCount
    };
    jsondata.data.push(picData);
    const jsonfile = JSON.stringify(jsondata, null, 4);
    const newFilename = filename.replace('.xcod', '.json');
    fs.writeFile(newFilename, jsonfile, (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log('JSON file has been written successfully.');
      }
      rl.close();
    });
  });
});
