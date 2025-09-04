/**
 * App Controller
 */
class AppController {
  /**
     * GET /
     * Returns homepage message
     * @param {Object} request
     * @param {Object} response
     */
  static getHomepage(request, response) {
    response.status(200).send('Hello Holberton School!');
  }
}

export default AppCon;
