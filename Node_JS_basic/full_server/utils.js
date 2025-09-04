import fs from 'fs';

/**
 * Reads a CSV database file and returns student data organized by field
 * @param {string} filePath
 * @returns {Promise<Object>}
 */
function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        if (lines.length <= 1) {
          resolve({});
          return;
        }

        const students = lines.slice(1).filter((line) => {
          const fields = line.split(',');
          return fields.length >= 4 && fields.every((field) => field.trim() !== '');
        });

        const studentsByField = {};

        students.forEach((student) => {
          const studentData = student.split(',');
          const firstName = studentData[0].trim();
          const field = studentData[3].trim();

          if (!studentsByField[field]) {
            studentsByField[field] = [];
          }
          studentsByField[field].push(firstName);
        });

        resolve(studentsByField);
      } catch (parseError) {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

export default readDatabase;
