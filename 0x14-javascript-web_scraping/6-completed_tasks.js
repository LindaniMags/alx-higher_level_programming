const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(error);
  } else {
    const complete = {};

    body.forEach((task) => {
      if (task.completed) {
        if (complete[task.userId]) {
          complete[task.userId]++;
        } else {
          complete[task.userId] = 1;
        }
      }
    });
    for (const userId in complete) {
      console.log(`'${userId}': ${complete[userId]},\n`);
    }
  }
});
