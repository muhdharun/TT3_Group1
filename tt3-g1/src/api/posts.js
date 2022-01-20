import axios from 'axios';

export default axios.create({
    baseURL: 'https://localhost:3500'
})

//npx json-server -p 3500 -w data/db.json
//now launch the react app
// npm start
