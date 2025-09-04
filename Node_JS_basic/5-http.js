const http = require('http');
const fs = require('fs');
const url = require('url');

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

const app = http.createServer(async (req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const path = parsedUrl.pathname;

  res.setHeader('Content-Type', 'text/plain');

  if (path === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (path === '/students') {
    res.statusCode = 200;
    res.write('This is the list of our students\n');

    try {
      const databasePath = process.argv[2];
      if (!databasePath) {
        res.write('Cannot load the database');
        res.end();
        return;
      }

      const studentInfo = await countStudents(databasePath);
      res.end(studentInfo);
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

module.exports = app;
