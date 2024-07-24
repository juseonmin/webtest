const fs = require('fs');
const path = require('path');

const directoryPath = path.join(__dirname, 'images');
const outputPath = path.join(__dirname, 'imageList.json');

fs.readdir(directoryPath, (err, files) => {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    }

    const imageFiles = files.filter(file => file.endsWith('.png'));
    fs.writeFileSync(outputPath, JSON.stringify(imageFiles, null, 2));
    console.log('Image list has been generated!');
});
