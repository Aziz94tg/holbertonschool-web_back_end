const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }

      const students = lines.slice(1).filter((line) => {
        const fields = line.split(',');
        return fields.length >= 4 && fields.every((field) => field.trim() !== '');
      });

      const totalStudents = students.length;
      const fields = {};

      students.forEach((student) => {
        const studentData = student.split(',');
        const firstName = studentData[0].trim();
        const field = studentData[3].trim();

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      let result = `Number of students: ${totalStudents}\n`;

      Object.keys(fields).forEach((field) => {
        const count = fields[field].length;
        const names = fields[field].join(', ');
        result += `Number of students in ${field}: ${count}. List: ${names}\n`;
      });

      resolve(result.trim());
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text/plain');

  try {
    const databasePath = process.argv[2];
    if (!databasePath) {
      res.send('This is the list of our students\nCannot load the database');
      return;
    }

    const studentInfo = await countStudents(databasePath);
    res.send(`This is the list of our students\n${studentInfo}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(1245, () => {
  console.log('Express server listening on port 1245');
});

module.exports = app;
