import readDatabase from '../utils.js';

/**
 * Students Controller
 */
class StudentsController {
  /**
   * GET /students
   * Returns list of all students organized by field
   * @param {Object} request - Express request object
   * @param {Object} response - Express response object
   */
  static async getAllStudents(request, response) {
    const databasePath = process.argv[2];

    try {
      const studentsByField = await readDatabase(databasePath);

      let responseText = 'This is the list of our students\n';

      const sortedFields = Object.keys(studentsByField).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      sortedFields.forEach((field) => {
        const students = studentsByField[field];
        const count = students.length;
        const namesList = students.join(', ');
        responseText += `Number of students in ${field}: ${count}. List: ${namesList}\n`;
      });

      response.status(200).send(responseText.trim());
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }

  /**
   * GET /students/:major
   * Returns list of students filtered by major
   * @param {Object} request
   * @param {Object} response
   */
  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    const databasePath = process.argv[2];

    // Validate major parameter
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const studentsByField = await readDatabase(databasePath);

      if (studentsByField[major]) {
        const namesList = studentsByField[major].join(', ');
        response.status(200).send(`List: ${namesList}`);
      } else {
        response.status(200).send('List: ');
      }
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
