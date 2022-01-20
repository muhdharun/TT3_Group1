import axios from 'axios';

export default axios.create({
    baseURL: 'http://localhost:3500' //8000
})

//npx json-server -p 3500 -w data/db.json
//now launch the react app
// npm start
